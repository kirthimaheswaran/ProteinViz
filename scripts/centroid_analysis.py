from Bio.PDB import PDBParser
import numpy as np
import os

# Create parser
parser = PDBParser(QUIET=True)

# Load protein
structure = parser.get_structure("AChE", "data/proteins/4M0E.pdb")

coordinates = []

# Collect coordinates of all atoms
for atom in structure.get_atoms():
    coordinates.append(atom.coord)

# Convert to NumPy array
coordinates = np.array(coordinates)

# Calculate centroid
centroid = coordinates.mean(axis=0)

print("=" * 45)
print("ProteinViz - Centroid Analysis")
print("=" * 45)

print(f"X Coordinate : {centroid[0]:.2f}")
print(f"Y Coordinate : {centroid[1]:.2f}")
print(f"Z Coordinate : {centroid[2]:.2f}")

# Save report
os.makedirs("results", exist_ok=True)

with open("results/centroid_report.txt", "w") as file:
    file.write("Protein Centroid\n")
    file.write("=================\n\n")
    file.write(f"X: {centroid[0]:.2f}\n")
    file.write(f"Y: {centroid[1]:.2f}\n")
    file.write(f"Z: {centroid[2]:.2f}\n")

print("\nCentroid report saved to results/centroid_report.txt")