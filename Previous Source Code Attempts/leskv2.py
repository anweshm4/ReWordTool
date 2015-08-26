from nltk.wsd import lesk
from nltk import word_tokenize
from nltk.corpus import wordnet as wn
print "Word Sense Disambiguation"
print" --------------------------"
'''sentence = raw_input('Enter your sentence : ')
sent = word_tokenize(sentence)
word = raw_input('Enter word to derive meaning of : ')
pos = raw_input('Enter type of word : ')
syns= (lesk(sent, word, pos))
'''
print (wn.synset('set.v.01').definition())
print (wn.synset('set.v.01').lemma_names)
