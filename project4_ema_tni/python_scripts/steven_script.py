#!/usr/bin/env python
import math
import operator
from decimal import Decimal

# trouver l'entropie (nombre de bits par symboles)

# file_name = "/etc/passwd"
# file_name = "/home/andre/Downloads/exemple1.txt"
file_name = "/Users/Steven/Documents/EMA/TNI/exemple1.txt"
f = open(file_name)
char_count = 0

alphabet = {}
char = str(f.read(1)) # .lower()
while char:
    char2 = f.read(1)
    chaine = str(char) + str(char2) 
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
