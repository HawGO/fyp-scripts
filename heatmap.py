import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("resolved_segments_p_values.tsv", sep="\t", header=None)
data.columns = ['heatmap_col', 'heatmap_row', 'value']

row_order = data['heatmap_row'].unique()
col_order = data['heatmap_col'].unique()

data_aggregated = data.groupby(['heatmap_row', 'heatmap_col'], as_index=False).agg('sum')

heatmap_matrix = data_aggregated.pivot(index='heatmap_row', columns='heatmap_col', values='value')
heatmap_matrix = heatmap_matrix.reindex(row_order, axis=0)  # Reorder rows
heatmap_matrix = heatmap_matrix[col_order]  # Reorder columns

plt.figure(figsize=(10, 8))  # Adjust size if needed
sns.heatmap(heatmap_matrix, annot=False, cmap='Blues', cbar_kws={'label': 'Value'})

plt.title("Heatmap")
plt.xlabel("Heatmap Columns")
plt.ylabel("Heatmap Rows")
plt.show()
