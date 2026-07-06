from Bio.PDB import PDBParser

# Average molecular weights (Da) of amino acid residues
aa_weights = {
    "ALA": 89.09, "ARG": 174.20, "ASN": 132.12,
    "ASP": 133.10, "CYS": 121.16, "GLN": 146.15,
    "GLU": 147.13, "GLY": 75.07, "HIS": 155.16,
    "ILE": 131.18, "LEU": 131.18, "LYS": 146.19,
    "MET": 149.21, "PHE": 165.19, "PRO": 115.13,
    "SER": 105.09, "THR": 119.12, "TRP": 204.23,
    "TYR": 181.19, "VAL": 117.15
}

# Create parser
parser = PDBParser(QUIET=True)

# Load protein
structure = parser.get_structure("AChE", "data/proteins/4M0E.pdb")

total_weight = 0

for residue in structure.get_residues():

    # Skip non-standard residues
    if residue.id[0] != " ":
        continue

    aa = residue.resname

    if aa in aa_weights:
        total_weight += aa_weights[aa]

print("=" * 45)
print("ProteinViz - Molecular Weight")
print("=" * 45)

print(f"Estimated Molecular Weight: {total_weight:.2f} Da")
print(f"Estimated Molecular Weight: {total_weight/1000:.2f} kDa")