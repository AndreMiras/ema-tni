#!/usr/bin/env python2
"""
TNI script
"""

import codecs
import optparse


# globals
# selected_encoding = "utf-8"
selected_encoding="iso-8859-1"

def decoding_text(encoded_char_map, ngram_max_size, coded_full_file):
    count = 0
    char = coded_full_file[count:count+1]
    decoded_full_file = ""
    while char:
        tampon = encoded_char_map[ord(char)]
        decoded_full_file += tampon
        count += 1
        char = coded_full_file[count:count+1]
    return decoded_full_file

def encoding_text(encoded_char_map, full_file, ngram_max_size):
    coded_full_file = ""
    char_count = 0
    # char_control = f.read(ngram_max_size)
    char_control = full_file[char_count:ngram_max_size+char_count]
    while char_control:
        if char_control in encoded_char_map:
            tampon = encoded_char_map.index(char_control)
            encoding_tampon = unichr(tampon)
            coded_full_file += encoding_tampon
            char_count += ngram_max_size
            char_control = full_file[char_count:ngram_max_size+char_count]
        else:
             compter = ngram_max_size
             tmp_char = char_control
             while not (tmp_char in encoded_char_map):
                 tmp_char = char_control[:compter]
                 compter -= 1
             tampon = encoded_char_map.index(tmp_char)
             encoding_tampon = unichr(tampon)
             coded_full_file += encoding_tampon
             char_count += len(tmp_char)
             char_control = full_file[char_count:char_count+ngram_max_size]
    return coded_full_file

def create_encoded_char_map(uniq_char_list, n_gram_to_encode):
    """
    (u'e qu', {'occurrences': 17, 'weigth': 68})
    but should be occurrences 51

    >>> input_file_name = "../exemple1.txt"
    >>> output_file_name = "output.txt"
    >>> decoded_file_name = "decoded1.txt"
    >>> ngram_max_size = 4

    >>> f = codecs.open(input_file_name, "r", encoding=selected_encoding)
    >>> full_file = f.read()
    >>> f.close()
    >>> uniq_char_list = n_gram(1, full_file)
    >>> all_ngrams = generate_all_ngrams_to_ngram_max_size(ngram_max_size, full_file)
    >>> all_ngrams = add_ngram_weigth(all_ngrams)
    >>> sorted_ngrams = sort_digram_by_weight(all_ngrams)

    >>> encoded_char_map = create_encoded_char_map(uniq_char_list, sorted_ngrams)
    >>> len(encoded_char_map)
    255
    >>> encoded_char_map[:10]
    [u'\\x80', u'\\x89', u'\\n', u'C', u'\\x93', u'\\xc2', u'\\x99', u'R', u'\\xae', u'!']

    >>> encoded_char_map[245:]
    [u'\\x80\\x99a', u'ais', u' fa', u'ma', u'ui', u'omm', u'ont ', u'l ', u' qui', u'out']
    """
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

def n_gram(n_gram_size, full_file):
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

    >>> input_file_name = "../exemple1.txt"
    >>> f = codecs.open(input_file_name, "r", encoding=selected_encoding)
    >>> full_file = f.read()
    >>> f.close()

    >>> ngrams = n_gram(3, full_file)
    >>> len(ngrams)
    2893
    >>> "foo" in ngrams
    False
    >>> ngrams["bar"]["occurrences"]
    3

    >>> ngrams = n_gram(4, full_file)
    >>> len(ngrams)
    6992

    >>> ngrams["les "]["occurrences"]
    134
    >>> ngrams["e qu"]["occurrences"]
    51
    >>> ngrams["les "]["occurrences"]
    134
    """
    # prob n-gram
    # print("=================================" + str(n_gram_size) + "-grammes=================================")
    f = codecs.open(file_name, "r+", encoding=selected_encoding)
    char_count = 0

    alphabet = {}
    chaine = full_file[char_count:n_gram_size+char_count]
    char_count += 1
    while chaine:
        if chaine not in alphabet:
            alphabet.update(
            {
                chaine:
                {
                    "occurrences": 0,
                    "weigth": 0,
                }
            })
        alphabet[chaine]["occurrences"] += 1
        chaine = full_file[char_count:n_gram_size+char_count]
        char_count += 1
    return alphabet

def sort_digram_by_weight(all_ngrams):
    """
    Sorts all_ngrams by weigth.
    """
    dict_to_list = [x for x in all_ngrams.iteritems()]
    dict_to_list.sort(key=lambda x: x[1]["weigth"])
    dict_to_list.reverse()
    return dict_to_list

def generate_all_ngrams_to_ngram_max_size(ngram_max_size, full_file):
    """
    Put all ngrams from 2 to ngram_max_size in the same object
    to be later sorted (with sort_digram_by_weight).
    """
    all_ngrams = {}
    for i in range(2, ngram_max_size+1):
        ngrams = n_gram(i, full_file)
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
    """
    >>> import hashlib
    >>> input_file_name = "../exemple1.txt"
    >>> output_file_name = "output.txt"
    >>> decoded_file_name = "decoded1.txt"
    >>> f = open(input_file_name)
    >>> hashlib.sha1(f.read()).hexdigest()
    '07a96a90b53a8ccaa589b6671d527d20b859469a'
    >>> f.close()
    >>> run(4, input_file_name, output_file_name)

    After running encoding and decoding the hash should be the same
    >>> f = open(decoded_file_name)
    >>> hashlib.sha1(f.read()).hexdigest()
    '07a96a90b53a8ccaa589b6671d527d20b859469a'
    >>> f.close()
    """
    f = codecs.open(file_name, "r", encoding=selected_encoding)
    full_file = f.read()
    f.close()
    uniq_char_list = n_gram(1, full_file)
    all_ngrams = generate_all_ngrams_to_ngram_max_size(ngram_max_size, full_file)
    all_ngrams = add_ngram_weigth(all_ngrams)
    sorted_ngrams = sort_digram_by_weight(all_ngrams)

    encoded_char_map = create_encoded_char_map(uniq_char_list, sorted_ngrams)
    coded_full_file = encoding_text(encoded_char_map, file_name, ngram_max_size)
    f4 = codecs.open(output_file, "w", encoding=selected_encoding)
    f4.write(coded_full_file)

    f2 = codecs.open(output_file, "r", encoding=selected_encoding)
    coded_full_file = f2.read()
    f2.close()

    decoded_full_file = decoding_text(encoded_char_map, ngram_max_size, coded_full_file)
    f3 = codecs.open(decoded_file, "w", encoding=selected_encoding)
    f3.write(decoded_full_file)
    f3.close()

def _test():
    import doctest
    doctest.testmod()

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
    parser.add_option("-t", action="store_true", dest="test",
                      help="run tests")

    (options, args) = parser.parse_args()
    file_name = options.filename
    ngram_max_size = options.ngram_max_size
    output_file = options.output
    decoded_file = options.decoded
    if options.test:
        _test()
    else:
        run(ngram_max_size, file_name, output_file)
