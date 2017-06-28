##
#   Pierre Pauly
#   s0836497    
#   level 10
#
#   Further Documentation in ReadMe.txt
##

import re

class SimpleCaps:
    """ Simple word capitalizing script using Naive Bayes. (Unix version) """

    ##
    #   init 
    #
    #   params: filename, path to training set (txt file).
    #
    ##
    def __init__(self, filename = ''):
        self.freqs = {}
        self.wordbag = []
        
        # default file
        if (filename == ''):
            filename = './small.txt'

        with open(filename,'r') as f:
            word_list = f.read()

        #assumption: space delimited sentences
        word_list = re.split(" *",word_list)
        self.createFeatures(word_list)    

    ##
    #   Task 1.
    #   Use the following set of features:
    #       the word itself,
    #       the last two letters,
    #       the last three letters,
    #       the first two letters,
    #       the first three letters.
    #
    #   value (val):  1 if feature is present
    #           0 otherwise
    #
    #   label:  1 if word is capitalized (first letter is upper case),
    #           0 otherwise
    #
    #   freqDict:   dictionary (map) containing the frequencies of the words appearing of the form:
    #               key: (feature, label)
    #               value: number of occurances 
    ##
    def createFeatures(self,words):
        val = 1        
        for word in words:
            label = word[0].islower()
            if (len(word)>=3):
                features = [(word,val), (word[-2:], val), (word[-3:],val), (word[0:1],val), (word[0:2],val)]
            else:
                if (len(word)==2):
                    features = [(word,val), (word[-2:], val), (word[0:1],val), (word[0:2],val)]
                else:
                    features = [(word,val)]
            self.wordbag.append((features,label))
            # and count the frequencies
            for f,v in features:
                if (self.freqs.__contains__((f,label))):
                    self.freqs[(f,label)] +=1
                else:
                    self.freqs[(f,label)] = 1
        print (self.wordbag, self.freqs)
            
        
            
        
