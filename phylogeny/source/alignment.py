import argparse
import subprocess
from pathlib import Path

from Bio import SeqIO

#Align with MAFFT
def align_sequences(input_file, output_file):
	"""Align FASTA sequences with MAFFT"""

	input_file = Path(input_file).resolve()
	output_file = Path(output_file).resolve()

	#check if input exists
	if not input_file.is_file():
		raise FileNotFoundError(f"Input file not found: {input_file}")

	#Check and read FASTA
	records = list(SeqIO.parse(input_file, "fasta"))

	if len(records) < 2:
		raise ValueError("At least 2 sequences required")

	if any(not record.seq for record in records):
		raise ValueError("FASTA file contains an empty sequence")

	#run MAFFT and get output
	result = subprocess.run(["mafft", "--auto", str(input_file)], capture_output = True, text = True, check = True)

	output_file.parent.mkdir(parents = True, exist_ok = True)
	output_file.write_text(result.stdout, encoding = "utf-8")

	alignment = list(SeqIO.parse(output_file, "fasta"))

	if len(alignment) != len(records):
		raise ValueError("Alignment contains incorrect number of sequences")

	lengths = {len(record.seq) for record in alignment}

	if len(lengths) != 1:
		raise ValueError("Output sequences are uneven lengths")

	print(f"Input sequences: {len(records)}")
	print(f"Aligned sequences: {len(alignment)}")
	print(f"Alignment length: {next(iter(lengths))} positions")
	print(f"Saved alignment to: {output_file}")

def main():
	parser = argparse.ArgumentParser(description = "Align sequences with MAFFT")
	parser.add_argument("input", help = "Input FASTA file")
	parser.add_argument("-o", "--output", help = "Output FASTA file")

	args = parser.parse_args()

	input_path = Path(args.input)
	project_root = Path(__file__).resolve().parents[1]

	output_path = (Path(args.output)
	if args.output
	else project_root / "results" / f"{input_path.stem}_aligned.fasta"
	)

	try:
		align_sequences(input_path, output_path)
	except (FileNotFoundError, ValueError, subprocess.CalledProcessError) as error:
		print(f"Error: {error}")
		raise SystemExit(1)

if __name__ == "__main__":
	main()
