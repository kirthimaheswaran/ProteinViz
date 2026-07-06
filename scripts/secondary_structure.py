from Bio.PDB import PDBParser
from collections import Counter
import pandas as pd
import os

# Create parser
parser = PDBParser(QUIET=True)

# Load protein
structure = parser.get_structure("AChE", "data/proteins/4M0E.pdb")

secondary_structure = Counter()

for residue in structure.get_residues():

    # Skip non-standard residues
    if residue.id[0] != " ":
        continue

    # Placeholder classification
    # (We'll use DSSP later for accurate assignments.)
    if "CA" in residue:
        secondary_structure["Unknown"] += 1

# Create DataFrame
df = pd.DataFrame(
    secondary_structure.items(),
    columns=["Structure", "Count"]
)

print(df)

# Save results
os.makedirs("results", exist_ok=True)
df.to_csv("results/secondary_structure.csv", index=False)

print("\nResults saved to results/secondary_structure.csv")