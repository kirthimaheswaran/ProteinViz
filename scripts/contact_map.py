from Bio.PDB import PDBParser
import numpy as np
import matplotlib.pyplot as plt
import os

# Create parser
parser = PDBParser(QUIET=True)

# Load protein
structure = parser.get_structure("AChE", "data/proteins/4M0E.pdb")

# Store CA atoms
ca_atoms = []

for residue in structure.get_residues():

    # Skip non-standard residues
    if residue.id[0] != " ":
        continue

    # Store only alpha carbon atoms
    if "CA" in residue:
        ca_atoms.append(residue["CA"])

n = len(ca_atoms)

# Create contact matrix
contact_map = np.zeros((n, n))

# Distance threshold (Å)
threshold = 8.0

# Calculate contacts
for i in range(n):
    for j in range(n):

        distance = ca_atoms[i] - ca_atoms[j]

        if distance <= threshold:
            contact_map[i, j] = 1

# Create figures folder
os.makedirs("figures", exist_ok=True)

# Plot contact map
plt.figure(figsize=(8, 8))

plt.imshow(contact_map, cmap="Blues", origin="lower")

plt.title("Residue Contact Map")
plt.xlabel("Residue Index")
plt.ylabel("Residue Index")

plt.colorbar(label="Contact")

plt.tight_layout()

plt.savefig("figures/contact_map.png")

plt.show()

print("Contact map saved to figures/contact_map.png")