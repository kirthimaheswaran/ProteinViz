from Bio.PDB import PDBParser

# Create parser
parser = PDBParser(QUIET=True)

# Load protein
structure = parser.get_structure("AChE", "data/proteins/4M0E.pdb")

largest_chain = None
largest_count = 0

for chain in structure.get_chains():

    residue_count = sum(
        1 for residue in chain
        if residue.id[0] == " "
    )

    if residue_count > largest_count:
        largest_count = residue_count
        largest_chain = chain.id

print("=" * 45)
print("ProteinViz - Largest Chain")
print("=" * 45)

print(f"Largest Chain : {largest_chain}")
print(f"Residues      : {largest_count}")