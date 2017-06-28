#!/usr/bin/python

import sys

for line in sys.stdin:
	# split into words
	line = line.strip()
	word, pT, pF = line.split('\t')
	
	if (pT < pF):
		print word.lower()
	else:
		print word[0].capitalize()
