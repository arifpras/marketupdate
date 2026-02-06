# Quick Guide: AI Prompts for Market Update Summaries

## Complete Prompt Template for Users

### Use Case
When you have a data report PDF (e.g., Market Update 20260205x.pdf) and need to generate a summary for the first page following DJPPR standards.

### Full Prompt to Use

```
I have a Market Update data report that needs a summary for the first page.

DATA REPORT PATH:
/Users/arifpras/Library/CloudStorage/OneDrive-Kemenkeu/01_Kemenkeu/TK4_202601/marketupdate/Market Update 20260205x.pdf

REFERENCE DOCUMENT (with correct format on page 1):
/Users/arifpras/Library/CloudStorage/OneDrive-Kemenkeu/01_Kemenkeu/TK4_202601/marketupdate/Market Update 20260204.pdf

TASK:
Generate a summary following the DJPPR SBN Daily Market Update format. The summary must:

1. STRUCTURE - Include exactly three sections with 2-3 bullet points each:
   - Headlines Pasar SUN (Government Bonds)
   - Headlines Pasar SBSN (Islamic Bonds/Sukuk)
   - Headlines Pasar Internasional (International Markets)

2. HEADER FORMAT:
   DIREKTORAT JENDERAL PENGELOLAAN PEMBIAYAAN DAN RISIKO
   KEMENTERIAN KEUANGAN RI
   [Date in Indonesian: DD Bulan YYYY]
   SBN Daily Market Update

3. CONTENT REQUIREMENTS:
   - Start each section with market direction (menguat/melemah/mixed)
   - Include specific data: percentages (2 decimals), amounts (Rp with T for trillion)
   - Cite sources: BI settlement data, IBPA quotations, SI-BISSS, PLTE
   - Use temporal markers: ytd, mtd, specific dates
   - Include key market indicators: Rupiah/USD, IHSG, VIX, yields, CDS, spreads
   - Name officials with full titles when citing policy news

4. STYLE:
   - Language: Formal Indonesian (Bahasa Indonesia)
   - Format numbers: Indonesian notation (comma thousands, period decimal)
   - Use comparative language: dari...ke..., naik/turun, menguat/melemah
   - Professional tone: objective, data-driven, concise

5. OUTPUT:
   - Create a text file first
   - Convert to PDF using pandoc or quarto with these settings:
     * Margins: 2.5cm
     * Font: 11pt
     * Paper: A4 or Letter

Please extract the data, generate the summary, and save it as a separate PDF file named 
"[Original_Filename] - Summary.pdf"
```

### Simplified Version (If Context Already Learned)

If the AI already knows the DJPPR Market Update format from previous conversation:

```
Generate a summary for /Users/arifpras/Library/CloudStorage/OneDrive-Kemenkeu/01_Kemenkeu/TK4_202601/marketupdate/Market Update 20260205x.pdf following the learned DJPPR format. Extract data and create the summary as a separate PDF suitable for the first page of the report.
```

### Even Shorter (Same Session, Style Already Established)

```
based on those style, pattern, and structure; generate a summary for /Users/arifpras/Library/CloudStorage/OneDrive-Kemenkeu/01_Kemenkeu/TK4_202601/marketupdate/Market Update 20260205x.pdf; save in a different pdf page.
```

---

## Example Output

### Market Update Summary - February 5, 2026

Below is an actual example of a generated summary following the defined style, pattern, and structure:

```
DIREKTORAT JENDERAL PENGELOLAAN PEMBIAYAAN DAN RISIKO
KEMENTERIAN KEUANGAN RI

5 Februari 2026

SBN Daily Market Update

Headlines Pasar SUN
• Pasar SUN bergerak melemah. Berdasarkan kuotasi IBPA tanggal 5 Februari 
  2026 (endday), yield SUN seri benchmark bergerak naik 0,2 s.d. 4,1 bps 
  apabila dibandingkan hari kemarin. Nilai tukar Rupiah mengalami pelemahan, 
  di mana hari ini ditutup melemah sebesar 18,85 poin (0,23%) ke level 
  Rp16.782/US$. Indeks IHSG mengalami penurunan sebesar 18,85 poin (0,23%) 
  ke level 8.127,87. Telah dilaksanakan penerbitan SUN melalui lelang 
  perdana tanggal 3 Februari 2026 sebesar Rp36,0 T dengan setelmen tanggal 
  5 Februari 2026.

• Kepemilikan Non Residen atas SBN, berdasarkan data setelmen BI tanggal 
  4 Februari 2026, tercatat melakukan net buy sebesar Rp5,32 triliun secara 
  year to date (ytd). Transaksi rata-rata perdagangan harian bulan Februari 
  2026 (s.d. 4 Februari 2026) adalah sebesar Rp20,83 T (outright), 
  Rp28,64 T (repo non BI), dan Rp67,63 T (repo BI). Kepemilikan Individu 
  Residen atas SBN (Tradable dan Non Tradable) mencapai Rp660,47 T per 
  4 Februari 2026, dengan kepemilikan SBN Reguler sebesar Rp280,24 T dan 
  SBN Ritel sebesar Rp379,46 T.

Headlines Pasar SBSN
• Realisasi penerbitan SBN sampai dengan 5 Februari 2026 adalah sebesar 
  Rp233,94 T (13,58%) dengan realisasi SUN sebesar Rp176,50 T (14,11%) 
  dan SBSN Rp57,44 T (12,17%). Realisasi untuk SBN Jatuh Tempo (termasuk 
  cash management dan buyback) adalah sebesar Rp51,93 T (5,62%). Realisasi 
  SBN Neto adalah sebesar Rp182,01 T (22,76%) dari target UU APBN 2026 
  dengan defisit 2,68%.

• Pada bulan Februari 2026, diperkirakan terdapat penerbitan sebesar 
  Rp121,00 T dan SBN jatuh tempo sebesar Rp52,57 T. SBN neto pada Februari 
  2026 diperkirakan menjadi Rp219,76 T. Indeks CMP Pasar SBN pada 
  5 Februari 2026 berada di level 0,250 yang mengindikasikan kondisi pasar 
  dalam status "Normal" (0,250 < Indeks < 0,425).

Headlines Pasar Internasional
• Yield Global Bonds Indonesia (SUN Valas) bergerak turun pada hari Kamis 
  (5/2). Yield SUN Valas USD tenor 5Y, 10Y, 30Y, 50Y bergerak turun 
  masing-masing -1,3 bps, -0,6 bps, -0,4 bps, dan -0,6 bps. Yield US 
  Treasury pada penutupan perdagangan hari Rabu (4/2) bergerak mixed, 
  dengan yield untuk UST tenor 10Y naik 1,0 bps dan tenor 30Y naik 2,3 bps 
  dari hari sebelumnya. Credit risk Indonesia yang tercermin dari nilai CDS 
  bergerak naik pada penutupan hari Rabu (4/2), dengan CDS tenor 5 tahun 
  naik 0,46 bps dan tenor 10 tahun naik 0,61 bps.

• Spread dari yield global bonds Indonesia terhadap UST tenor 10Y dan 30Y 
  bergerak turun, tenor 10Y turun 2 bps (dari 83 bps ke 81 bps) dan tenor 
  30Y turun 5 bps (dari 84 bps ke 79 bps). Nilai NDF bergerak naik pada 
  hari Kamis (5/2) dibandingkan hari sebelumnya, dengan NDF tenor 1, 6, dan 
  12 bulan bergerak naik masing-masing 46, 45, dan 48 poin.

• Indeks saham utama global bergerak mixed pada sesi perdagangan hari Kamis, 
  05 Februari 2026. Di Asia, indeks Nikkei turun 0,88%, Hang Seng naik 
  0,14%, Shanghai turun 0,64%, dan KOSPI melemah signifikan sebesar 3,86%. 
  Di Amerika, DJIA menguat 0,53%, S&P 500 turun 0,51%, dan Nasdaq melemah 
  1,51%. Sementara itu di Eropa, FTSE naik 0,85%, CAC 40 naik 1,01%, dan 
  DAX turun 0,72%. Harga minyak mentah ICP pada 5 Februari 2026 tercatat 
  di level US$64,05 per barel, sementara minyak sawit berada di level 
  US$1.044,37 per metric ton.
```

**Key Observations in This Example:**

1. **Structure Compliance**: All three mandatory sections present (SUN, SBSN, Internasional) with 2-3 bullets each
2. **Numerical Precision**: All percentages show 2 decimals (0,23%, 13,58%, etc.)
3. **Source Attribution**: Properly cited (IBPA, BI settlement data, etc.)
4. **Temporal References**: Uses ytd, mtd, and specific dates throughout
5. **Comparative Language**: "dari...ke...", "naik/turun", "menguat/melemah"
6. **Market Direction**: Each section starts with clear direction statement
7. **Professional Tone**: Formal Indonesian with proper titles and terminology

---

## Quick Reference

### What You Need
1. **Data report PDF** - The full market update document
2. **Reference PDF** (optional) - An example with correct format on page 1
3. **AI assistant** - GitHub Copilot, ChatGPT, Claude, etc.

### What You Get
- Summary text file (Markdown or plain text)
- Summary PDF file suitable for first page insertion
- Follows exact DJPPR formatting standards

### For More Details
See the complete WORKFLOW_AUTOMATION.pdf for:
- Detailed style and pattern definitions
- Writing rules and conventions
- Data source references
- Troubleshooting guide

---

**Created:** 2026-02-06  
**Team:** Tim Kerja Pembangunan Sistem Automasi Pengelolaan Data SBN  
**Organization:** DJPPR, Kementerian Keuangan RI
