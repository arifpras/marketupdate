# Market Update

This repository contains the market update materials, database files, and automated report generation tools for the TK4_202601 cycle.

## Contents
- **Market Update Documents**: Daily summary reports in PDF/TXT format
- **Database Files** (`10. Database AKP/`):
  - `DB_Kepemilikan.db` - SBN ownership data by investor type
  - `DB_PLTE.db` - Pricing, yields, and transaction details
  - `DB_Transaksi_Harian.db` - Daily settlement transactions
  - `DB_Subreg.db` - Sub-regional data
  - `Database_Domestik_Internasional.db` - Domestic and international market data
- **Automation Scripts**:
  - `generate_market_report.py` - Automated report generator from databases
  - Workflow guides and process documentation

## Report Generation

### Usage
```bash
python3 generate_market_report.py
```

This script:
- Extracts the latest market data from the AKP databases
- Calculates yield changes and market movements
- Generates a formatted market update report
- Exports to `Market_Update_[YYYYMMDD].txt`

### Requirements
- Python 3.6+
- pandas
- sqlite3 (built-in)

### Report Sections

#### Headlines Pasar SUN
- **Yield movements**: Average yield changes vs. previous day (in basis points)
- **FX rates**: Rupiah/USD movements and levels
- **IHSG**: Indonesian stock index changes
- **SBN ownership**: Breakdown by investor type (domestic individual, corporate, non-resident)
- **Transaction summary**: Daily outright and repo transaction volumes

#### Benchmark Yields Table
- Displays major benchmark series (FR0091-FR0099)
- Shows current vs. previous day yields
- Calculates basis point changes for each series

#### Headlines Pasar Internasional
- **US Treasury yields**: 10Y yield movements and trends
- **Spread analysis**: Indonesia 10Y vs. UST 10Y spread (in bps)
- **CDS spreads**: 5Y and 10Y credit default swap levels
- **NDF rates**: 1-month, 6-month, and 12-month forward rates
- **Global stock indices**: 
  - US (S&P 500)
  - Japan (Nikkei)
  - Hong Kong (Hang Seng)
  - China (Shanghai)
  - Europe (DAX)
- **Commodity prices**:
  - Indonesian Crude Price (ICP)
  - WTI crude oil
  - Palm oil

### Sample Output
```
================================================================================
DIREKTORAT JENDERAL PENGELOLAAN PEMBIAYAAN DAN RISIKO
KEMENTERIAN KEUANGAN RI
================================================================================

2026-02-05

SBN Daily Market Update

Headlines Pasar SUN
--------------------------------------------------------------------------------
• Pasar SUN bergerak turun. Berdasarkan yield rata-rata, yield SUN bergerak turun 
  sebesar 5.4 bps dibandingkan hari kemarin (dari 5.9441% menjadi 5.8899%).
  Nilai tukar Rupiah melemah sebesar 55.00 poin ke level Rp16,830/US$.
  Indeks IHSG turun sebesar 42.84 poin (-0.53%) ke level 8,103.88.

• Kepemilikan SBN per 2026-02-05:
  - Investor Domestik Individu: Rp27.39 T
  - Investor Domestik Korporat: Rp90.73 T
  - Non Resident: Rp0.00 T
  - Total Kepemilikan: Rp118.12 T

• Transaksi Perdagangan Harian:
  - Transaksi Outright: Rp78.57 T
  - Transaksi Repo: Rp38.36 T
```

## Data Sources
All data is sourced from official AKP (Akun Khusus Pemodal) databases maintained by DJPPR Kemenkeu RI.
