#!/usr/bin/python

import sys

# key of the form (word, X) where X is either ''T' or 'F'
ps = {}

for line in sys.stdin:
	line = line.strip()
	fi, freq, fsum = line.split('\t')
	key = (fi[0:-1],fi[-1])
	if (ps.__contains__(key)):
		# approximation, taking many averages will be okay in the end
		ps[key] = (float(ps[key]) + (float(freq) / float(fsum))) / 2.0
	else:
		# +0.0 to force floating point division
		ps[key] = float(freq) / float(fsum) 
	
for k, p in ps.items():
	print '%s\t%f' % (k, p)
