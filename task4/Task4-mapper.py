#!/usr/bin/python

import sys

ps = {}	

#for line in sys.stdin:
for line in ["byekbkj	0	0	88	33	0.777","@hellobk	0	0	99"]:
	# split into words
	line = line.strip()
	params = line.split('\t')

	# is the current line from the test set? -> @ marker
	# [word, word[-2:], word[-3:], word[0:2], word[0:3]]
	if (params[0][0] == '@'):
		feat = params[0][1:]
		i = params[1]		
		l = params[2]
		k = (feat,i,l) 
		ilist = [0]
		if ((i==2)|(i==4)|((i==0)&(len(feat) > 2))):
			ilist = [0,1,2,3,4]
		elif ((i==1) | (i==3)| ((i==0)&(len(feat) > 1))):
			ilist = [0,1,3]
		pT = 1
		pF = 1
		for x in ilist:
			pT *= ps.get((feat,x,True),0.000001)
			pF *= ps.get((feat,x,False),0.000001)
		print "%s\t%f\t%f" % (feat, pT, pF) 
		
	else:
		#training set - store in dict
		feat, index, label, countS, countO, prob = params
		k = (feat,index,label) 
		ps[k] = prob
