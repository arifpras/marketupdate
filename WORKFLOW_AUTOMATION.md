---
title: "Market Update Summary - Automated Production Workflow"
author: "Tim Kerja Pembangunan Sistem Automasi Pengelolaan Data SBN"
date: "2026-02-06"
format:
  pdf:
    documentclass: article
    geometry:
      - margin=2cm
    fontsize: 10pt
    linestretch: 1.15
    colorlinks: true
    code-block-font-size: \small
    toc: true
    toc-depth: 3
    number-sections: true
---

## Overview
This document outlines the automated workflow for generating Market Update summary reports following DJPPR Kemenkeu RI standards.

---

## Prerequisites

### Tools Required
- **pdftotext**: For extracting content from source PDFs
- **pandoc**: For converting text to PDF format
- **xelatex**: PDF engine for pandoc (or alternative: wkhtmltopdf, weasyprint)

### Installation (macOS)
```bash
# Install homebrew packages
brew install poppler  # provides pdftotext
brew install pandoc
brew install --cask mactex  # provides xelatex
```

---

## Detailed Style, Pattern, and Structure Definition

This section defines "those style, pattern, and structure" referenced in the production prompt.

### **DOCUMENT STRUCTURE**

#### Header Format (Required)
```
DIREKTORAT JENDERAL PENGELOLAAN PEMBIAYAAN DAN RISIKO
KEMENTERIAN KEUANGAN RI

[DD] [Bulan] [YYYY]

SBN Daily Market Update
```

**Example:**
```
5 Februari 2026
```

#### Three Main Sections (Required)
1. **Headlines Pasar SUN** (Government Bonds Market)
2. **Headlines Pasar SBSN** (Sukuk/Islamic Bonds Market)
3. **Headlines Pasar Internasional** (International Markets)

Each section must have **2-3 bullet points** (•)

---

### **SECTION 1: HEADLINES PASAR SUN**

#### Bullet 1: Market Direction + Key Drivers
**Pattern:**
```
• Pasar SUN bergerak [menguat/melemah/mixed]. [Policy/Political News with Names and Specifics]. 
Nilai tukar Rupiah [mengalami penguatan/pelemahan], di mana hari ini ditutup [naik/melemah] 
sebesar [X] poin ([X.XX]%) ke level Rp[X.XXX]/US$. [Additional market indicators: VIX, IHSG].
```

**Key Elements:**
- Start with clear market direction: "bergerak menguat" / "bergerak melemah" / "bergerak mixed"
- Include specific policy news with official names and percentages
- Rupiah movement: absolute points + percentage (2 decimals) + final level
- Additional indices: IHSG (Jakarta Composite), VIX when relevant
- Use "Menteri...", "Presiden...", "Gubernur..." for attribution

**Example:**
```
• Pasar SUN bergerak menguat. Menteri Koordinator Bidang Perekonomian Airlangga Hartarto 
menyampaikan bahwa proses negosiasi tarif antara Indonesia dan Amerika Serikat telah rampung 
dan saat ini memasuki tahap penyusunan dokumen hukum, dengan progres mencapai sekitar 90%. 
Nilai tukar Rupiah mengalami pelemahan, di mana hari ini ditutup melemah sebesar 15 poin (0,09%) 
ke level Rp16.775/US$. Sementara itu, indeks VIX mengalami penurunan ke level 17,94 dari level 18,00. 
IHSG naik 24,12 poin (0,30%) ke level 8.146,72.
```

#### Bullet 2: Ownership & Trading Data
**Pattern:**
```
• Kepemilikan Non Residen atas SBN, berdasarkan data setelmen BI tanggal [DD] [Bulan] [YYYY], 
[mengalami kenaikan/penurunan] sebesar Rp[X,XX] T ([X,XX]%) dari Rp[XXX,XX] T ke Rp[XXX,XX] T. 
Kepemilikan Non Residen [naik/turun] Rp[X,XX] T ([X,XX]%) secara year to date (ytd) dan 
[naik/turun] Rp[X,XX] T ([X,XX]%) secara month to date (mtd). Selanjutnya, berdasarkan data PLTE 
per tanggal [DD] [Bulan] [YYYY], perdagangan SBN tercatat sebesar Rp[XX,XX] triliun, dengan asing 
tercatat melakukan net [buy/sell] sebesar Rp[X,XX] triliun.
```

**Key Elements:**
- Always cite data source: "berdasarkan data setelmen BI tanggal..."
- Show changes with "dari...ke..." pattern
- Include YTD (year to date) and MTD (month to date) comparisons
- Reference PLTE (Platform Elektronik) data separately
- Specify foreign investor activity: "net buy" or "net sell"
- Use Indonesian number format: Rp with comma thousands separator

**Alternative Format (if individual ownership included):**
Add: "Kepemilikan Individu Residen atas SBN (Tradable dan Non Tradable) mencapai Rp[XXX,XX] T per [date]"

---

### **SECTION 2: HEADLINES PASAR SBSN**

#### Bullet 1: Yield Movements + Investor Activity
**Pattern:**
```
• Yield SBSN seri benchmark bergerak [turun/naik] dalam range [X] s.d. [X]. [PBS030], [PBS040], 
[PBS034], dan [PBS038], [X] bps, [X] bps, [X] bps, dan [X] bps. Secara month to date (mtd), 
[investor type] menjadi net buyer terbesar dengan total Rp[X,X] triliun. Sedangkan net sell 
terbesar (mtd) adalah [investor type] dengan total Rp[X,X] triliun. (data SI-BISSS per [DD] [Bulan] [YYYY]).
```

**Key Elements:**
- Specify benchmark series codes (PBS030, PBS040, PBS034, PBS038)
- Use "s.d." (sampai dengan / up to) for ranges
- Show exact bps (basis points) changes for each series
- Identify largest net buyers and sellers by type
- Always cite: "(data SI-BISSS per [date])"
- Investor types: Bank Konvensional, Non Residen, Asuransi, Dana Pensiun

**Alternative Format (Issuance Focus):**
```
• Realisasi penerbitan SBN sampai dengan [date] adalah sebesar Rp[XXX,XX] T ([XX,XX]%) dengan 
realisasi SUN sebesar Rp[XXX,XX] T ([XX,XX]%) dan SBSN Rp[XX,XX] T ([XX,XX]%). Realisasi untuk 
SBN Jatuh Tempo (termasuk cash management dan buyback) adalah sebesar Rp[XX,XX] T ([X,XX]%). 
Realisasi SBN Neto adalah sebesar Rp[XXX,XX] T ([XX,XX]%) dari target UU APBN [YYYY] dengan 
defisit [X,XX]%.
```

#### Bullet 2: Ownership or Projections
**Pattern A (Ownership):**
```
• Kepemilikan SBSN Domestik terbanyak dipegang oleh [investor type] dengan total Rp[XXX,XX] triliun. 
Sementara itu Investor Asing memegang SBSN Domestik sebesar Rp[XX,XX] triliun. (data SI-BISSS per 
[DD] [Bulan] [YYYY]). Data PLTE per [DD] [Bulan] [YYYY] pukul [HH.MM] WIB, volume transaksi 
perdagangan SBSN Domestik sebesar Rp[X,XX] triliun.
```

**Pattern B (Projections):**
```
• Pada bulan [Bulan] [YYYY], diperkirakan terdapat penerbitan sebesar Rp[XXX,XX] T dan SBN jatuh 
tempo sebesar Rp[XX,XX] T. SBN neto pada [Bulan] [YYYY] diperkirakan menjadi Rp[XXX,XX] T. Indeks 
CMP Pasar SBN pada [date] berada di level [X,XXX] yang mengindikasikan kondisi pasar dalam status 
"[Normal/Waspada/Siaga/Ditengarai Krisis]".
```

**Key Elements:**
- Include timestamp for PLTE data: "pukul 16.00 WIB"
- For projections, use "diperkirakan"
- CMP Index ranges: Normal (0.250-0.425), Waspada (0.425-0.600), Siaga (0.600-0.775), Krisis (0.775-1.000)

---

### **SECTION 3: HEADLINES PASAR INTERNASIONAL**

#### Bullet 1: US Policy + Commodities/Geopolitics
**Pattern:**
```
• [US Federal Reserve/Policy news with official names and positions]. [Geopolitical event with 
specific impact]. [Commodity price movement with specific figures].
```

**Key Elements:**
- Name specific Fed officials with titles: "Presiden Federal Reserve [City], [Name]"
- Include their specific statements/positions
- Link geopolitical events to market impacts (oil, bonds, etc.)
- Specify commodity movements: "WTI sebesar X,X% ke level US$XX,XX per barel"

**Example:**
```
• Pejabat Federal Reserve menyampaikan sinyal yang beragam terkait arah kebijakan moneter. 
Presiden Federal Reserve Richmond, Tom Barkin, menegaskan fokus bank sentral pada pencapaian 
target inflasi seiring penguatan pasar tenaga kerja. Ketegangan geopolitik kembali meningkat 
setelah Angkatan Laut AS menembak jatuh sebuah drone Iran di Laut Arab, yang mendorong kenaikan 
harga minyak mentah WTI sebesar 1,1% ke level US$63,88 per barel.
```

#### Bullet 2: Asian Markets
**Pattern:**
```
• Indeks saham utama Asia ditutup bergerak [mixed/menguat/melemah] pada sesi perdagangan hari 
[Day], [DD] [Bulan] [YYYY]. Indeks [Name] [melemah/menguat] [X,XX]%, [Name] [menguat/melemah] 
[X,XX]%, [Name] [naik/turun] [tipis] [X,XX]%, [Name] [menguat/melemah] [X,XX]%, dan [Name] 
[naik/turun] [X,XX]%. [Explanation of market drivers and reasons for movements].
```

**Key Elements:**
- List at least 5 major Asian indices: Nikkei, Topix, Hang Seng, KOSPI, CSI 300, Shanghai, STI
- Use varied verbs: melemah, menguat, naik, turun, naik tipis
- Always include explanatory sentence for market movements
- Reference sector impacts: "koreksi di sektor teknologi"

**Example:**
```
• Indeks saham utama Asia ditutup bergerak mixed pada sesi perdagangan hari Rabu, 04 Februari 2026. 
Indeks Nikkei melemah 0,78%, Topix menguat 0,27%, Hang Seng naik tipis 0,05%, KOSPI menguat 1,57%, 
dan CSI 300 naik 0,83%. Pelemahan di sejumlah bursa utama mengikuti pergerakan pasar saham AS yang 
tertekan oleh koreksi di sektor teknologi.
```

#### Bullet 3: European Markets + Economic Data
**Pattern:**
```
• Indeks saham kawasan Eropa [dibuka/ditutup] bergerak [mixed/menguat/melemah] pada sesi 
perdagangan hari [Day], [DD] [Bulan] [YYYY]. Indeks [Name] [melemah/menguat] [X,XX]%, [Name] 
[menguat/melemah] [X,XX]%, [Name] [turun/naik] [X,XX]%, dan [Name] [naik/turun] [X,XX]%. 
Data ekonomi menunjukkan [economic indicator] [melandai/naik/turun] ke level [X,XX]% pada [month] 
dari sebelumnya [X,XX]% pada bulan [month]. [Additional economic commentary with specific data].
```

**Key Elements:**
- List major European indices: Stoxx Europe 600, CAC 40, DAX, FTSE 100
- Include economic data releases: inflation, PMI, GDP
- Specify previous vs current figures with "dari sebelumnya...pada bulan..."
- Add country-specific details: UK, Germany, France

**Alternative: Indonesia Global Bonds**
```
• Yield Global Bonds Indonesia (SUN Valas) bergerak [turun/naik] pada hari [Day] ([D/M]). Yield 
SUN Valas USD tenor 5Y, 10Y, 30Y, 50Y bergerak [turun/naik] masing-masing [X,X], [X,X], [X,X], 
[X,X] bps. Yield US Treasury pada penutupan perdagangan hari [Day] ([D/M]) bergerak [mixed/naik/turun]. 
Yield khusus untuk UST tenor 10Y [naik/turun] [X,X] bps dan tenor 30Y [naik/turun] [X,X] bps dari 
hari sebelumnya. Credit risk Indonesia yang tercermin dari nilai CDS bergerak [naik/turun] pada 
penutupan hari [Day] ([D/M]), dengan CDS tenor 5 tahun [naik/turun] [X,XX] bps dan tenor 10 tahun 
[naik/turun] [X,XX] bps.
```

---

### **WRITING STYLE RULES**

#### 1. Numerical Precision
- **Percentages:** Always 2 decimal places: `0.09%`, `1.57%`, `22.76%`
- **Amounts (Rupiah):** Use T for trillion, with 2 decimals: `Rp2,61 T`, `Rp882,03 T`
- **Exchange Rate:** Format as `Rp16.775/US$` (with period as thousands separator)
- **Basis Points:** Integer or 1 decimal: `2 bps`, `-1.5 bps`, `-6.7 s.d. -2.1 bps`
- **Index Points:** 2 decimals: `24,12 poin`, `18,85 poin`
- **Index Levels:** 2 decimals with comma: `8.146,72`, `17,94`

#### 2. Temporal References
- **Always include:** Date stamps for all data sources
- **Use:** ytd (year to date), mtd (month to date)
- **Format dates:** `tanggal 4 Februari 2026`, `per 3 Februari 2026`, `pada hari Rabu, 04 Februari 2026`
- **Comparative:** "hari ini", "hari kemarin", "hari sebelumnya"

#### 3. Source Attribution (CRITICAL)
Must cite data sources explicitly:
- `berdasarkan data setelmen BI tanggal [date]`
- `berdasarkan kuotasi IBPA tanggal [date] (endday)`
- `berdasarkan data PLTE per tanggal [date]`
- `(data SI-BISSS per [date])`
- `pada penutupan perdagangan hari [day] ([date])`

#### 4. Comparative Language
- **Direction:** menguat/melemah (strengthen/weaken), naik/turun (rise/fall)
- **Transitions:** "dari...ke..." (from...to), "sebesar...ke level..." (by...to level...)
- **Ranges:** "dalam range X s.d. Y" (in range X to Y)
- **Intensity:** "naik tipis" (rose slightly), "melemah signifikan" (weakened significantly)

#### 5. Market Direction Opening
ALWAYS start each section's first bullet with:
- `Pasar SUN bergerak [menguat/melemah/mixed].`
- `Yield SBSN seri benchmark bergerak [turun/naik] dalam range...`
- `Yield Global Bonds Indonesia (SUN Valas) bergerak [turun/naik]...`
- `Indeks saham utama [region] ditutup bergerak [mixed/menguat/melemah]...`

#### 6. Causality Chains
Link events to outcomes explicitly:
- "...yang mendorong kenaikan..." (which drove the increase...)
- "...seiring..." (amid/alongside...)
- "...mengikuti..." (following...)
- "...meskipun..." (despite...)
- "...didorong oleh..." (driven by...)

#### 7. Professional Titles
Always include full titles:
- `Menteri Koordinator Bidang Perekonomian [Name]`
- `Presiden Federal Reserve [City], [Name]`
- `Gubernur Federal Reserve [Name]`
- `Perdana Menteri [Name]`

#### 8. Parenthetical Usage
- Percentages after absolute values: `naik Rp3,37 T (0,38%)`
- Abbreviations first use: `year to date (ytd)`
- Date shortcuts: `hari Rabu (4/2)`, `pada Januari (1/26)`
- Alternative forms: `SBN Jatuh Tempo (termasuk cash management dan buyback)`

---

### **DATA SOURCES REFERENCE**

| Abbreviation | Full Name | Usage |
|--------------|-----------|--------|
| BI | Bank Indonesia | Settlement data, exchange rates |
| IBPA | Indonesian Bond Pricing Agency | Yield quotations |
| PLTE | Platform Lelang Elektronik | Trading volume data |
| SI-BISSS | Sistem Informasi BISSS | SBSN ownership/trading |
| UST | US Treasury | US government bonds |
| CDS | Credit Default Swap | Credit risk indicator |
| NDF | Non-Deliverable Forward | Forward FX rate |
| VIX | Volatility Index | Market volatility |
| WTI | West Texas Intermediate | Oil benchmark |
| ICP | Indonesian Crude Price | Indonesia oil benchmark |

---

### **FORMATTING SPECIFICATIONS**

#### Language
- **Primary:** Indonesian (Bahasa Indonesia)
- **Numbers:** Indonesian format (comma as thousands separator, period as decimal)
- **Dates:** Indonesian format (DD Bulan YYYY)

#### Tone
- **Formal:** Official government document style
- **Objective:** Factual reporting, no opinions
- **Concise:** Dense information, minimal filler
- **Technical:** Uses market terminology appropriately

#### Document Properties (for PDF conversion)
```
Font: 11pt
Margins: 2.5cm all sides
Line spacing: Single or 1.15
Alignment: Justified
Bullet style: • (filled circle)
```

---

## Workflow Steps

### Step 1: Analyze Reference Document (One-Time Setup)

**Purpose**: Learn the style, pattern, and structure from an existing report

**Prompt**:
```
observe this: [PATH_TO_REFERENCE_PDF]
```

**Example**:
```
observe this: /Users/arifpras/Library/CloudStorage/OneDrive-Kemenkeu/01_Kemenkeu/TK4_202601/marketupdate/Market Update 20260204.pdf
```

**Expected Output**: AI will extract and display the PDF content

---

### Step 2: Learn Style and Structure (One-Time Setup)

**Purpose**: Capture the writing patterns, structure, and formatting rules

**Prompt**:
```
learn the style and pattern to produce the summary on page 1 of the report.
```

**Expected Output**: AI will analyze and document:
- Document structure (header, sections, subsections)
- Writing style patterns (precision, attribution, temporal references)
- Data presentation format (percentages, ranges, comparative language)
- Section requirements (Headlines Pasar SUN, SBSN, Internasional)

**Key Patterns to Confirm**:
- ✓ Three main headline sections
- ✓ Bullet points with market direction statements
- ✓ Precise figures with 2-decimal percentages
- ✓ Source attributions (BI, IBPA, SI-BISSS, PLTE)
- ✓ Temporal markers (ytd, mtd, specific dates)
- ✓ Comparative language (naik/turun, menguat/melemah)

---

### Step 3: Generate Summary for New Report

**Purpose**: Create a summary for a new market update following the learned style

**Prompt Template**:
```
based on those style, pattern, and structure; generate a summary for [PATH_TO_NEW_PDF]; save in a different pdf page.
```

**Example**:
```
based on those style, pattern, and structure; generate a summary for /Users/arifpras/Library/CloudStorage/OneDrive-Kemenkeu/01_Kemenkeu/TK4_202601/marketupdate/Market Update 20260205x.pdf; save in a different pdf page.
```

**Expected Output**: 
- AI will extract data from the new PDF
- Generate summary following learned structure
- Create text file with formatted content
- Convert to PDF using pandoc

---

## Automation Script (Optional)

For full automation, create a bash script:

```bash
#!/bin/bash
# market_summary_generator.sh

# Variables
SOURCE_PDF="$1"
OUTPUT_DIR="$(dirname "$SOURCE_PDF")"
BASE_NAME="$(basename "$SOURCE_PDF" .pdf)"
OUTPUT_FILE="${OUTPUT_DIR}/${BASE_NAME} - Summary.pdf"

# Step 1: Extract content (for verification)
echo "Extracting content from: $SOURCE_PDF"
pdftotext "$SOURCE_PDF" "${OUTPUT_DIR}/temp_extract.txt"

# Step 2: Use AI to generate summary
echo "Please use AI with this prompt:"
echo "based on the learned style and structure, generate a summary for $SOURCE_PDF; save in a different pdf page."

# Note: This requires AI interaction - can be integrated with API if available
```

---

## Quality Control Checklist

After generating each summary, verify:

### Content Requirements
- [ ] Header includes: DJPPR name, Kemenkeu RI, date, title
- [ ] Three main sections: Headlines Pasar SUN, SBSN, Internasional
- [ ] Each section has 2-3 bullet points

### Data Quality
- [ ] All percentages show 2 decimal places
- [ ] Amounts use Indonesian notation (Rp, T for trillion)
- [ ] Dates are consistent and accurate
- [ ] Source attributions included (BI, IBPA, etc.)

### Language Style
- [ ] Uses Indonesian language
- [ ] Formal/professional tone
- [ ] Market direction clearly stated (menguat/melemah)
- [ ] Comparative language used (dari...ke...)
- [ ] Temporal references included (ytd, mtd)

### Formatting
- [ ] PDF margins appropriate (2.5cm)
- [ ] Font size readable (11pt)
- [ ] Proper paragraph spacing
- [ ] Bullet points properly formatted

---

## Troubleshooting

### Issue: PDF extraction shows garbled text
**Solution**: 
```bash
# Try different encoding
pdftotext -enc UTF-8 "source.pdf" output.txt

# Or use layout preservation
pdftotext -layout "source.pdf" output.txt
```

### Issue: Pandoc conversion fails
**Solution**:
```bash
# Check if xelatex is installed
which xelatex

# Try alternative PDF engine
pandoc input.txt -o output.pdf --pdf-engine=wkhtmltopdf

# Or use basic conversion
pandoc input.txt -o output.pdf
```

### Issue: Missing data in summary
**Solution**: 
- Manually verify source PDF has required sections
- Adjust extraction command to get more content
- Use specific page ranges: `pdftotext -f 1 -l 2 source.pdf -`

---

## File Naming Convention

Follow this pattern for consistency:

```
Market Update YYYYMMDD - Summary.pdf
```

Examples:
- `Market Update 20260205 - Summary.pdf`
- `Market Update 20260206 - Summary.pdf`

---

## Advanced: API Integration

For fully automated workflow with AI API:

```python
#!/usr/bin/env python3
# auto_market_summary.py

import subprocess
import openai  # or other AI API
from pathlib import Path

def generate_summary(source_pdf_path):
    # Extract PDF content
    result = subprocess.run(
        ['pdftotext', source_pdf_path, '-'],
        capture_output=True, text=True
    )
    pdf_content = result.stdout
    
    # Call AI API with learned prompt
    prompt = f"""based on the learned style and structure for DJPPR Market Updates, 
    generate a summary for this content:
    
    {pdf_content}
    
    Follow the three-section format: Headlines Pasar SUN, SBSN, and Internasional."""
    
    # API call (pseudo-code)
    summary = ai_api.generate(prompt)
    
    # Save and convert to PDF
    output_path = Path(source_pdf_path).parent / f"{Path(source_pdf_path).stem} - Summary.txt"
    output_path.write_text(summary)
    
    # Convert to PDF
    subprocess.run([
        'pandoc', str(output_path), 
        '-o', str(output_path).replace('.txt', '.pdf'),
        '--pdf-engine=xelatex',
        '-V', 'geometry:margin=2.5cm',
        '-V', 'fontsize=11pt'
    ])
    
    return output_path

if __name__ == "__main__":
    import sys
    source_pdf = sys.argv[1]
    generate_summary(source_pdf)
```

---

## Summary of Prompts

### One-Time Learning Phase
1. **Observe reference**: `observe this: [reference_pdf_path]`
2. **Learn style**: `learn the style and pattern to produce the summary on page 1 of the report.`

### Production Phase (Repeat for each new report)
3. **Generate summary**: `based on those style, pattern, and structure; generate a summary for [new_pdf_path]; save in a different pdf page.`

---

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

## Version History

- **v1.0** (2026-02-06): Initial workflow documentation
- Created by: Arif P. Sulistiono (github.com/arifpras)
- Based on: Market Update 20260204.pdf structure

---

## Contact

For questions or improvements to this workflow:
- Tim Kerja Pembangunan Sistem Automasi Pengelolaan Data SBN: DJPPR, Kemenkeu RI
- Location: Ged. Frans Seda, Jl. Wahidin Raya No. 1, Jakarta

---

## Appendix: Example Output

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

1. **Structure Compliance**: All three mandatory sections present (SUN, SBSN, 
   Internasional) with 2-3 bullets each
2. **Numerical Precision**: All percentages show 2 decimals (0,23%, 13,58%, etc.)
3. **Source Attribution**: Properly cited (IBPA, BI settlement data, etc.)
4. **Temporal References**: Uses ytd, mtd, and specific dates throughout
5. **Comparative Language**: "dari...ke...", "naik/turun", "menguat/melemah"
6. **Market Direction**: Each section starts with clear direction statement
7. **Professional Tone**: Formal Indonesian with proper titles and terminology
