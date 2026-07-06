import pandas as pd
import matplotlib.pyplot as plt
import os

# Load amino acid composition
df = pd.read_csv("results/amino_acid_composition.csv")

# Create figures folder if it doesn't exist
os.makedirs("figures", exist_ok=True)

# Create bar chart
plt.figure(figsize=(12, 6))
plt.bar(df["Amino Acid"], df["Count"], color="steelblue")

plt.title("Amino Acid Composition of AChE")
plt.xlabel("Amino Acid")
plt.ylabel("Count")
plt.xticks(rotation=45)

plt.tight_layout()

# Save figure
plt.savefig("figures/amino_acid_composition.png")

plt.show()

print("Figure saved to figures/amino_acid_composition.png")