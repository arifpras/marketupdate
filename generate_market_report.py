#!/usr/bin/env python3
"""
Market Update Report Generator
Generates daily market update reports from AKP databases
"""

import sqlite3
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path
import sys

# Database paths
DB_DIR = Path(__file__).parent / "10. Database AKP"
DB_KEPEMILIKAN = DB_DIR / "DB_Kepemilikan.db"
DB_PLTE = DB_DIR / "DB_PLTE.db"
DB_TRANSAKSI = DB_DIR / "DB_Transaksi_Harian.db"
DB_SUBREG = DB_DIR / "DB_Subreg.db"
DB_DOMESTIK = DB_DIR / "Database_Domestik_Internasional.db"


class MarketReportGenerator:
    def __init__(self):
        self.report_date = None
        self.previous_date = None
        self.data = {}
        
    def get_latest_date(self, db_path, table_name, date_col):
        """Get the latest date from a database table"""
        try:
            conn = sqlite3.connect(db_path)
            query = f"SELECT MAX({date_col}) FROM {table_name}"
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchone()[0]
            conn.close()
            return result
        except Exception as e:
            print(f"Error getting latest date from {db_path}: {e}")
            return None
    
    def get_yield_data(self):
        """Extract yield data from DB_PLTE"""
        try:
            conn = sqlite3.connect(DB_PLTE)
            query = """
            SELECT 
                tanggal_transaksi as date,
                Securities_Id as security,
                Yield as yield,
                Price as price,
                Coupon_Rate as coupon,
                Volume as volume,
                Value as value
            FROM DB_PLTE
            WHERE tanggal_transaksi IN (
                SELECT DISTINCT tanggal_transaksi FROM DB_PLTE 
                ORDER BY tanggal_transaksi DESC LIMIT 2
            )
            ORDER BY tanggal_transaksi DESC, Securities_Id
            """
            df = pd.read_sql_query(query, conn)
            conn.close()
            return df
        except Exception as e:
            print(f"Error getting yield data: {e}")
            return None
    
    def get_benchmark_yields(self):
        """Extract benchmark yield data - average yield per security per day"""
        try:
            conn = sqlite3.connect(DB_PLTE)
            # Common benchmark series - get average yield per day
            query = """
            SELECT 
                tanggal_transaksi as date,
                Securities_Id as security,
                AVG(Yield) as yield,
                AVG(Price) as price,
                MAX(Mature_Date) as maturity
            FROM DB_PLTE
            WHERE tanggal_transaksi IN (
                SELECT DISTINCT tanggal_transaksi FROM DB_PLTE 
                ORDER BY tanggal_transaksi DESC LIMIT 2
            )
            AND Securities_Id IN (
                'FR0091', 'FR0092', 'FR0093', 'FR0094', 'FR0095', 
                'FR0096', 'FR0097', 'FR0098', 'FR0099'
            )
            AND Yield > 0
            GROUP BY tanggal_transaksi, Securities_Id
            ORDER BY tanggal_transaksi DESC, Mature_Date
            """
            df = pd.read_sql_query(query, conn)
            conn.close()
            return df
        except Exception as e:
            print(f"Error getting benchmark yields: {e}")
            return None
    
    def get_ownership_data(self):
        """Extract ownership data from DB_Kepemilikan"""
        try:
            conn = sqlite3.connect(DB_KEPEMILIKAN)
            query = """
            SELECT 
                tanggal as date,
                KATEGORI_SBN as category,
                Total_CN as domestic_individual,
                Total_CR as domestic_company,
                Total_OR as non_resident
            FROM Kepemilikan_Investor_Tradable
            ORDER BY tanggal DESC LIMIT 2
            """
            df = pd.read_sql_query(query, conn)
            conn.close()
            return df
        except Exception as e:
            print(f"Error getting ownership data: {e}")
            return None
    
    def get_transaction_data(self):
        """Extract transaction data from DB_Transaksi_Harian"""
        try:
            conn = sqlite3.connect(DB_TRANSAKSI)
            query = """
            SELECT 
                TANGGAL_SETELMEN as settle_date,
                JENIS_TRANSAKSI as trans_type,
                SERI as series,
                COUNT(*) as transaction_count,
                SUM(NOMINAL) as total_volume,
                SUM(NILAI_TRANSAKSI) as total_value,
                AVG(YIELD) as avg_yield
            FROM Transaksi_Harian
            WHERE TANGGAL_SETELMEN IN (
                SELECT DISTINCT TANGGAL_SETELMEN FROM Transaksi_Harian
                ORDER BY TANGGAL_SETELMEN DESC LIMIT 2
            )
            GROUP BY TANGGAL_SETELMEN, JENIS_TRANSAKSI
            ORDER BY TANGGAL_SETELMEN DESC
            """
            df = pd.read_sql_query(query, conn)
            conn.close()
            return df
        except Exception as e:
            print(f"Error getting transaction data: {e}")
            return None
    
    def get_fx_data(self):
        """Extract FX rate data"""
        try:
            conn = sqlite3.connect(DB_DOMESTIK)
            query = """
            SELECT tanggal, USD, EUR, JPY, SGD
            FROM Kurs_IDR
            ORDER BY tanggal DESC LIMIT 2
            """
            df = pd.read_sql_query(query, conn)
            conn.close()
            return df
        except Exception as e:
            print(f"Error getting FX data: {e}")
            return None
    
    def get_ust_data(self):
        """Extract US Treasury yield data"""
        try:
            conn = sqlite3.connect(DB_DOMESTIK)
            query = """
            SELECT tanggal, Indonesia, USA
            FROM '10Y_General'
            ORDER BY tanggal DESC LIMIT 2
            """
            df = pd.read_sql_query(query, conn)
            conn.close()
            return df
        except Exception as e:
            print(f"Error getting UST data: {e}")
            return None
    
    def get_cds_data(self):
        """Extract CDS data"""
        try:
            conn = sqlite3.connect(DB_DOMESTIK)
            query = """
            SELECT DISTINCT tanggal, PRICE as price, TENOR as tenor
            FROM CDS_Indo
            WHERE TENOR IN ('CDS 5Y', 'CDS 10Y')
            AND tanggal IN (
                SELECT DISTINCT tanggal FROM CDS_Indo ORDER BY tanggal DESC LIMIT 1
            )
            ORDER BY tanggal DESC, TENOR
            """
            df = pd.read_sql_query(query, conn)
            conn.close()
            return df
        except Exception as e:
            print(f"Error getting CDS data: {e}")
            return None
    
    def get_ndf_data(self):
        """Extract NDF data"""
        try:
            conn = sqlite3.connect(DB_DOMESTIK)
            query = """
            SELECT tanggal, IHN_1M_Curncy, IHN_6M_Curncy, IHN_12M_Curncy
            FROM NDF_Update
            ORDER BY tanggal DESC LIMIT 2
            """
            df = pd.read_sql_query(query, conn)
            conn.close()
            return df
        except Exception as e:
            print(f"Error getting NDF data: {e}")
            return None
    
    def get_stock_indices(self):
        """Extract stock index data"""
        try:
            conn = sqlite3.connect(DB_DOMESTIK)
            query = """
            SELECT tanggal, Indonesia, USA, Japan, Hongkong, Shanghai, German
            FROM Saham_Peers
            ORDER BY tanggal DESC LIMIT 2
            """
            df = pd.read_sql_query(query, conn)
            conn.close()
            return df
        except Exception as e:
            print(f"Error getting stock index data: {e}")
            return None
    
    def get_commodity_data(self):
        """Extract commodity price data"""
        try:
            conn = sqlite3.connect(DB_DOMESTIK)
            query = """
            SELECT tanggal, ICP, WTI, PALM_OIL
            FROM Commodity_DB
            ORDER BY tanggal DESC LIMIT 2
            """
            df = pd.read_sql_query(query, conn)
            conn.close()
            return df
        except Exception as e:
            print(f"Error getting commodity data: {e}")
            return None
    
    def calculate_yield_changes(self, yields_df):
        """Calculate yield changes between latest two dates"""
        if yields_df is None or len(yields_df) < 2:
            return None
        
        # Filter out invalid yields (0 or very high)
        yields_clean = yields_df[(yields_df['yield'] > 0) & (yields_df['yield'] < 20)].copy()
        
        dates = yields_clean['date'].unique()[:2]  # Latest 2 dates
        if len(dates) < 2:
            return None
        
        today = yields_clean[yields_clean['date'] == dates[0]].groupby('date')['yield'].agg(['mean', 'std']).iloc[0]
        yesterday = yields_clean[yields_clean['date'] == dates[1]].groupby('date')['yield'].agg(['mean', 'std']).iloc[0]
        
        change_bps = (today['mean'] - yesterday['mean']) * 100  # Convert to basis points
        
        return {
            'date': dates[0],
            'prev_date': dates[1],
            'today_yield': today['mean'],
            'yesterday_yield': yesterday['mean'],
            'change_bps': change_bps,
            'trend': 'naik' if change_bps > 0 else 'turun'
        }
    
    def calculate_ownership_changes(self, ownership_df):
        """Calculate ownership changes"""
        if ownership_df is None or len(ownership_df) == 0:
            return None
        
        # Group by date and sum ownership
        ownership_summary = ownership_df.groupby('date')[['domestic_individual', 'domestic_company', 'non_resident']].sum()
        
        if len(ownership_summary) >= 1:
            latest = ownership_summary.iloc[0]
            total_ownership = latest.sum()
            
            return {
                'date': ownership_summary.index[0],
                'domestic_individual': latest['domestic_individual'],
                'domestic_company': latest['domestic_company'],
                'non_resident': latest['non_resident'],
                'total': total_ownership
            }
        return None
    
    def generate_report(self):
        """Generate the market update report"""
        print("\n" + "="*80)
        print("DIREKTORAT JENDERAL PENGELOLAAN PEMBIAYAAN DAN RISIKO")
        print("KEMENTERIAN KEUANGAN RI")
        print("="*80)
        
        # Get all data
        yields_df = self.get_yield_data()
        benchmark_df = self.get_benchmark_yields()
        ownership_df = self.get_ownership_data()
        trans_df = self.get_transaction_data()
        fx_df = self.get_fx_data()
        ust_df = self.get_ust_data()
        cds_df = self.get_cds_data()
        ndf_df = self.get_ndf_data()
        stocks_df = self.get_stock_indices()
        commodity_df = self.get_commodity_data()
        
        if yields_df is None or len(yields_df) == 0:
            print("No data available")
            return
        
        latest_date = yields_df['date'].iloc[0]
        print(f"\n{latest_date}\n")
        print("SBN Daily Market Update\n")
        
        # ======================== HEADLINES PASAR SUN ========================
        print("Headlines Pasar SUN")
        print("-" * 80)
        
        # Yield changes
        yield_changes = self.calculate_yield_changes(yields_df)
        if yield_changes:
            print("• Pasar SUN bergerak " + yield_changes['trend'] + 
                  f". Berdasarkan yield rata-rata, yield SUN " +
                  f"bergerak {yield_changes['trend']} sebesar {abs(yield_changes['change_bps']):.1f} bps" +
                  f" dibandingkan hari kemarin (dari {yield_changes['yesterday_yield']:.4f}% menjadi {yield_changes['today_yield']:.4f}%).")
        
        # FX rate changes
        if fx_df is not None and len(fx_df) >= 2:
            usd_today = fx_df.iloc[0]['USD']
            usd_yesterday = fx_df.iloc[1]['USD']
            usd_change = usd_today - usd_yesterday
            trend = "melemah" if usd_change > 0 else "menguat"
            print(f"  Nilai tukar Rupiah {trend} sebesar {abs(usd_change):.2f} poin ke level Rp{usd_today:,.0f}/US$.")
        
        # Stock index (IHSG)
        if stocks_df is not None and len(stocks_df) >= 2:
            ihsg_today = stocks_df.iloc[0]['Indonesia']
            ihsg_yesterday = stocks_df.iloc[1]['Indonesia']
            ihsg_change = ihsg_today - ihsg_yesterday
            ihsg_pct = (ihsg_change / ihsg_yesterday) * 100
            trend = "naik" if ihsg_change > 0 else "turun"
            print(f"  Indeks IHSG {trend} sebesar {abs(ihsg_change):.2f} poin ({ihsg_pct:.2f}%) ke level {ihsg_today:,.2f}.")
        
        print()
        
        # Ownership summary
        ownership = self.calculate_ownership_changes(ownership_df)
        if ownership:
            print("• Kepemilikan SBN per " + str(ownership['date']) + ":")
            print(f"  - Investor Domestik Individu: Rp{ownership['domestic_individual']/1e12:.2f} T")
            print(f"  - Investor Domestik Korporat: Rp{ownership['domestic_company']/1e12:.2f} T")
            print(f"  - Non Resident: Rp{ownership['non_resident']/1e12:.2f} T")
            print(f"  - Total Kepemilikan: Rp{ownership['total']/1e12:.2f} T")
        
        print()
        
        # Transaction summary
        if trans_df is not None and len(trans_df) > 0:
            # Filter today's transactions
            latest_settle = trans_df['settle_date'].iloc[0]
            today_trans = trans_df[trans_df['settle_date'] == latest_settle]
            
            # Calculate outright, repo non-BI, repo BI
            outright_types = ['SALE', 'ALLOTMENT', 'FOP']
            repo_types = ['REPO', 'REPO 2nd LEG']
            
            outright_vol = today_trans[today_trans['trans_type'].isin(outright_types)]['total_volume'].sum() / 1e12
            repo_vol = today_trans[today_trans['trans_type'].isin(repo_types)]['total_volume'].sum() / 1e12
            
            print("• Transaksi Perdagangan Harian:")
            print(f"  - Transaksi Outright: Rp{outright_vol:.2f} T")
            print(f"  - Transaksi Repo: Rp{repo_vol:.2f} T")
        
        print("\n")
        
        # ======================== BENCHMARK YIELDS ========================
        if benchmark_df is not None and len(benchmark_df) > 0:
            print("Yield SUN Seri Benchmark")
            print("-" * 80)
            
            dates = benchmark_df['date'].unique()
            if len(dates) >= 2:
                today_bench = benchmark_df[benchmark_df['date'] == dates[0]]
                yesterday_bench = benchmark_df[benchmark_df['date'] == dates[1]]
                
                print(f"{'Seri':<10} {'Yield Hari Ini':>15} {'Yield Kemarin':>15} {'Perubahan (bps)':>18}")
                print("-" * 80)
                
                for _, row_today in today_bench.iterrows():
                    security = row_today['security']
                    yield_today = row_today['yield']
                    
                    # Find matching yesterday data
                    yesterday_row = yesterday_bench[yesterday_bench['security'] == security]
                    if not yesterday_row.empty:
                        yield_yesterday = yesterday_row.iloc[0]['yield']
                        change_bps = (yield_today - yield_yesterday) * 100
                        
                        print(f"{security:<10} {yield_today:>14.4f}% {yield_yesterday:>14.4f}% {change_bps:>17.2f}")
                
                print()
        
        print()
        
        # ======================== HEADLINES PASAR INTERNASIONAL ========================
        print("Headlines Pasar Internasional")
        print("-" * 80)
        
        # US Treasury yields
        if ust_df is not None and len(ust_df) >= 2:
            indo_yield_today = ust_df.iloc[0]['Indonesia']
            indo_yield_yesterday = ust_df.iloc[1]['Indonesia']
            indo_change = (indo_yield_today - indo_yield_yesterday) * 100  # to bps
            
            ust_yield_today = ust_df.iloc[0]['USA']
            ust_yield_yesterday = ust_df.iloc[1]['USA']
            ust_change = (ust_yield_today - ust_yield_yesterday) * 100
            
            # Calculate spread
            spread_today = (indo_yield_today - ust_yield_today) * 100  # in bps
            spread_yesterday = (indo_yield_yesterday - ust_yield_yesterday) * 100
            spread_change = spread_today - spread_yesterday
            
            indo_trend = "naik" if indo_change > 0 else "turun"
            ust_trend = "naik" if ust_change > 0 else "turun"
            
            print(f"• Yield Global Bonds Indonesia (SUN Valas) 10Y bergerak {indo_trend} {abs(indo_change):.1f} bps ke {indo_yield_today:.3f}%.")
            print(f"  Yield US Treasury 10Y bergerak {ust_trend} {abs(ust_change):.1f} bps ke {ust_yield_today:.3f}%.")
            print(f"  Spread Indonesia terhadap UST 10Y: {spread_today:.0f} bps ({spread_change:+.0f} bps dari hari sebelumnya).")
        
        # CDS data
        if cds_df is not None and len(cds_df) >= 1:
            print(f"\n• Credit Risk Indonesia (CDS):")
            for i, row in cds_df.iterrows():
                print(f"  - {row['tenor']}: {row['price']:.2f} bps")
        
        # NDF data
        if ndf_df is not None and len(ndf_df) >= 2:
            ndf_1m_today = ndf_df.iloc[0]['IHN_1M_Curncy']
            ndf_1m_yesterday = ndf_df.iloc[1]['IHN_1M_Curncy']
            ndf_6m_today = ndf_df.iloc[0]['IHN_6M_Curncy']
            ndf_12m_today = ndf_df.iloc[0]['IHN_12M_Curncy']
            
            ndf_1m_change = ndf_1m_today - ndf_1m_yesterday
            trend = "naik" if ndf_1m_change > 0 else "turun"
            
            print(f"\n• Nilai NDF bergerak {trend} pada hari ini:")
            print(f"  - NDF 1M: {ndf_1m_today:,.0f} ({ndf_1m_change:+.0f} poin)")
            print(f"  - NDF 6M: {ndf_6m_today:,.0f}")
            print(f"  - NDF 12M: {ndf_12m_today:,.0f}")
        
        # Global stock indices
        if stocks_df is not None and len(stocks_df) >= 2:
            print(f"\n• Indeks Saham Global (perubahan hari ini):")
            indices = {
                'USA': 'S&P 500',
                'Japan': 'Nikkei',
                'Hongkong': 'Hang Seng',
                'Shanghai': 'Shanghai',
                'German': 'DAX'
            }
            
            for key, label in indices.items():
                if key in stocks_df.columns:
                    today_val = stocks_df.iloc[0][key]
                    yesterday_val = stocks_df.iloc[1][key]
                    change = today_val - yesterday_val
                    pct_change = (change / yesterday_val) * 100
                    trend = "naik" if change > 0 else "turun"
                    print(f"  - {label}: {trend} {abs(pct_change):.2f}% ke {today_val:,.2f}")
        
        # Commodity prices
        if commodity_df is not None and len(commodity_df) >= 1:
            icp = commodity_df.iloc[0]['ICP']
            palm_oil = commodity_df.iloc[0]['PALM_OIL']
            wti = commodity_df.iloc[0]['WTI']
            
            print(f"\n• Harga Komoditas:")
            print(f"  - Minyak Mentah ICP: US${icp:.2f} per barel")
            print(f"  - Minyak Mentah WTI: US${wti:.2f} per barel")
            print(f"  - Minyak Sawit: US${palm_oil:.2f} per metric ton")
        
        print("\n" + "=" * 80)
        print(f"Report generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80 + "\n")
    
    def export_to_text(self, filename=None):
        """Export report to text file"""
        if filename is None:
            filename = f"Market_Update_{datetime.now().strftime('%Y%m%d')}.txt"
        
        # Redirect print to file
        filepath = Path(__file__).parent / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            # Capture report content
            sys.stdout = f
            self.generate_report()
            sys.stdout = sys.__stdout__
        
        print(f"Report exported to: {filepath}")
        return filepath


if __name__ == "__main__":
    generator = MarketReportGenerator()
    generator.generate_report()
    generator.export_to_text()
