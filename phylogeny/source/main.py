import Bio
import argparse
from pathlib import Path
from Bio import AlignIO, Phylo
from alignment import align_sequences
from treemaker import build_dendrogram

def main():
	parser = argparse.ArgumentParser( description = "Align sequences and construct a dendrogram")
	parser.add_argument("input", help = "Input FASTA file")
	parser.add_argument("-o", "--output-dir", default = "results", help = "Output FASTA file")

	args = parser.parse_args()

	input_file = Path(args.input)
	output_dir = Path(args.output_dir)
	output_dir.mkdir(parents = True, exist_ok = True)

	#outputs
	aligned_file = output_dir / f"{input_file.stem}_aligned.fasta"
	tree_file = output_dir / f"{input_file.stem}_tree.nwk"

	#Align sequences
	align_sequences(input_file, aligned_file)

	#make tree
	alignment = AlignIO.read(str(aligned_file), "fasta")
	tree = build_dendrogram(alignment)

	Phylo.write(tree, "results/tree.nwk", "newick")

	#Show file saves
	print("Dendogram saved to results/tree.nwk")
	print(f"Number of leaves: {len(tree.get_terminals())}")

if __name__ == "__main__":
        main()
