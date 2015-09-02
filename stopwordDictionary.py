import csv
# import sys

#  reload(sys)
#  sys.setdefaultencoding('utf8')  # seems redundant as of now.


class StopWordDictionary:

    reader = csv_file = None

    def __init__(self):  # Constructor
        print "Initializing Stop word dictionary..."
        self.csv_file = open('StopwordDefinitions.csv')  # Open the file
        self.reader = csv.reader(self.csv_file, delimiter=':')  # Create _csv.reader object
        return

    def has_sense(self, word):  # Returns true if dictionary contains a definition
        word = word.lower()
        for row in self.reader:  # Iterate through each line
            if word == row[0]:  # If word matches key
                self.csv_file.seek(0)  # Reset file to start
                return True  # Definition found, return true
        return False  # Nothing found, return false

    def get_sense(self, word):  # Returns the definition of the word
        word = word.lower()
        for row in self.reader:  # Iterate through each line
            if word == row[0]:  # If word matches key
                self.csv_file.seek(0)  # Reset file to start
                return row[1]  # Return definition

    def __del__(self):  # Destruction
        self.reader = None
        self.csv_file.close()
        return

# USAGE EXAMPLE
# stDict = StopWordDictionary()

# if stDict.has_sense("myasdasdasd"):
#    print stDict.get_sense("myasdasdasdasd")
# else:
#    print "Nothing found!"