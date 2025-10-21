import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

serra = pd.read_csv(r"C:\Users\bruno\OneDrive\VISUAL CODE STUDIO\IC.2025\Criação de histograma de análise de variação da vegetação\Sample_Serra_Do_Japi.csv")
urbano = pd.read_csv(r"C:\Users\bruno\OneDrive\VISUAL CODE STUDIO\IC.2025\Criação de histograma de análise de variação da vegetação\Sample_Urban_Area.csv")

serra['Class'] = serra['VALUE'].replace({100000: 1, 200000: 2, 300000: 3})
urbano['Class'] = urbano['VALUE'].replace({100000: 1, 200000: 2, 300000: 3})

labels = {1: 'Possible vegetation loss', 2: 'No significant change', 3: 'Possible vegetation gain'}
colors = {1: '#E74C3C', 2: '#BDBDBD', 3: '#27AE60'}  # vermelho, cinza, verde

def perc(df):
    return df['Class'].value_counts(normalize=True).reindex([1,2,3], fill_value=0) * 100

serra_p = perc(serra)
urbano_p = perc(urbano)

x = np.arange(2)  # 2 grupos: Serra e Urbano
bar_width = 0.25

offsets = [-bar_width, 0, bar_width]
classes = [1, 2, 3]

plt.figure(figsize=(8, 5))

for i, c in enumerate(classes):
    plt.bar(x + offsets[i],
            [serra_p[c], urbano_p[c]],
            width=bar_width,
            color=colors[c],
            edgecolor='black',
            label=labels[c])

for i, c in enumerate(classes):
    for j, val in enumerate([serra_p[c], urbano_p[c]]):
        plt.text(x[j] + offsets[i], val + 1,
                 f"{val:.1f}%", ha='center', fontsize=10)

plt.xticks(x, ['Serra do Japi zone (A)', 'Urban portion of Jundiaí (B)'], fontsize=11)
plt.ylabel("Percentage of Total Pixels (%)", fontsize=12)
plt.title("Vegetation Change by Region – Serra do Japi vs Urban Jundiaí (2013–2023)", fontsize=13, pad=10)
plt.legend(frameon=False, title="Class")
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig("comparativo_por_regiao.png", dpi=300)
plt.show()