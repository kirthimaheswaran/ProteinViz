from Bio.PDB import PDBParser
from collections import Counter
import pandas as pd
import os

# Create parser
parser = PDBParser(QUIET=True)

# Load protein
structure = parser.get_structure("AChE", "data/proteins/4M0E.pdb")

# Count amino acids
aa_counts = Counter()

for residue in structure.get_residues():

    # Skip non-standard residues
    if residue.id[0] != " ":
        continue

    aa = residue.resname
    aa_counts[aa] += 1

# Total residues
total_residues = sum(aa_counts.values())

# Create DataFrame
df = pd.DataFrame(
    aa_counts.items(),
    columns=["Amino Acid", "Count"]
)

# Calculate percentage
df["Percentage"] = (df["Count"] / total_residues) * 100

# Round percentage
df["Percentage"] = df["Percentage"].round(2)

# Sort by count
df = df.sort_values(by="Count", ascending=False)

# Display results
print("=" * 45)
print("ProteinViz - Amino Acid Percentage")
print("=" * 45)
print(df)

# Create results folder
os.makedirs("results", exist_ok=True)

# Save CSV
df.to_csv("results/amino_acid_percentage.csv", index=False)

print("\nResults saved to results/amino_acid_percentage.csv")