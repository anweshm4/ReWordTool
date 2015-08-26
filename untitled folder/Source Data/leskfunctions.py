import nltk
from nltk.corpus import wordnet as wn

stopwords = nltk.corpus.stopwords.words(fileids='english')
stopwords += ['thing', 'one']

words = [('salad', 'NOUN'), ('greens', 'NOUN'), ('tomato','NOUN'), 
         ('addition', 'NOUN'), ('meal', 'NOUN'), ('avocado', 'NOUN'), 
         ('special', 'ADJ')]

def sensesPOS(word):
    '''Given word tuple with POS get Synset senses as output array'''
    
    if (word[1] == 'NOUN'):
        return wn.synsets(word[0], pos=wn.NOUN)
    
    return wn.synsets(word[0], pos=wn.ADJ)

def removeStopWords(words):
    '''Given a list of words remove uninformative words'''

    i = 0
    
    while i < len(words):
        if not words[i].isalpha(): 
            del words[i]
        elif words[i] in stopwords:
            del words[i]
        else: 
            i += 1
            
    return words

def addExamples(bag, sense):
    '''Given a word sense, add examples to bag'''
    
    for i in sense.examples:
        definition = i
        definition = definition.replace("(", "")
        definition = definition.replace(")", "")
        definition = definition.split()
        definition = removeStopWords(definition)
        bag = addToBag(bag, definition)
        
    return bag
    

def addToBag(bag, words):
    '''Lemmatize words and only add to bag if not already there'''

    lemmatizer = nltk.PorterStemmer()
    
    for i in words:
        i = lemmatizer.stem(i)
        if i not in bag: 
            bag += [i]
            
    return bag

def getDi(senses):
    '''Given senses of a word get bag of words in dictionary defn'''

    bag = []
    
    for i in senses:
        definition = i.definition
        definition = definition.replace("(", "")
        definition = definition.replace(")", "")
        definition = definition.split()
        definition = removeStopWords(definition)
        bag = addToBag(bag, definition)
        bag = addExamples(bag, i)

    return bag

def getB(other_words):
    '''Given other words in context window get dictionary defn of all senses
    of all other words'''

    bag = []
    
    for words in other_words:
        senses = wn.synsets(words[0])
        bag += getDi(senses)
        
    return bag

def getCount(word_sense, other_words):
    '''Given word_sense and other_words return count of words that overlap
    and an array of overlapping words'''
    
    count = 0
    overlap = []
    
    B = getB(other_words)
    Di = getDi([word_sense])
    
    for word in Di:
        if word in B: 
            count += 1
            overlap.append(word)
    
    return [count, overlap]
    
def getOutput(senses, other_words):
    '''Given target words format output'''
    
    output_string = ""
    max_count = 0
    choice = senses[0]
    
    for i in senses:
        sense = formatWord(i)
        gloss = i.definition
        [count, overlap] = getCount(i, other_words)
        
        if count > max_count or max_count == 0:
            max_count = count
            choice = i
        
        output_string += sense + "\t" + gloss + "\t" + str(count) + "\t" + str(overlap) + "\n"
        
    return formatWord(choice) + "\n" + output_string
        
def formatWord(synset):
    
    string = str(synset)
    string = string.replace("Synset('", "")
    string = string.replace("')", "")
    string = string.split(".")
    
    return string[0] + "#" + string[-1] + string[-2]
    
if __name__=="__main__":
    
    for i in range(0, len(words)):
        print words[i][0] + "/" + words[i][1] 
        senses = sensesPOS(words[i])
        other_words = words[:i] + words[i+1:]
        print getOutput(senses, other_words)
        
        print "\n"

