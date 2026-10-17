from Bio import AlignIO, Phylo
from Bio.Align import MultipleSeqAlignment
from Bio.Phylo.TreeConstruction import DistanceMatrix

#Only accept Amino Acids
Valid_AA = set("-ARNDCEQGHILKMFPSTWYV")

def calculate_dist_matrix(alignment: MultipleSeqAlignment,) -> DistanceMatrix:
	"""Calculate p-distances for alignment"""

	records = list(alignment)

	if len(records) < 3:
		raise ValueError("At least three sequences needed")

	names = [record.id for record in records]

	if len(set(names)) != len(names):
		raise ValueError("Sequence IDs must be unique")

	lengths = {len(record.seq) for record in records}

	if len(lengths) != 1:
		raise ValueError("All sequences must be the same length")

	#Make matrix
	matrix = []

	for i, seq_a in enumerate(records):
		row = []
		for j in range(i + 1):
			if i == j:
				row.append(0.0)
				continue
			seq_b = records[j]
			differences = 0
			comparable = 0
			for aa_a, aa_b in zip (str(seq_a.seq).upper(), str(seq_b.seq).upper(),):
				#Ignore non-accepted characters
				if aa_a not in Valid_AA or aa_b not in Valid_AA:
					continue
				comparable += 1

				if aa_a != aa_b:
					differences += 1
			if comparable == 0:
				raise ValueError("No comparable amino acids for {names[i]} and {names[j]}")

			distance = differences / comparable
			row.append(distance)
		matrix.append(row)
	return DistanceMatrix(names, matrix)
