from __future__ import division
import nltk
from nltk.corpus import wordnet as wn


tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
fp = open("data.txt")
data = fp.read()

#to tokenize input text into sentences

print '\n-----\n'.join(tokenizer.tokenize(data))# splits text into sentences

#to tokenize the tokenized sentences into words

tokens = nltk.wordpunct_tokenize(data)
text = nltk.Text(tokens)
words = [w.lower() for w in text]  
print words     #to print the tokens

for a in words:
    print a

syns = wn.synsets(a)
print "synsets:", syns

for s in syns:
    for l in s.lemmas:
        print l.name
    print s.definition
    print s.examples
