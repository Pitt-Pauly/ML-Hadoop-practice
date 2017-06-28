#!/usr/bin/python

import sys, re

feature2count = {}	

for line in sys.stdin:
	# split into words
	line = line.strip()
	#hashedF, count = line.split('\t')
	word, index, label, count = line.split('\t')

	#feature2count[hashedF] = int(feature2count.get(hashedF,0)) + int(count)
	feature2count[(word,index,label)] = int(feature2count.get((word,index,label),0)) + int(count)

	if (len(feature2count) > 10000):
		for (w, i, l),c in feature2count.items():
			oppc = feature2count.get((w,i,int(not l)),0)
			print "%s\t%d\t%d\t%d\t%d" % (w,i,l,c,oppc)
		
		#for hf,c in feature2count.items():
		#	oppositeFlag = str(hf[0] != 'T')[0]
		#	oppfeat = oppositeFlag + hf[1:] 
		#	oppcount = feature2count.get(oppfeat,0)
		#	print "%s\t%d\t%d" % (hf, int(c), int(oppcount)) 
for (w, i, l),c in feature2count.items():
	oppc = feature2count.get((w,i,int(not l)),0)
	print "%s\t%d\t%d\t%d\t%d" % (w,i,l,c,oppc)

#for hf,c in feature2count.items():
#	oppositeFlag = str(hf[0] != 'T')[0]
#	oppfeat = oppositeFlag + hf[1:]
#	oppcount = feature2count.get(oppfeat,0)
	# format: hashedfeature selfcount othercount
#	print "%s\t%d\t%d" % (hf, int(c), int(oppcount))
