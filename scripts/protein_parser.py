from Bio.PDB import PDBParser
from collections import Counter
import pandas as pd
import os

# Create parser
parser = PDBParser(QUIET=True)

# Load protein
structure = parser.get_structure("AChE", "data/proteins/4M0E.pdb")

print("=" * 40)
print("ProteinViz")
print("=" * 40)

# Count amino acids
amino_acids = []

for residue in structure.get_residues():
    # Ignore water molecules and other non-standard residues
    if residue.id[0] == " ":
        amino_acids.append(residue.resname)

# Count frequencies
aa_counts = Counter(amino_acids)

# Convert to DataFrame
df = pd.DataFrame(
    aa_counts.items(),
    columns=["Amino Acid", "Count"]
)

# Sort by count
df = df.sort_values(by="Count", ascending=False)

# Display results
print("\nAmino Acid Composition\n")
print(df)

# Create results folder if it doesn't exist
os.makedirs("results", exist_ok=True)

# Save CSV
df.to_csv("results/amino_acid_composition.csv", index=False)

print("\nResults saved to:")
print("results/amino_acid_composition.csv")