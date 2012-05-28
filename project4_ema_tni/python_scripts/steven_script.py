#!/usr/bin/env python2
import math
import codecs
import optparse
import operator
from decimal import Decimal


file_name = ""

if __name__=="__main__":
    parser = optparse.OptionParser("usage: %prog --filename exemple1.txt")
    parser.add_option("-f", "--filename", dest="filename",
                      default="exemple1.txt", type="string",
                      help="file name to parse")

    (options, args) = parser.parse_args()
    file_name = options.filename

# trouver l'entropie (nombre de bits par symboles)

# selected_encoding = "utf-8"
selected_encoding="iso-8859-1"
f = codecs.open(file_name, "r", encoding=selected_encoding)
char_count = 0

alphabet = {}
char = str(f.read(1)) # .lower()
while char:
    char2 = f.read(1)
    chaine = char + char2
    if chaine not in alphabet:
        alphabet.update({chaine:0})
    alphabet[chaine] += 1
    char_count += 2
    print(str(char_count))
    char = f.read(1) # .lower()
f.close()

print(str(char_count))

# prob digramme
print("=================================DIGRAMMES=================================")
probcharinit = 0
for lettre in alphabet:
    nb_occ_char = alphabet[lettre]
    prob_char = nb_occ_char / float(char_count)
   # print(str(lettre) + ":" + str(prob_char))
    if prob_char > probcharinit :
        moreLettre = lettre
        probcharinit = prob_char
print(str(moreLettre) + " : " + str(probcharinit))

sorted_alphabet = sorted(alphabet.iteritems(), key=operator.itemgetter(1))
sorted_alphabet.reverse()
compteur = 0
for lettre in sorted_alphabet:
    print(str(lettre))
    
    # prob trigrammes
print("=================================TRIGRAMMES=================================")
f = open(file_name)
char_count = 0

alphabet2 = {}
char = str(f.read(1)) # .lower()
while char:
    char2 = f.read(1)
    char3 = f.read(1)
    chaine = str(char) + str(char2) + str(char3) 
    if chaine not in alphabet2:
        alphabet2.update({chaine:0})
    alphabet2[chaine] += 1
    char_count += 1
    char = f.read(1) # .lower()
f.close()

probcharinit = 0
for lettre in alphabet2:
    nb_occ_char = alphabet2[lettre]
    prob_char = nb_occ_char / float(char_count)
   # print(str(lettre) + ":" + str(prob_char))
    if prob_char > probcharinit :
        moreLettre = lettre
        probcharinit = prob_char
print(str(moreLettre) + " : " + str(probcharinit))

sorted_alphabet2 = sorted(alphabet2.iteritems(), key=operator.itemgetter(1))
# sorted_alphabet.reverse()
for lettre in sorted_alphabet2:
    print(str(lettre))

# prob quadrigrammes
print("=================================QUADRIGRAMMES=================================")
f = open(file_name)
char_count = 0

alphabet3 = {}
char = str(f.read(1)) # .lower()
while char:
    char2 = f.read(1)
    char3 = f.read(1)
    char4 = f.read(1)
    chaine = str(char) + str(char2) + str(char3) + str(char4)
    if chaine not in alphabet3:
        alphabet3.update({chaine:0})
    alphabet3[chaine] += 1
    char_count += 1
    char = f.read(1) # .lower()
f.close()
probcharinit = 0
for lettre in alphabet3:
    nb_occ_char = alphabet3[lettre]
    prob_char = nb_occ_char / float(char_count)
   # print(str(lettre) + ":" + str(prob_char))
    if prob_char > probcharinit :
        moreLettre = lettre
        probcharinit = prob_char
print(str(moreLettre) + " : " + str(probcharinit))

sorted_alphabet3 = sorted(alphabet3.iteritems(), key=operator.itemgetter(1))
# sorted_alphabet.reverse()
for lettre in sorted_alphabet3:
    print(str(lettre))
