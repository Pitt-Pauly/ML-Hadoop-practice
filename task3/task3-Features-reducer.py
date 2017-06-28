#!/usr/bin/python

import sys

feature2count = {}	

for line in sys.stdin:
	# split into words
	line = line.strip()
	feat, index, label = line.split('\t')
	
	k = (feat, index, label)
	feature2count[k] = int(feature2count.get(k,0)) + 1
	
	if (len(feature2count) > 10000):
		for (f,i,l),c in feature2count.items():
			print "@%s\t%d\t%d\t%d" % (f, int(i), int(l), int(c)) 
	
for (f,i,l),c in feature2count.items():
	print "@%s\t%d\t%d\t%d" % (f, int(i), int(l), int(c)) 
