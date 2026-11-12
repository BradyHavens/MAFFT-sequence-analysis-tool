from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor

from distances import calculate_dist_matrix

def build_dendrogram(alignment):
	"""Construct a tree with neightbor joining"""

	#make tree
	distance_matrix = calculate_dist_matrix(alignment)
	print(distance_matrix)

	constructor =  DistanceTreeConstructor()
	tree = constructor.nj(distance_matrix)

	return tree
