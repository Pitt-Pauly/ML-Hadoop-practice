#!/usr/bin/python

import sys

feature2count = {}	

for line in sys.stdin:
	# split into words
	line = line.strip()
	hashedF, count = line.split('\t')

	feature2count[hashedF] = int(feature2count.get(hashedF,0)) + int(count)

	if (len(feature2count) > 10000):
		for hf,c in feature2count.items():
			oppositeFlag = str(hf[-2] != 'T')[0]
			oppfeat = hf[0:-2]+ oppositeFlag + hf[-1]
			oppcount = feature2count.get(oppfeat,0)
			print "%s\t%d\t%d" % (hf, int(c), int(oppcount)) 
	
for hf,c in feature2count.items():
	oppositeFlag = str(hf[-2] != 'T')[0]
	oppfeat = hf[0:-2]+ oppositeFlag + hf[-1]
	oppcount = feature2count.get(oppfeat,0)
	# format: hashedfeature selfcount othercount
	print "%s\t%d\t%d" % (hf, int(c), int(oppcount))
