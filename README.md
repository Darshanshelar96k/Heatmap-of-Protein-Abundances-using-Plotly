# Heatmap-of-Protein-Abundances-using-Plotly
This Python script generates an interactive heatmap for visualizing protein abundance data from an Excel file. The heatmap, created using Plotly, displays raw abundance values across different conditions. It's designed to handle large datasets efficiently, offering a zoomable and hoverable interface for data exploration.

This script generates an interactive heatmap for protein abundance data from an Excel file using Plotly.

---

## Requirements
- Python 3.x  
- Pandas  
- Plotly  
- Openpyxl  

Install dependencies using:  
```bash
pip install pandas plotly openpyxl
```

---

## Input Format
- Excel file with:
  - First column: Protein identifiers (e.g., Accession IDs)  
  - First row: Condition labels  
  - Numeric values (e.g., `2,180,000`)  

---

## How to Run
1. Place your Excel file in the project folder.  
2. Run the script using:  
```bash
python heatmap_plotly.py <path_to_excel_file>
```
Example:
```bash
python heatmap_plotly.py protein_data.xlsx
```

3. The interactive heatmap will open in your browser.

---

## Example
```bash
python heatmap_plotly.py ./data/protein_abundance.xlsx
```


---

## Author
**Darshan Shelar**  
