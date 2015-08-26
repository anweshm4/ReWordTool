# ParaphrasingEngine.py
# Author: Amlanjyoti Saikia
# Date: 03 - Aug - 2015

import nltk
import pywsd.utils
import pywsd.lesk
import string
# import pywsd.lesk
# from pywsd.lesk import original_lesk
# from pywsd.lesk import simple_lesk
# from pywsd.lesk import adapted_lesk
# from pywsd.lesk import cosine_lesk
# from pywsd import disambiguate
# from pywsd.utils import has_synset


class ParaphrasingEngine:

    input = None
    words = None

    def __init__(self, input_string):
        self.input = input_string
        print "Breaking input into words..."
        # self.words = nltk.word_tokenize(self.input.translate(string.maketrans("",""), string.punctuation))
        # self.words = nltk.word_tokenize(self.input.translate(None, string.punctuation))
        self.words = nltk.word_tokenize(str(self.input).translate(None, string.punctuation))
        # print "\nChecking synsets of each word . . ."
        # print (pywsd.disambiguate(self.input))
        return

    def disambiguate_original_lesk(self):
        print "\nINFO: Disambiguating via original lesk...\n============================== \n"
        original_answer = []
        for each_word in self.words:
            if pywsd.utils.has_synset(each_word):
                answer = pywsd.lesk.original_lesk(self.input, each_word)
                original_answer.append(answer)
                print "Sense: ", answer
                print each_word+": "+answer.definition()+"\n"
            else:
                print each_word+": "+each_word+"\n"
                original_answer.append(each_word)
        return original_answer

    def disambiguate_simple_lesk(self):
        print "\nINFO: Disambiguating via simple lesk...\n============================== \n"
        simple_answer = []
        for each_word in self.words:
            if pywsd.utils.has_synset(each_word):
                answer = pywsd.lesk.simple_lesk(self.input, each_word)
                simple_answer.append(answer)
                print "Sense: ", answer
                print each_word+": "+answer.definition()+"\n"
            else:
                print each_word+": "+each_word+"\n"
                simple_answer.append(each_word)
        return simple_answer

    def disambiguate_adapted_lesk(self):
        print "\nINFO: Disambiguating via adapted lesk...\n============================== \n"
        adapted_answer = []
        for each_word in self.words:
            if pywsd.utils.has_synset(each_word):
                answer = pywsd.lesk.adapted_lesk(self.input, each_word)
                adapted_answer.append(answer)
                print "Sense: ", answer
                print each_word+": "+answer.definition()+"\n"
            else:
                print each_word+": "+each_word+"\n"
                adapted_answer.append(each_word)
        return adapted_answer

    def disambiguate_cosine_lesk(self):
        print "\nINFO: Disambiguating via cosine lesk......\n============================== \n"
        cosine_answer = []
        for each_word in self.words:
            if pywsd.utils.has_synset(each_word):
                answer = pywsd.lesk.cosine_lesk(self.input, each_word)
                cosine_answer.append(answer)
                print "Sense: ", answer
                print each_word+": "+answer.definition()+"\n"
            else:
                print each_word+": "+each_word+"\n"
                cosine_answer.append(each_word)
        return cosine_answer