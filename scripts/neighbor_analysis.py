from Bio.PDB import PDBParser, NeighborSearch

# Create parser
parser = PDBParser(QUIET=True)

# Load protein
structure = parser.get_structure("AChE", "data/proteins/4M0E.pdb")

# Get all atoms
atoms = list(structure.get_atoms())

# Create neighbor search object
neighbor_search = NeighborSearch(atoms)

# Select the first alpha carbon (CA)
target_atom = None

for atom in atoms:
    if atom.get_name() == "CA":
        target_atom = atom
        break

# Find neighboring atoms within 5 Å
neighbors = neighbor_search.search(target_atom.coord, 5.0)

print("=" * 45)
print("ProteinViz - Neighbor Analysis")
print("=" * 45)

print(f"Target Atom : {target_atom.get_full_id()}")
print(f"Neighbors within 5 Å : {len(neighbors)}")