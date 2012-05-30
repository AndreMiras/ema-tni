#!/usr/bin/env python2
import math
import codecs
import optparse
import operator
from decimal import Decimal


# globals
# selected_encoding = "utf-8"
selected_encoding="iso-8859-1"

def decoding_text(encoded_char_map, n_gram_max_size, output_file, decoded_file):
    f = codecs.open(output_file, "r", encoding=selected_encoding)
    f2 = codecs.open(decoded_file, "w", encoding=selected_encoding)
    char = f.read(1)
    while char:
        tampon = encoded_char_map[ord(char)]
        f2.write(tampon)
        char = f.read(1)
    f2.close()

def encoding_text(encoded_char_map, file_name, n_gram_max_size, output_file):
    f = codecs.open(file_name, "r", encoding=selected_encoding)
    f2 = codecs.open(output_file, "w", encoding=selected_encoding)
    char_control = f.read(n_gram_max_size)
    # import ipdb; ipdb.set_trace()
    while char_control:
        compteur = 0
        if char_control in encoded_char_map:
            tampon = encoded_char_map.index(char_control)
            encoding_tampon = unichr(tampon)
            f2.write(encoding_tampon)
            char_control = f.read(n_gram_max_size)
        else:
             while compteur < n_gram_max_size:
                 compteur += 1
                 tmp_char = char_control[:compteur]
                 if tmp_char in encoded_char_map:
                     tampon = encoded_char_map.index(tmp_char)
                     encoding_tampon = unichr(tampon)
                     f2.write(encoding_tampon)
                     char_control = char_control[compteur:] + f.read(compteur)
                     compteur = n_gram_max_size
                 else:
                     char_control = char_control[compteur:] + f.read(n_gram_max_size-compteur)
                     compteur = n_gram_max_size
    f.close()
    f2.close()

def create_encoded_char_map(uniq_char_list, n_gram_to_encode):
    encoded_char_map = []
    for couple in uniq_char_list:
        char = couple[0]
        encoded_char_map.append(char)
    count = 1
    couple = n_gram_to_encode[0]
    char = couple[0]
    while (char and (len(encoded_char_map) < 255)):
        encoded_char_map.append(char)
        couple = n_gram_to_encode[count]
        char = couple[0]
        count += 1
    return encoded_char_map

def n_gram(n_gram_size, file_name):
    """
    alphabet
    {
        "a": {"occurences":0, "weigth":0}
        "b": {"occurences":0, "weigth":0}
    }
    """
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
            # alphabet.update({chaine:{"occurences":0, "weigth": 0}})
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
    sorted_alphabet = list(sorted(alphabet.iteritems(), key=operator.itemgetter(1)))
    sorted_alphabet.reverse()
    # for lettre in sorted_alphabet:
    #     print(str(sorted_alphabet.index(lettre)))
    return sorted_alphabet

def run(n_gram_max_size, file_name, output_file):
    sorted_alphabets = []
    uniq_char_list = n_gram(1, file_name)
    sorted_digrams = n_gram(n_gram_max_size, file_name)
    encoded_char_map = []
    encoded_char_map = create_encoded_char_map(uniq_char_list, sorted_digrams)
    encoding_text(encoded_char_map, file_name, n_gram_max_size, output_file)
    decoding_text(encoded_char_map, n_gram_max_size, output_file, decoded_file)
    """
    for i in range(1, n_gram_max_size+1):
        sorted_alphabet = n_gram(i, file_name)
        sorted_alphabets.append(sorted_alphabet)
    """

if __name__=="__main__":
    parser = optparse.OptionParser("usage: %prog --filename exemple1.txt")
    parser.add_option("-f", "--filename", dest="filename",
                      default="exemple1.txt", type="string",
                      help="file name to parse")
    parser.add_option("-n", "--ngram", dest="n_gram_max_size",
                      default="4", type="int",
                      help="passing n-gram max size as param")
    parser.add_option("-o", "--output", dest="output",
                      default="test1.txt", type="string",
                      help="output file name")
    parser.add_option("-d", "--decoded", dest="decoded",
                      default="decoded1.txt", type="string",
                      help="decoded file name")

    (options, args) = parser.parse_args()
    file_name = options.filename
    n_gram_max_size = options.n_gram_max_size
    output_file = options.output
    decoded_file = options.decoded

    run(n_gram_max_size, file_name, output_file)
