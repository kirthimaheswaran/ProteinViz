from Bio.PDB import PDBParser
from collections import Counter
import os

# Create parser
parser = PDBParser(QUIET=True)

# Load protein
structure = parser.get_structure("AChE", "data/proteins/4M0E.pdb")

# Basic counts
models = len(list(structure.get_models()))
chains = list(structure.get_chains())
residues = [
    residue for residue in structure.get_residues()
    if residue.id[0] == " "
]
atoms = list(structure.get_atoms())

# Amino acid composition
amino_acids = [residue.resname for residue in residues]
aa_counts = Counter(amino_acids)

most_common = aa_counts.most_common(1)[0]

# Create report
report = f"""
========================================
ProteinViz Protein Summary
========================================

Protein ID          : {structure.id}

Number of Models    : {models}
Number of Chains    : {len(chains)}
Protein Residues    : {len(residues)}
Number of Atoms     : {len(atoms)}

Most Common Amino Acid
-----------------------
{most_common[0]} ({most_common[1]} residues)

Chain IDs
---------
"""

for chain in chains:
    report += f"{chain.id}\n"

report += "\nAmino Acid Composition\n"
report += "----------------------\n"

for aa, count in aa_counts.most_common():
    report += f"{aa:<5} : {count}\n"

# Save report
os.makedirs("results", exist_ok=True)

with open("results/protein_summary.txt", "w") as file:
    file.write(report)

print(report)
print("\nProtein summary saved to results/protein_summary.txt")