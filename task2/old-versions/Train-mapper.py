#!/usr/bin/python

import sys, re

feature2count = {}	

for line in sys.stdin:
	# split into words
	words =  re.compile(r'[a-zA-Z]+').findall(line)

	for word in words:
		label = (not word.isdigit()) & (not word.islower())
		if (len(word)>3):
			fs = [word, word[-2:], word[-3:], word[0:2], word[0:3]]
		else:
			if (len(word)==3):
				fs = [word, word[-2:], word[0:2]]
			else:
				fs = [word]
		for f in fs:
			# key encoding! label + (F|T)
			fl = f+str(label)[0]
			if (feature2count.__contains__(fl)):
				feature2count[fl] += 1
			else:
				feature2count[fl] = 1
		# check map size after every added word, > 1 kB ? -> flush
		# dict.__sizeof__() does not work on hadoop
		if (len(feature2count) > 80):
			for fi,c in feature2count.items():
				label = (fi[-1] != 'T')
				fo = fi[0:-1]+ str(label)[0]
				fsum = 0
				if (feature2count.__contains__(fo)):
					fsum = c + feature2count[fo]
				else:
					fsum = c
				print "%s\t%d\t%d" % (fi,c,fsum)
			feature2count.clear()

for fi,c in feature2count.items():
	label = (fi[-1] != 'T')
	fo = fi[0:-1]+ str(label)[0]
	fsum = 0
	if (feature2count.__contains__(fo)):
		fsum = c + feature2count[fo]
	else:
		fsum = c
	print "%s\t%d\t%d" % (fi,c,fsum)
feature2count.clear() 
