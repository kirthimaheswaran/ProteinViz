import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
df = pd.read_csv("results/chain_summary.csv")

# Create figure
plt.figure(figsize=(6, 5))
plt.bar(df["Chain"], df["Residues"], color="darkorange")

plt.title("Residues per Protein Chain")
plt.xlabel("Chain")
plt.ylabel("Number of Residues")

plt.tight_layout()

# Save
os.makedirs("figures", exist_ok=True)
plt.savefig("figures/chain_summary.png")

plt.show()

print("Figure saved to figures/chain_summary.png")