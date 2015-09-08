# ReWordTool
Tool built using Python's NLTK to preprocess a sentence and deliver results using the Lesk algorithm.

Screenshot :

![alt tag](http://i.imgur.com/isCybmN.png)

# PREPROCESSING #
## Don't process ##
* Proper nouns
* Pronouns [Done]
* Single/double letters words
* Misspelt Words [Done]

## Work Flow ##

* misspelt [Don't process Proper nouns]
* stopword: Get definition from StopWords dictionary

## Stopwords [Done] ##
* Read stopwords and create dictionary
* Check if stopword is there in dictionary
* Load definition from dictionary


# DIFFERENCES #
## Process ##

* Get all three sense-sets - simple, adapted and cosine.
* Make sure at least two of them have 0+ senses.
  (If not, then no need to compare)
* Compare all senses.
    If they are all equal
        show "No differences"
    else
        show the differences.
