import pandas as pd
import matplotlib.pyplot as plt



df = pd.DataFrame({
    "Planeta": ["Mercúrio", "Vênus", "Terra", "Marte",
                "Júpiter", "Saturno", "Urano", "Netuno"],
    "Diametro_km": [4879, 12104, 12742, 6779,
                     139820, 116460, 50724, 49244],
    "Luas": [0, 0, 1, 2, 95, 146, 27, 14]
})

print("BASE DE DADOS")
print(df)



freq_luas = df["Luas"].value_counts().sort_index()

print("\nTABELA DE FREQUÊNCIA - LUAS")
print(freq_luas)



classes = pd.cut(df["Diametro_km"], bins=5)

freq_diametro = classes.value_counts().sort_index()

print("\nTABELA DE FREQUÊNCIA - DIÂMETRO")
print(freq_diametro)



plt.figure(figsize=(10,5))

plt.bar(
    df["Planeta"],
    df["Diametro_km"]
)

plt.title("Diâmetro dos Planetas")
plt.xlabel("Planeta")
plt.ylabel("Diâmetro (km)")

plt.show()



plt.figure(figsize=(10,5))

plt.hist(
    df["Diametro_km"],
    bins=5,
    edgecolor="black"
)

plt.title("Distribuição dos Diâmetros")
plt.xlabel("Diâmetro (km)")
plt.ylabel("Frequência")

plt.show()



coluna = df["Diametro_km"]

print("\n===== ESTATÍSTICA DESCRITIVA =====")

print("Média:", coluna.mean())
print("Mediana:", coluna.median())
print("Moda:", coluna.mode()[0])

print("Máximo:", coluna.max())
print("Mínimo:", coluna.min())

print("Amplitude:", coluna.max() - coluna.min())

print("Variância:", coluna.var())
print("Desvio Padrão:", coluna.std())

print("Q1:", coluna.quantile(0.25))
print("Q2:", coluna.quantile(0.50))
print("Q3:", coluna.quantile(0.75))