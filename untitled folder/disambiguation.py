import nltk
from pywsd.lesk import simple_lesk
from pywsd.lesk import adapted_lesk
from pywsd.lesk import cosine_lesk
from pywsd import disambiguate
from pywsd.similarity import max_similarity as maxsim
from pywsd.utils import has_synset

simplelesk_answer = []
adaptedlesk_answer = []
cosinelesk_answer = []

print "\nSentence Context Disambiguation\n============================== \n"

raw_sentence=raw_input("Please enter your sentence : ")
words = nltk.word_tokenize(raw_sentence)
print "\nChecking synsets of each word . . .\n==========================================\n"
print(disambiguate(raw_sentence))
print "\nDisambiguating your sentence word by word using Simple Lesk algorithm. Hold on. \n======================================================"
for eachword in words:
    if has_synset(eachword):
        answer = simple_lesk(raw_sentence, eachword)
        simplelesk_answer.append(answer)
        print "Sense :", answer
        print eachword+":"+answer.definition()+"\n"
    else:
        print eachword+": "+eachword+"\n"    
        simplelesk_answer.append(eachword)
        
        
print "\nDisambiguating your sentence word by word using Adapted Lesk algorithm. Hold on. \n======================================================"

for eachword in words:
    if has_synset(eachword):
        answer = adapted_lesk(raw_sentence, eachword)
        adaptedlesk_answer.append(answer)
        print "Sense :", answer
        print eachword+":"+answer.definition()+"\n"
    else:
        print eachword+": "+eachword+"\n"
        adaptedlesk_answer.append(eachword)
        
        
print "\nDisambiguating your sentence word by word using Cosine Lesk algorithm. Hold on. \n======================================================"

for eachword in words:
    if has_synset(eachword):
        answer = cosine_lesk(raw_sentence, eachword)
        cosinelesk_answer.append(answer)
        print "Sense :", answer
        print eachword+":"+answer.definition()+"\n"
    else:
        print eachword+": "+eachword+"\n"
        cosinelesk_answer.append(eachword)
        
print "Word Definition Comparison\n====================================\n"
    
for i in range(len(simplelesk_answer)):  # assuming the lists are of the same length
    print "\n============================================================"
    print "\nWord being compared is: "+words[i]
    if simplelesk_answer[i]==adaptedlesk_answer[i]==cosinelesk_answer[i]:
        print "\nSame definition in all algorithms."
    
    elif simplelesk_answer[i]==adaptedlesk_answer[i] and \
         simplelesk_answer[i]!=cosinelesk_answer[i]:
            print "\nSimple and Adapted Lesk Definition: "+simplelesk_answer[i].definition()
            print "\nCosine Lesk Definition: "+cosinelesk_answer[i].definition()
    
    elif simplelesk_answer[i]==cosinelesk_answer[i] and \
         simplelesk_answer[i]!=adaptedlesk_answer[i]:
            print "\nSimple and Cosine Lesk Definition: "+simplelesk_answer[i].definition()
            print "\nAdapted Lesk Definition: "+cosinelesk_answer[i].definition()
        
    elif adaptedlesk_answer[i]==cosinelesk_answer[i] and \
         adapatedlesk!=simplelesk_answer[i]:
            print "\nAdapted and Cosine Lesk Definition: "+adapted_answer[i].definition()
            print "\nSimple Lesk Definition: "+simplelesk_answer[i].definition()
    
    elif simplelesk_answer[i]!=adaptedlesk_answer[i]!=cosinelesk_answer[i]:
        print "\nSimple Lesk Definition: "+simplelesk_answer[i].definition()
        print "\nAdapted Lesk Definition: "+adaptedlesk_answer[i].definition()
        print "\nCosine Lesk Definition: "+cosinelesk_answer[i].definition()
        print

        
