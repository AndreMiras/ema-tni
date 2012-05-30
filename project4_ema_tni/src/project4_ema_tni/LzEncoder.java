/*
 * TODO:
 * Perhaps we could keep utf-8/iso-8859 reserved codes but override nonused ones
 * with ngrams dictionary that we would store in the header.
 * 0x26, 0x56
 */
package project4_ema_tni;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map.Entry;
import java.util.NavigableSet;

/**
 *
 * @author andre
 */
public class LzEncoder
{
    private String text;
    private ArrayList<Byte> encodedText = new ArrayList<Byte>();

    /*
     * contains the new encoded charmap
     * ngram and char to be encoded/decoded are already ordered by code values
     * e.g.:
     *  - encodedCharMap[0] has the code 0
     *  - encodedCharMap[3] has the code 3
     */
    private ArrayList<String> encodedCharMap = new ArrayList<String>();

    public LzEncoder(String text)
    {
        this.text = text;
        createEncodedCharMap();
    }

    public ArrayList<String> getEncodedCharMap()
    {
        if(encodedCharMap.isEmpty())
        {
            createEncodedCharMap();
        }

        return encodedCharMap;
    }

    private void encodeText()
    {
        int step = 2; // FIXME: hardcoded
        int i = 0;
        Integer code;
        // char char1 = text.substring(0, 1);
        char char1 = text.charAt(0);
        char char2 = text.charAt(1);
        String charControl =
                new StringBuilder().append("").append(char1).append(char2).toString();

        while (i < text.length() - 1)
        {
            // verify we can find the digram
            if(encodedCharMap.contains(charControl))
            {
                code = encodedCharMap.indexOf(charControl);
                encodedText.add(code.byteValue()); // FIXME: unichr
                char1 = text.charAt(i);
                char2 = text.charAt(i+1);
                charControl =
                    new StringBuilder().append("").append(char1).append(char2).toString();
                i += step;
            }
            // otherwize get the monogram
            else
            {
                char1 = text.charAt(i);
                charControl =
                        new StringBuilder().append("").append(char1).toString();
                code = encodedCharMap.indexOf(charControl);
                encodedText.add(code.byteValue()); // FIXME: use unichr

                // preparing next iteration with next char couple
                char1 = text.charAt(i+1);
                char2 = text.charAt(i+2);
                charControl =
                    new StringBuilder().append("").append(char1).append(char2).toString();
                i++;
            }
        }
    }

    public ArrayList<Byte> getEncodedText()
    {
        if (encodedText.isEmpty())
        {
            encodeText();
        }

        return encodedText;
    }

    private void createEncodedCharMap()
    {
        // TODO
        // 256 values
        // get anything that's not in the ngram dic and add it to the
        // reserved byte
        // 256 - number_of_uniq_char

        // used to get the number of uniq char
        LzDictionary lzDictionary1 = new LzDictionary(text, 1);
        NavigableSet<Entry<String, Integer>> sortedCharCountDict =
                lzDictionary1.getNGramCountDictSorted();
        int number_of_uniq_char = sortedCharCountDict.size();

        // get the uniq digram sorted dictionary
        LzDictionary lzDictionary2 = new LzDictionary(text, 2);
        NavigableSet<Entry<String, Integer>> nGramCountDictSorted =
                lzDictionary2.getNGramCountDictSorted();

        ArrayList<String> nGramArraySortedByCount =
                lzDictionary2.getNGramArraySortedByCount();

        HashMap<String, Integer> encodingTable; // ??
        ArrayList<String> uniqCharArraySortedByCount =
                lzDictionary1.getNGramArraySortedByCount();

        // adding uniq char to the dic
        for (int i=0; i<number_of_uniq_char; i++)
        {
            encodedCharMap.add(uniqCharArraySortedByCount.get(i));
        }

        // using left slot to add ngrams
        int i = 1;
        String aChar = nGramArraySortedByCount.get(0);
        /*
         * FIXME:
         *  - aChar.isEmpty() this condition should really be something else
         *  - 255 or 256, to be verified
         */
        while((!aChar.isEmpty()) && (encodedCharMap.size() < 255))
        {
            aChar = nGramArraySortedByCount.get(i);
            encodedCharMap.add(aChar);
            i++;
        }
    }
}
