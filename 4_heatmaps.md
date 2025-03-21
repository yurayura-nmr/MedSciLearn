# **Creating a Heatmap in Python**

Next, we’ll simulate gene expression data and visualize it using a heatmap. 
This is a great way to explore patterns in data, such as upregulated and downregulated genes in biological studies.

## **What is a Heatmap?**
A heatmap is a graphical representation of data where individual values are represented by colors. 
In biology, heatmaps are often used to visualize gene expression data, showing which genes are upregulated (more active)
or downregulated (less active) under different conditions.

## **Prerequisites**
As with the previous exercises, make sure you have the following Python libraries installed:

- **Pandas**: For handling data.
- **NumPy**: For numerical operations.
- **Seaborn**: For creating the heatmap.
- **Matplotlib**: For customizing and displaying the plot.

If you have not done so yet, you can install these libraries using pip:
```bash
pip install pandas numpy seaborn matplotlib
```

---

## **Step 1: Simulate Gene Expression Data**

We’ll start by simulating a dataset with:

- **20 upregulated genes** (higher expression in HFpEF).
- **20 downregulated genes** (lower expression in HFpEF).
- **4 samples** (2 CHOW and 2 HFpEF).

Here’s the code to simulate the data:

```python
import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Simulate upregulated genes (higher expression in HFpEF)
upregulated_data = np.random.uniform(low=7, high=10, size=(20, 4))  # 20 genes, 4 samples

# Simulate downregulated genes (lower expression in HFpEF)
downregulated_data = np.random.uniform(low=1, high=4, size=(20, 4))  # 20 genes, 4 samples

# Combine the data
simulated_data = np.vstack([upregulated_data, downregulated_data])

# Create gene names (e.g., Gene1, Gene2, ...)
gene_names = [f'Gene{i+1}' for i in range(40)]

# Create sample names (e.g., CHOW_Sample1, CHOW_Sample2, HFpEF_Sample1, HFpEF_Sample2)
sample_names = ['CHOW_Sample1', 'CHOW_Sample2', 'HFpEF_Sample1', 'HFpEF_Sample2']

# Create a DataFrame
data = pd.DataFrame(simulated_data, index=gene_names, columns=sample_names)

# Display the first few rows of the simulated data
print(data.head())
```

---

## **Step 2: Create the Heatmap**
Now that we have our simulated data, let’s create a heatmap using **Seaborn** and **Matplotlib**.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Set up the figure size
plt.figure(figsize=(10, 8))

# Create the heatmap
sns.heatmap(data, cmap='viridis', annot=True, fmt='.2f', linewidths=0.5)

# Add labels and title
plt.title('Simulated Heatmap of DEGs in HFpEF vs CHOW')
plt.xlabel('Samples')
plt.ylabel('Genes')

# Show the plot
plt.show()
```

---

## **Step 3: Customize the Heatmap**

You can customize the heatmap to make it more informative. For example:

- **Change the Colormap:** Use `cmap='coolwarm'` or `cmap='RdBu_r'` for a red-blue color scheme.
- **Add Clustering:** Use `sns.clustermap` to group similar genes and samples.

Here’s an example of a clustered heatmap:
```python
# Create a clustered heatmap
sns.clustermap(data, cmap='coolwarm', annot=True, fmt='.2f', linewidths=0.5)

# Add title
plt.title('Clustered Heatmap of DEGs in HFpEF vs CHOW')

# Show the plot
plt.show()
```

---

## **Step 4: Interpret the Heatmap**
- **Rows:** Represent genes (e.g., Gene1 to Gene40).
- **Columns:** Represent samples (e.g., CHOW_Sample1, HFpEF_Sample2).
- **Color Intensity:** Represents gene expression levels (higher values = brighter colors).

---

## **Next Steps**
1. **Experiment:** Try changing the colormap, adding clustering, or modifying the dataset.
2. **Real Data:** Once you’re comfortable, you can replace the simulated data with real gene expression data.
3. **Explore:** Learn more about Seaborn and Matplotlib to create other types of visualizations.

