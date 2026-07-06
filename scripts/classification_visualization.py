import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
df = pd.read_csv("results/amino_acid_classes.csv")

# Create figures folder
os.makedirs("figures", exist_ok=True)

# Create bar chart
plt.figure(figsize=(8, 5))

plt.bar(
    df["Class"],
    df["Count"],
    color=["steelblue", "orange", "green", "red", "purple"]
)

plt.title("Amino Acid Classification")
plt.xlabel("Class")
plt.ylabel("Number of Residues")

plt.tight_layout()

plt.savefig("figures/amino_acid_classes.png")

plt.show()

print("Figure saved to figures/amino_acid_classes.png")