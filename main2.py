
# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')



import nltk
import csv

import matplotlib.pyplot as plt
plt.figure(figsize=(8, 5))  # the size you wan

from nltk.corpus import gutenberg
print(nltk.corpus.gutenberg.fileids())


print('pic a0')

f    = open("g76.txt","rb")
inputfile = f.read().decode(errors='replace')

print('pic a1')

tokens = nltk.tokenize.word_tokenize(inputfile)


fd = nltk.FreqDist(tokens)

print('pic a2 ')
fd.most_common(100)

print('pic a3')
print(fd.most_common(100))

print('pic a4')

fd.plot(20, cumulative=False)


print('pic 2')

fd.plot(20, cumulative=True)

from nltk import FreqDist
import csv



with open("0023_word_frequency.csv", "wb") as fp:
    writer = csv.writer(fp, quoting=csv.QUOTE_ALL)
    writer.writerows(fd.most_common(5000000))
