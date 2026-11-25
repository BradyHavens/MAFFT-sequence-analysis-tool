# MAFFT-sequence-analysis-tool

A python script for performing multiple sequence alignment (MSA) on biological sequences from FASTA files using MAFFT.

## OVERVIEW
This project is provides a basic workflow for aligning sequence data found in FASTA files using MAFFT and using those alignments to produce dendrograms in a Newick format. It also uses a bootstrap method to print a consensus tree separate from the produced Newick file. This project is being used for bioinformatics learning and sequence analysis; it has potential to grow into a component of larger workflows.

## Features
-Accepts FASTA sequence data
-Uses MAFFT to align sequences
-Produces aligned sequence files in FASTA format
-uses aligned sequences to produce a .nwk file containing a dendrogram of sequence similarity.
-uses bootstrap to print a consensus tree 

## Requirements (Other versions may work, these were used for development)
Ubuntu
Python 3.14.4
Biopython 1.88
MAFFT v7.525

## Usage
In a virtual environment in terminal, run:
python phylogeny/source/alignment.py path/yourFASTAfile.fasta
Aligned sequence and Newick file will appear in results/yourFASTAfile_aligned.fasta and results/tree.nwk

## Acknowledgements
This projects relies of MAFFT, developed by its own authors. Refer to the MAFFT project for its documentation and Liscence.
