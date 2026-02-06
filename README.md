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

### Output
The script generates a comprehensive market update including:
- Yield movements and changes vs. previous day
- SBN ownership breakdown (domestic individual, corporate, non-resident)
- Transaction summary by type
- Volume and value totals
