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

def n_gram(n_gram_size):
    # prob n-gram
    print("=================================" + str(n_gram_size) + "-grammes=================================")
    # f = open(file_name)
    f = codecs.open(file_name, "r", encoding=selected_encoding)
    char_count = 0

    alphabet = {}
    char = f.read(1) # .lower()
    chaine = char
    while char:
        for i in range(1, n_gram_size):
            chaine += f.read(1)
        if chaine not in alphabet:
            alphabet.update({chaine:0})
        alphabet[chaine] += 1
        char_count += 1
        char = f.read(1) # .lower()
        chaine = char
    f.close()

    """
    probcharinit = 0
    for lettre in alphabet:
        nb_occ_char = alphabet[lettre]
        prob_char = nb_occ_char / float(char_count)
        print(str(lettre) + ":" + str(prob_char))
        if prob_char > probcharinit :
            moreLettre = lettre
            probcharinit = prob_char
    print(str(moreLettre) + " : " + str(probcharinit))
    """

    sorted_alphabet = sorted(alphabet.iteritems(), key=operator.itemgetter(1))
    # sorted_alphabet.reverse()
    for lettre in sorted_alphabet:
        print(str(lettre))


n_gram(2)

    # prob trigrammes
print("=================================TRIGRAMMES=================================")
n_gram(3)

# prob quadrigrammes
print("=================================QUADRIGRAMMES=================================")
n_gram(4)
