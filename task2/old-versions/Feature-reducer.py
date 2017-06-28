#!/usr/bin/python

import sys

feature2count = {}	

for line in sys.stdin:
	# split into words
	line = line.strip()
	feat, index, label, count = line.split('\t')
	
	# this is the final feature count  of that kind since they are all 
	# directed to the same reducer.
	k = (feat, index, label)
	feature2count[k] = int(feature2count.get(k,0)) + int(count)
	
	if (len(feature2count) > 10000):
		for (f,i,l),c in feature2count.items():
			p = float(c) / float(c + feature2count.get(f,i,not l),0.0000001)
			print "%s\t%d\t%d\t%d\t%f" % (f, i, int(l), int(c), p) 
	
for (f,i,l),c in feature2count.items():
	p = float(c) / float(c + feature2count.get(f,i,not l),0.0000001)
	print "%s\t%d\t%d\t%d\t%f" % (f, i, int(l), int(c), p) 
