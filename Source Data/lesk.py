from nltk.wsd import lesk
from nltk import word_tokenize
from nltk.corpus import wordnet as wn
print "Word Sense Disambiguation"
print" --------------------------"
sentence = raw_input('Enter your sentence : ')
sent = word_tokenize(sentence)
word = raw_input('Enter word to derive meaning of : ')
pos = raw_input('Enter type of word : ')
synset = (lesk(sent, word, pos))
synset=str(synset)
print synset
finalsynset = synset[7:]
finalsynset=finalsynset[:-1]
#value=[int(s) for s in finalsynset.split() if s.isdigit()]
print finalsynset
value=int(finalsynset.split()[0])
print value
    

#print (wn.synset(finalsynset).definition())


