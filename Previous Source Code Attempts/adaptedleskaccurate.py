from pywsd.lesk import adapted_lesk
raw_sentence=raw_input("Please enter your sentence : ")
raw_word=raw_input("Please enter input word :")

print "#TESTING adapted_lesk() with pos, stem, nbest and scores."
print "Context:", raw_sentence
answer = adapted_lesk(raw_sentence[0],raw_word,'n', True, \
                     nbest=True, keepscore=True)
print "Senses ranked by #overlaps:", answer
best_sense = answer[0][1]
try: definition = best_sense.definition() 
except: definition = best_sense.definition
print "Definition:", definition