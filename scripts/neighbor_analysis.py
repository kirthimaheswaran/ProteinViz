from Bio.PDB import PDBParser, NeighborSearch

# Create parser
parser = PDBParser(QUIET=True)

# Load protein
structure = parser.get_structure("AChE", "data/proteins/4M0E.pdb")

# Get all atoms
atoms = list(structure.get_atoms())

# Create NeighborSearch object
neighbor_search = NeighborSearch(atoms)

# Select the first alpha carbon (CA)
target_atom = None

for atom in atoms:
    if atom.get_name() == "CA":
        target_atom = atom
        break

# Find neighboring atoms within 5 Å
neighbors = neighbor_search.search(target_atom.coord, 5.0)

# Store unique residues
neighbor_residues = set()

for atom in neighbors:
    residue = atom.get_parent()

    # Skip non-standard residues
    if residue.id[0] != " ":
        continue

    neighbor_residues.add(residue)

print("=" * 45)
print("ProteinViz - Neighbor Analysis")
print("=" * 45)

print(f"Target Atom: {target_atom.get_full_id()}")
print(f"Neighboring Residues: {len(neighbor_residues)}\n")

print("Nearby Residues")
print("-" * 25)

for residue in sorted(neighbor_residues, key=lambda r: r.id[1]):
    print(f"{residue.resname} {residue.id[1]}")