#!/usr/bin/python

import sys

feature2count = {}	

for line in sys.stdin:
#for line in ["word	0	0	4"]:
	# split into words
	line = line.strip()
	feat, index, label = line.split('\t')
	
	# this is the final feature count  of that kind since they are all 
	# directed to the same reducer.
	k = (feat, index, label)
	feature2count[k] = int(feature2count.get(k,0)) + 1
	
	if (len(feature2count) > 10000):
		for (f,i,l),c in feature2count.items():
			#print (f,i,l,(l!=True),c)
			co = feature2count.get((f,i,(l!=True)),0.000001)
			p = float(c) / float(c + co)
			print "%s\t%d\t%d\t%d\t%d\t%f" % (f, int(i), int(l), int(c), int(co), p) 
	
for (f,i,l),c in feature2count.items():
	#print (f,i,l,(l!=True),c)
	co = feature2count.get((f,i,(l!=True)),0.000001)
	p = float(c) / float(c + co)
	print "%s\t%d\t%d\t%d\t%d\t%f" % (f, int(i), int(l), int(c), int(co), p) 
