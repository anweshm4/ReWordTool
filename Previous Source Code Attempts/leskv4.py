from pywsd.lesk import simple_lesk
sent = ' The path leads us through.'
ambiguous = 'through'
answer = simple_lesk(sent, ambiguous)
print answer
print answer.definition()
