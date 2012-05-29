/*
 * TODO:
 * Perhaps we could keep utf-8/iso-8859 reserved codes but override nonused ones
 * with ngrams dictionary that we would store in the header.
 */
package project4_ema_tni;

import java.util.HashMap;
import java.util.Map.Entry;
import java.util.SortedSet;

/**
 *
 * @author andre
 */
public class LzEncoder
{
    private String text;

    /*
     * contains the new encoded charmap
     * ngram and char to be encoded/decoded are already ordered by code values
     * e.g.:
     *  - encodedCharMap[0] has the code 0
     *  - encodedCharMap[3] has the code 3
     */
    private String[] encodedCharMap = new String[256];

    public LzEncoder(String text)
    {
        this.text = text;
        encode();
    }

    private void encode()
    {
        // TODO
        // 256 values
        // get anything that's not in the ngram dic and add it to the
        // reserved byte
        // 256 - number_of_uniq_char

        // used to get the number of uniq char
        LzDictionary lzDictionary1 = new LzDictionary(text, 1);
        SortedSet<Entry<String, Integer>> sortedCharCountDict =
                lzDictionary1.getNGramCountDictSorted();
        int number_of_uniq_char = sortedCharCountDict.size();

        // get the uniq digram sorted dictionary
        LzDictionary lzDictionary2 = new LzDictionary(text, 2);
        SortedSet<Entry<String, Integer>> nGramCountDictSorted =
                lzDictionary2.getNGramCountDictSorted();
        HashMap<String, Integer> encodingTable;

        /*
        for (int i=0; i<number_of_uniq_char; i++)
        {
        }
        */
    }
}
