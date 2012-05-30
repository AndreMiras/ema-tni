#!/usr/bin/env python2
"""
TODO:
    - code cleaning
"""

import math
import codecs
import optparse
import operator
from decimal import Decimal


# globals
# selected_encoding = "utf-8"
selected_encoding="iso-8859-1"

def decoding_text(encoded_char_map, ngram_max_size, output_file, decoded_file):
    f = codecs.open(output_file, "r", encoding=selected_encoding)
    f2 = codecs.open(decoded_file, "w", encoding=selected_encoding)
    char = f.read(1)
    while char:
        tampon = encoded_char_map[ord(char)]
        f2.write(tampon)
        char = f.read(1)
    f2.close()

def encoding_text(encoded_char_map, file_name, ngram_max_size, output_file):
    f = codecs.open(file_name, "r", encoding=selected_encoding)
    f2 = codecs.open(output_file, "w", encoding=selected_encoding)
    char_control = f.read(ngram_max_size)
    while char_control:
        compteur = 0
        if char_control in encoded_char_map:
            tampon = encoded_char_map.index(char_control)
            encoding_tampon = unichr(tampon)
            f2.write(encoding_tampon)
            char_control = f.read(ngram_max_size)
        else:
             while compteur < ngram_max_size:
                 compteur += 1
                 tmp_char = char_control[:compteur]
                 if tmp_char in encoded_char_map:
                     tampon = encoded_char_map.index(tmp_char)
                     encoding_tampon = unichr(tampon)
                     f2.write(encoding_tampon)
                     char_control = char_control[compteur:] + f.read(compteur)
                     compteur = ngram_max_size
                 else:
                     char_control = char_control[compteur:] + f.read(ngram_max_size-compteur)
                     compteur = ngram_max_size
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
    import pdb; pdb.set_trace()
    return encoded_char_map

def n_gram(n_gram_size, file_name):
    """
    Count ngrams occurrences.
    alphabet
    {
        "a": {"occurrences":0, "weigth":0}
        "b": {"occurrences":0, "weigth":0}
    }
    occurrences: number of ngrams counted
    weigth: the weigth given to this ngram computed from the following formula:
        weigth = ngram-size * occurrences
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
            # alphabet.update({chaine:0})
            alphabet.update(
            {
                chaine:
                {
                    "occurrences": 0,
                    "weigth": 0,
                }
            })
        alphabet[chaine]["occurrences"] += 1
        char_count += 1
        char = f.read(1) # .lower()
        chaine = char
    f.close()
    return alphabet

def sort_digram_by_weight(all_ngrams):
    """
    Sorts all_ngrams by weigth.
    """
    dict_to_list = [x for x in all_ngrams.iteritems()]
    dict_to_list.sort(key=lambda x: x[1]["weigth"])
    dict_to_list.reverse()
    import pdb; pdb.set_trace()
    return dict_to_list

def generate_all_ngrams_to_ngram_max_size(ngram_max_size, file_name):
    """
    Put all ngrams from 2 to ngram_max_size in the same object
    to be later sorted (with sort_digram_by_weight).
    """
    all_ngrams = {}
    for i in range(2, ngram_max_size+1):
        ngrams = n_gram(i, file_name)
        all_ngrams.update(ngrams)
    return all_ngrams

def add_ngram_weigth(all_ngrams):
    """
    weigth: the weigth given to this ngram computed from the following formula:
        weigth = ngram-size * occurrences
    """
    for ngram in all_ngrams:
        all_ngrams[ngram]["weigth"] = len(ngram) * all_ngrams[ngram]["occurrences"]
    return all_ngrams

def run(ngram_max_size, file_name, output_file):
    sorted_alphabets = []
    uniq_char_list = n_gram(1, file_name)
    all_ngrams = generate_all_ngrams_to_ngram_max_size(ngram_max_size, file_name)
    all_ngrams = add_ngram_weigth(all_ngrams)
    sorted_ngrams = sort_digram_by_weight(all_ngrams)

    encoded_char_map = create_encoded_char_map(uniq_char_list, sorted_ngrams)
    encoding_text(encoded_char_map, file_name, ngram_max_size, output_file)
    decoding_text(encoded_char_map, ngram_max_size, output_file, decoded_file)

if __name__=="__main__":
    parser = optparse.OptionParser("usage: %prog --filename exemple1.txt")
    parser.add_option("-f", "--filename", dest="filename",
                      default="exemple1.txt", type="string",
                      help="file name to parse")
    parser.add_option("-n", "--ngram", dest="ngram_max_size",
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
    ngram_max_size = options.ngram_max_size
    output_file = options.output
    decoded_file = options.decoded

    run(ngram_max_size, file_name, output_file)
