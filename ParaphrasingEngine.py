import nltk
import pywsd.utils
import pywsd.lesk
import string


class ParaphrasingEngine:

    input = None
    words = None
    stop_word_dict = None

    def __init__(self, input_string, stop_word_dictionary):
        self.input = input_string
        self.stop_word_dict = stop_word_dictionary
        print "Breaking input into words..."
        # Break into words. Remove punctuation.
        self.words = nltk.word_tokenize(str(self.input).translate(None, string.punctuation))
        return

    def disambiguate_original_lesk(self):  # TODO: Try to implement original lesk as well.
        print "\nINFO: Disambiguating via original lesk...\n============================== \n"
        original_answer = []
        for each_word in self.words:
            if pywsd.utils.has_synset(each_word): # if word has sense
                answer = pywsd.lesk.original_lesk(self.input, each_word) # get sense using pywsd library
                original_answer.append(answer) # append sense of each word
                print "Sense: ", answer
                print each_word+": "+answer.definition()+"\n"
            else:
                temp = each_word
                each_word = self.process_stop_word(each_word) #TODO: Link this with the stopwords dictionary
                print temp+": "+each_word+"\n"
                original_answer.append(each_word) # append word if no sense found
        return original_answer

    def disambiguate_simple_lesk(self):  # Same as above
        print "\nINFO: Disambiguating via simple lesk...\n============================== \n"
        simple_answer = []
        for each_word in self.words:
            if pywsd.utils.has_synset(each_word):
                answer = pywsd.lesk.simple_lesk(self.input, each_word)
                simple_answer.append(answer)
                print "Sense: ", answer
                print each_word+": "+answer.definition()+"\n"
            else:
                temp = each_word
                each_word = self.process_stop_word(each_word) #TODO: Link this with the stopwords dictionary
                print temp+": "+each_word+"\n"
                simple_answer.append(each_word)
        return simple_answer

    def disambiguate_adapted_lesk(self):  # Same as above
        print "\nINFO: Disambiguating via adapted lesk...\n============================== \n"
        adapted_answer = []
        for each_word in self.words:
            if pywsd.utils.has_synset(each_word):
                answer = pywsd.lesk.adapted_lesk(self.input, each_word)
                adapted_answer.append(answer)
                print "Sense: ", answer
                print each_word+": "+answer.definition()+"\n"
            else:
                temp = each_word
                each_word = self.process_stop_word(each_word) #TODO: Link this with the stopwords dictionary
                print temp+": "+each_word+"\n"
                adapted_answer.append(each_word)
        return adapted_answer

    def disambiguate_cosine_lesk(self): # Same as above
        print "\nINFO: Disambiguating via cosine lesk......\n============================== \n"
        cosine_answer = []
        for each_word in self.words:
            if pywsd.utils.has_synset(each_word):
                answer = pywsd.lesk.cosine_lesk(self.input, each_word)
                cosine_answer.append(answer)
                print "Sense: ", answer
                print each_word+": "+answer.definition()+"\n"
            else:
                temp = each_word
                each_word = self.process_stop_word(each_word) #TODO: Link this with the stopwords dictionary
                print temp+": "+each_word+"\n"
                cosine_answer.append(each_word)
        return cosine_answer

    def process_stop_word(self, word):
        if self.stop_word_dict.has_sense(word):
            return self.stop_word_dict.get_sense(word)
        else:/f
            return word
