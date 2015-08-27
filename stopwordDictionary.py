import csv
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')


with open('haveNoSense.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=':')
    for row in reader:
        if word == row[0]: # if the word shall be on column 1 (-> index 0)
            print "Found!"
            print ' : '.join(row)
            break;
        else:
            print "Not Found"