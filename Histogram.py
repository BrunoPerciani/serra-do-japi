# Import libraries for data handling, visualization, and numerical operations.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load CSV files containing sampled pixel values for Serra do Japi and the urban area.
serra = pd.read_csv(r"Paste your path here")
urbano = pd.read_csv(r"Paste your path here")

# Reclassify raster values into interpretable vegetation change classes.
serra['Class'] = serra['VALUE'].replace({100000: 1, 200000: 2, 300000: 3})
urbano['Class'] = urbano['VALUE'].replace({100000: 1, 200000: 2, 300000: 3})

# Define class labels used in the plot legend.
labels = {1: 'Possible vegetation loss', 2: 'No significant change', 3: 'Possible vegetation gain'}

# Define colors associated with each vegetation change class.
colors = {1: '#E74C3C', 2: '#BDBDBD', 3: '#27AE60'}  # red, gray, green

# Compute percentage distribution of classes relative to the total number of pixels.
def perc(df):
    return df['Class'].value_counts(normalize=True).reindex([1,2,3], fill_value=0) * 100

# Calculate class percentages for Serra do Japi and the urban area.
serra_p = perc(serra)
urbano_p = perc(urbano)

# Define x-axis positions for the two comparison groups.
x = np.arange(2)  # Serra and Urban
bar_width = 0.25

# Define horizontal offsets to place class bars side by side.
offsets = [-bar_width, 0, bar_width]
classes = [1, 2, 3]

# Initialize the figure with a fixed size.
plt.figure(figsize=(8, 5))

# Plot grouped bars for each vegetation change class.
for i, c in enumerate(classes):
    plt.bar(x + offsets[i],
            [serra_p[c], urbano_p[c]],
            width=bar_width,
            color=colors[c],
            edgecolor='black',
            label=labels[c])

# Add percentage value labels above each bar.
for i, c in enumerate(classes):
    for j, val in enumerate([serra_p[c], urbano_p[c]]):
        plt.text(x[j] + offsets[i], val + 1,
                 f"{val:.1f}%", ha='center', fontsize=10)

# Set x-axis tick labels identifying the analyzed regions.
plt.xticks(x, ['Serra do Japi zone (A)', 'Urban portion of Jundiaí (B)'], fontsize=11)

# Set y-axis label, plot title, and legend configuration.
plt.ylabel("Percentage of Total Pixels (%)", fontsize=12)
plt.title("Vegetation Change by Region – Serra do Japi vs Urban Jundiaí (2013–2023)", fontsize=13, pad=10)
plt.legend(frameon=False, title="Class")

# Limit y-axis range to percentage scale.
plt.ylim(0, 100)
