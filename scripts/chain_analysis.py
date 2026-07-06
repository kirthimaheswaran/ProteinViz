from Bio.PDB import PDBParser
import pandas as pd
import os

# Create parser
parser = PDBParser(QUIET=True)

# Load protein
structure = parser.get_structure("AChE", "data/proteins/4M0E.pdb")

chain_data = []

print("=" * 50)
print("ProteinViz - Chain Analysis")
print("=" * 50)

for chain in structure.get_chains():

    residue_count = 0

    print(f"\nChain {chain.id}")
    print("-" * 20)

    for residue in chain:
        print(residue.resname, residue.id)

        # Count only standard amino acids
        if residue.id[0] == " ":
            residue_count += 1

    chain_data.append({
        "Chain": chain.id,
        "Residues": residue_count
    })

# Convert to DataFrame
df = pd.DataFrame(chain_data)

print("\nSummary")
print(df)

# Save results
os.makedirs("results", exist_ok=True)
df.to_csv("results/chain_summary.csv", index=False)

print("\nChain summary saved to results/chain_summary.csv")