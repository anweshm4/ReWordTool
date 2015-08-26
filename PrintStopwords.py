# MainForm.py
# Author: Amlanjyoti Saikia
# PartOf: Project ReWord
# Date: 31/July/2015

from xml.etree import cElementTree
from nltk import corpus
import pywsd.utils


stop_word_list = corpus.stopwords.words("english")
haveSense = []
haveNoSense = []

rootElement = cElementTree.Element("root")
for stop_word in stop_word_list:
    wordElement = cElementTree.SubElement(rootElement, "StopWord", word=stop_word)
    if pywsd.utils.has_synset(stop_word):
        senses = corpus.wordnet.synsets(stop_word)
        for sense in senses:
            senseElement = cElementTree.SubElement(wordElement, "Sense", senseCode=sense.name())
            senseElement.text = sense.definition()
        haveSense.append(stop_word)
    else:
        senseElement = cElementTree.SubElement(wordElement, "Sense", senseCode="NA")
        haveNoSense.append(stop_word)

tree = cElementTree.ElementTree(rootElement)
tree.write("words.xml")

fileHaveSense = open('haveSense.txt', 'a')
for word in haveSense:
    fileHaveSense.write(word+"\n")
fileHaveSense.close()

fileHaveNoSense = open('haveNoSense.txt', 'a')
for word in haveNoSense:
    fileHaveNoSense.write(word+"\n")
fileHaveNoSense.close()
