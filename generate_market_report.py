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
        
        # Get data
        yields_df = self.get_yield_data()
        ownership_df = self.get_ownership_data()
        trans_df = self.get_transaction_data()
        
        if yields_df is None or len(yields_df) == 0:
            print("No data available")
            return
        
        latest_date = yields_df['date'].iloc[0]
        print(f"\n{latest_date}\n")
        print("SBN Daily Market Update\n")
        
        # Yield changes
        yield_changes = self.calculate_yield_changes(yields_df)
        if yield_changes:
            print("Headlines Pasar SUN")
            print("• Pasar SUN bergerak " + yield_changes['trend'] + 
                  f". Berdasarkan yield rata-rata, yield SUN " +
                  f"bergerak {yield_changes['trend']} sebesar {abs(yield_changes['change_bps']):.1f} bps" +
                  f" dibandingkan hari kemarin (dari {yield_changes['yesterday_yield']:.4f}% menjadi {yield_changes['today_yield']:.4f}%).\n")
        
        # Ownership summary
        ownership = self.calculate_ownership_changes(ownership_df)
        if ownership:
            print("• Kepemilikan SBN per " + str(ownership['date']) + ":")
            print(f"  - Investor Domestik Individu: Rp{ownership['domestic_individual']/1e12:.2f} T")
            print(f"  - Investor Domestik Korporat: Rp{ownership['domestic_company']/1e12:.2f} T")
            print(f"  - Non Resident: Rp{ownership['non_resident']/1e12:.2f} T")
            print(f"  - Total: Rp{ownership['total']/1e12:.2f} T\n")
        
        # Transaction summary
        if trans_df is not None and len(trans_df) > 0:
            print("Headlines Pasar Transaksi")
            print("-" * 80)
            
            total_volume = trans_df['total_volume'].sum() / 1e12
            total_value = trans_df['total_value'].sum() / 1e12
            
            print(f"• Total transaksi hari ini: Rp{total_volume:.2f} T (nominal), Rp{total_value:.2f} T (nilai)")
            
            # Group by transaction type
            trans_by_type = trans_df.groupby('trans_type').agg({
                'total_volume': 'sum',
                'total_value': 'sum',
                'avg_yield': 'mean'
            })
            
            print("\nRingkasan Transaksi per Jenis:")
            for idx, row in trans_by_type.iterrows():
                print(f"  {idx}: Rp{row['total_volume']/1e12:.2f} T | Yield rata-rata: {row['avg_yield']:.4f}%")
            print()
        
        print("=" * 80)
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
