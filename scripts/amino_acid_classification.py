from Bio.PDB import PDBParser
from collections import Counter
import pandas as pd
import os

# Create parser
parser = PDBParser(QUIET=True)

# Load protein structure
structure = parser.get_structure("AChE", "data/proteins/4M0E.pdb")

# Amino acid classifications
hydrophobic = ["ALA", "VAL", "LEU", "ILE", "MET", "PHE", "TRP", "PRO"]
polar = ["SER", "THR", "ASN", "GLN", "TYR", "CYS"]
positive = ["LYS", "ARG", "HIS"]
negative = ["ASP", "GLU"]
special = ["GLY"]

# Count amino acid classes
class_counts = Counter()

for residue in structure.get_residues():

    # Skip non-standard residues
    if residue.id[0] != " ":
        continue

    aa = residue.resname

    if aa in hydrophobic:
        class_counts["Hydrophobic"] += 1

    elif aa in polar:
        class_counts["Polar"] += 1

    elif aa in positive:
        class_counts["Positive"] += 1

    elif aa in negative:
        class_counts["Negative"] += 1

    elif aa in special:
        class_counts["Special"] += 1

# Convert to DataFrame
df = pd.DataFrame(
    class_counts.items(),
    columns=["Class", "Count"]
)

# Sort by count
df = df.sort_values(by="Count", ascending=False)

# Display results
print("=" * 40)
print("ProteinViz - Amino Acid Classification")
print("=" * 40)
print(df)

# Create results folder if it doesn't exist
os.makedirs("results", exist_ok=True)

# Save CSV
df.to_csv("results/amino_acid_classes.csv", index=False)

print("\nResults saved to results/amino_acid_classes.csv")