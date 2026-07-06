from Bio.PDB import PDBParser
import numpy as np
import os

# Create parser
parser = PDBParser(QUIET=True)

# Load protein
structure = parser.get_structure("AChE", "data/proteins/4M0E.pdb")

# Get all atom coordinates
coordinates = np.array([atom.coord for atom in structure.get_atoms()])

max_distance = 0

# Compare every pair of atoms
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        distance = np.linalg.norm(coordinates[i] - coordinates[j])

        if distance > max_distance:
            max_distance = distance

print("=" * 45)
print("ProteinViz - Protein Size Analysis")
print("=" * 45)

print(f"Maximum Distance: {max_distance:.2f} Å")

# Save report
os.makedirs("results", exist_ok=True)

with open("results/protein_size.txt", "w") as file:
    file.write("Protein Size Analysis\n")
    file.write("=====================\n\n")
    file.write(f"Maximum Distance: {max_distance:.2f} Å\n")

print("\nReport saved to results/protein_size.txt")