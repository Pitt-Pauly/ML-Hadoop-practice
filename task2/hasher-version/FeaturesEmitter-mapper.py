#!/usr/bin/python

#### ------------- task 2 FeatureEmitter-mapper.py -------------- ####

import sys, re

for line in sys.stdin:

	# split into words
	words =  re.compile(r'[a-zA-Z]+').findall(line)

	for word in words:
		label = (not word.isdigit()) & (not word.islower())
		if (len(word)>2):
			fs = [word, word[-2:], word[-3:], word[0:2], word[0:3]]
		else:
			if (len(word)>1):
				fs = [word, word[-2:], word[0:2]]
			else:
				fs = [word]
		for i in range(0,len(fs)):  
			# key encoding! label + featureIndex + (T|F)
			hashF = fs[i].lower()+str(i)+str(label)[0]
			print '%s\t1' % hashF
		

