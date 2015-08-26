from pywsd import disambiguate
from nltk import sent_tokenize
text = "Python is a widely used general-purpose, high-level programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java. The language provides constructs intended to enable clear programs on both a small and large scale. Python supports multiple programming paradigms, including object-oriented, imperative and functional programming or procedural styles."
for sent in sent_tokenize(text):
    print disambiguate(sent, prefersNone=True)
