import urllib
import re

url = 'https://www.gutenberg.org/files/2600/2600-0.txt'
file = urllib.request.urlopen(url)

Words = []
word=[]
for line in file:
    decoded_line = line.decode("utf-8")
    for word in decoded_line.lower().split():
        if re.findall('\w+', word) and word not in Words:
            if not re.findall('[ixv]', word) or word == 'war' or word == 'and' or word == 'peace':
                Words.append(word)
print("The count of unique words in Tolstoy's war and peace are", len(Words))