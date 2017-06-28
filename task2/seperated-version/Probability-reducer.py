#!/usr/bin/python

import sys, re

ps = {}	

for line in sys.stdin:
	# split into words
	line = line.strip()
	#hashedF, countS, countO = line.split('\t')
	word, index, label, count, oppcount = line.split('\t')
	k = (word,index,label)
	if (ps.__contains__(k)):
		ps[k] = (float(ps[k]) + (count / float(count + oppcount))) / 2.0
	else:
		ps[k] = (count / float(count + oppcount))
	#if (ps.__contains__(hashedF)):
		# take the average probability of both
	#	ps[hashedF] = (float(ps[hashedF]) + (countS / float(countS + countO))) / 2.0
	#else:
		# since the feature's index is encoded in the name 
		# this correctly gives p(fi|l)  
	#	ps[hashedF] = (countS / float(countS + countO))

	if (len(ps) > 10000):
		for hf,p in ps.items():
			print "%s\t%f" % (hf, float(p)) 
	
for hf,p in ps.items():
	print "%s\t%f" % (hf, float(p)) 
