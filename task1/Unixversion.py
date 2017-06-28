#!/usr/bin/python

##
#   Pierre Pauly
#   s0836497	
#   level 10
#
#   Further Documentation in ReadMe.txt
##
import sys, re, string
from lxml import html
from lxml.html.clean import clean_html

class SimpleCaps:
	""" Simple word capitalizing script using Naive Bayes. (Unix version) """

	##
	#   init 
	#
	#   params:	debug, boolean flag which turns debug messages on/off. 
	#			filename, 	path to training set (txt file).
	#						default if none given is './small.txt'
	##
	def __init__(self, debug = False, filename = '../files/small.txt'):
		self.freqs = {}
		#self.wordbag = []
		self.p = {}
		self.debugMode = debug
		self.train(filename)
		
	def train(self, filename = '../files/small.txt'):	
		wordlist = ""
		
		#	filter all html (script etc) tags out of the file
		tree = html.parse(filename)
		tree = clean_html(tree)
		text = tree.getroot().text_content()

		wordlist =  re.compile(r'[a-zA-Z]+').findall(text)
		
		if (self.debugMode):
			print ("\nFiltered and split training set, first 10 elements are:")
			for i in wordlist[0:10]:
				print (i)

		#	split into features for Naive Bayes training
		self.createFeatures(wordlist)

	##
	#   Task 1.
	#   Use the following set of features:
	#	   the word itself,
	#	   the last two letters,
	#	   the last three letters,
	#	   the first two letters,
	#	   the first three letters.
	#
	#   label:  1 if word is capitalized (any letter is upper case),
	#		   	0 otherwise (digit)
	#
	#   freqDict:   dictionary (map) containing the frequencies of the words appearing of the form:
	#			   	key: (feature, featureIndex, label)
	#			   	value: number of occurances 
	##
	def createFeatures(self,words):
		self.freqs = {}
		for word in words:
			label = (not word.isdigit()) & (not word.islower())
			word = word.lower()
			if (len(word)>2):
				features = [ word, word[-2:], word[-3:], word[0:2], word[0:3] ]
			else:
				if (len(word)>1):
					features = [ word, word[-2:], word[0:2] ]
				else:
					features = [ word ]
			# and count the frequencies of the individual (feature, label) pairs
			for i in range(0,len(features)):
				k = (features[i],i,label)
				self.freqs[k] = self.freqs.get(k,0) + 1
		
		if (self.debugMode):
			print ("\nFrequency dictionary created, first few results:\n")
			print "%r" % self.freqs.items()[0:4]

	##
	#	calc_fil_prop
	#
	#	params:	fi, the word to be looked up, 
	#			l,	the label. can be either True or False
	#	returns: p, s.t.
	#				   					freq(fi,l)
	#				p(fi|l) = 	-------------------------
	#							 freq(fi,0) + freq(fi,1)
	#
	##
	def calc_fil_prob(self,f,i,l):
		# get the 'other' frequency count
		fo = self.freqs.get((f,i,int(not l)),0.000001)
		f = self.freqs.get((f,i,l),0.000001)
		p = f / float(fo + f)
		return p

	##
	#	calc_props
	#
	#	params: p, 	dictionary containing the probabilities p(fi|l)
	# 				to be used in the Naive Bayes model.
	#				
	##
	def calc_fil_probs(self,p):
		if (self.freqs == {}):
			self.train()

		for (f,i,l) in self.freqs.keys():
			if (not p.__contains__((f,i,l))):
				p[(f,i,l)] = self.calc_fil_prob(f,i,l)
			else: 
				p[(f,i,l)] = (p[(f,i,l)] + self.calc_fil_prob(f,i,l)) /2.0
		return p
	
	def calc_p(self, label, word):
		if (self.p == {}):
			self.init_NB_model()

		if (len(word)>2):
			features = [ word, word[-2:], word[-3:], word[0:2], word[0:3] ]
		else:
			if (len(word)>1):
				features = [ word, word[-2:], word[0:2] ]
			else:
				features = [ word ]
		# and count the frequencies of the individual (feature, label) pairs
		multi = 1
		for i in range(0,len(features)):
			k = (features[i],i,label)
			multi *= self.p.get(k,1)
		return multi

	def init_NB_model(self):
		self.p = self.calc_fil_probs({})
		if (self.debugMode):
			print ("\nCalculating probabilites p(fi|l), 3 examples:\n")
			print  "p(%s) = %f" % (self.p.items()[0][0],self.p.items()[0][1]) 
			print  "p(%s) = %f" % (self.p.items()[1][0],self.p.items()[1][1])
			print  "p(%s) = %f" % (self.p.items()[2][0],self.p.items()[2][1])
	
	##
	#	adjust_case
	#
	#	params: word, the word whose case is to be analysed, and modified
	#
	#	return: word, the word with the correct case. (according to 
	#				  the Naive Bayes model.
	#
	#	description: 	Uses Naive Bayes assumptions and previously 
	#					counted frequencies to predict the case of the 
	#					first letter of the given word.
	#
	##
	def adjust_case(self, word):
		if (self.p == {}):
			self.init_NB_model()
		word = word.strip()
		if ((word != None) & (word != '')): 
			pT = self.calc_p(True,word)
			pF = self.calc_p(False,word)
			if (pT > pF):
				word = word.capitalize()
				#if (self.debugMode):
				#	print ('p(T|',word,') = ', pT, '\np(F|',word,') = ',pF,'\nresult: ', word, 'with ', pT*100, '% certainty')
			else:
				word = word.lower()
				#if (self.debugMode):
				#	print ('p(T|',word,') = ', pT, '\np(F|',word,') = ',pF,'\nresult: ', word, 'with ', pF*100, '% certainty')
		return word

def main():
	try:
		l = len(sys.argv)
		trainingfile = ''
		if (l == 5):
			if ((sys.argv[1] == '-d') & (sys.argv[2] == '-t')):
				debugMode = True
				trainingfile = sys.argv[3]
			else:
				sys.exit("Unsupported parameter. Correct syntax:\npython3 Unixversion [-d|-t trainingfile.txt] <target.txt>")
		elif (l == 3):
			param = sys.argv[1]
			if (param == '-d') :
				debugMode = True
			elif (param == '-t'):
				trainingfile = sys.argv[2]
		elif (l != 2): 
			sys.exit("Parameter(s) missing. Please at least specify a document to be analysed.")

		target = sys.argv[-1]
		# assuming the target file as only on word per line
		f = open(target, "r")
		doc = f.readlines()
		f.close()
		
		if (trainingfile != ''):
			c = SimpleCaps(debugMode,trainingfile)
		else:
			c = SimpleCaps(debugMode)
		c.init_NB_model()
		
		f = open(target[0:-4]+"-capitalized.txt","w")
		for word in doc:
			w = c.adjust_case(word)
			f.write(w+'\n')
		f.close()
	except:
		# handle exceptions
		if (IOError):
			print (sys.argv[-1], len(sys.argv))
			sys.exit("invalid filename. Unable to open file: "+sys.argv[-1])
	else:
		return 0 # exit errorlessly

if __name__ == '__main__':
	main()
	
