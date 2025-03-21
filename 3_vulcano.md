# Basic Tutorial: Creating Volcano Plots in Python

## Introduction  
This guide provides a simple way to create a **volcano plot** using Python.
A volcano plot is commonly used in **gene expression analysis** to visualize statistical significance (p-values) versus fold change.  

You may have already seen some volcano plots. This tutorial will help you implement one step by step. 
The example data comes from an open-source tutorial.

---

## 1. Installing Required Libraries  
To follow this tutorial, you need to install the `bioinfokit` package.  

**If you are using Conda**, the tutorial suggests:  
```bash
conda install bioinfokit
```
However, if you are using `pip`, install it with:  
```bash
pip install bioinfokit
```

---

## 2. Downloading Example Data  
The tutorial uses a publicly available dataset. You can download it from GitHub:  

[Download testvolcano.csv](https://raw.githubusercontent.com/vappiah/bioinfoscripts/refs/heads/main/testvolcano.csv)  

Make sure to save it in your working directory.

---

## 3. Running the Volcano Plot Script  
Here is a Python script to generate the volcano plot:  

```python
import pandas as pd
from bioinfokit.analys import stat
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("testvolcano.csv")

# Perform the volcano plot
stat.volcano(df=df, lfc="log2FC", pv="p-value", 
             lfc_thr=1, pv_thr=0.05, show=True, 
             color=("#A9A9A9", "#1F77B4", "#D62728"))

# Save the plot
plt.savefig("volcano_plot.png", dpi=300)
```

---

## 4. Understanding the Parameters  
- `lfc="log2FC"` → Log2 Fold Change column  
- `pv="p-value"` → P-value column  
- `lfc_thr=1` → Threshold for fold change (log2 scale)  
- `pv_thr=0.05` → P-value threshold for significance  
- `color=("#A9A9A9", "#1F77B4", "#D62728")` → Colors for non-significant, upregulated, and downregulated points  

---

## 5. Expected Output  
After running the script, you should see a volcano plot where:  
- **Blue points** represent upregulated genes.  
- **Red points** represent downregulated genes.  
- **Gray points** are non-significant.  

---

## 6. Reference Tutorial  
This guide is based on a Japanese bioinformatics tutorial, which you can find here:  
🔗 [Pythonで作るVolcano plot #bioinformatics - Qiita](https://qiita.com/insilicomab/items/c382f10208e8bd2482b5)  

I tried it using **English translation**, and it worked well.  

---

## 7. Troubleshooting  
If you run into issues, double-check:  
- The correct installation of `bioinfokit` (`pip install bioinfokit`)  
- The downloaded `testvolcano.csv` file is in the correct directory  
- Your Python environment is set up properly  

Let me know if you have any trouble! 😊  
