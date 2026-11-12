from Bio import AlignIO
from Bio import Phylo
from pathlib import Path
from Bio.Phylo.Consensus import bootstrap_consensus, majority_consensus
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

def bootstrap(alignment):
	msa = AlignIO.read(alignment, "fasta")
	calculator = DistanceCalculator("identity")
	constructor = DistanceTreeConstructor(calculator)

	consensus_tree = bootstrap_consensus(msa, 100, constructor, majority_consensus)

	Phylo.draw_ascii(consensus_tree)
