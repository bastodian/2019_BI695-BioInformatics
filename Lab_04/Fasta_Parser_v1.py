#!/usr/bin/env python

import sys

Counter = 0
Nucleotides = ['A','G','C','T']
SeqDict = {}

with open('Hydra_MiniCollagens.fst', 'r') as Fasta:
	for Line in Fasta:
		Counter += 1
		if Counter % 2 != 0:
			Header = Line.rstrip()
		elif Counter % 2 == 0:
			Sequence = Line.rstrip()
			SeqDict[Header] = Sequence

for Seq in SeqDict:
	if set(Nucleotides) == set(SeqDict[Seq]):
		sys.stdout.write('%s\n%s\n' % (Seq, SeqDict[Seq]))
	else:
		sys.stderr.write('%s\n%s\n' % (Seq, SeqDict[Seq]))
