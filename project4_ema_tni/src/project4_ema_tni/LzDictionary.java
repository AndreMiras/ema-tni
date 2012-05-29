/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package project4_ema_tni;

import java.util.*;

/**
 *
 * @author andre
 */
public class LzDictionary
{
    private static final int DEFAULT_NGRAM_DICTIONARY_SIZE = 256;
    private static final int DEFAULT_NGRAM_SIZE = 2; // digram is the default

    private String text;
    /*
     * nGramSize =
     *  - 2 for digram
     *  - 3 for trigram
     */
    private int nGramSize;
    /*
     * Keeping only the nGramDictionarySize nGrams with the highest count
     */
    private int nGramDictionarySize;
    private HashMap<String, Integer> nGramCountDict =
            new HashMap<String, Integer>();
    private HashMap<String, Float> nGramProbaDict =
            new HashMap<String, Float>();

    public LzDictionary(String text)
    {
        this(text, DEFAULT_NGRAM_SIZE, DEFAULT_NGRAM_DICTIONARY_SIZE);
    }

    public LzDictionary(String text, int nGramSize)
    {
        this(text, nGramSize, DEFAULT_NGRAM_DICTIONARY_SIZE);
    }

    public LzDictionary(String text, int nGramSize, int nGramDictionarySize)
    {
        this.text = text;
        this.nGramSize = nGramSize;
        this.nGramDictionarySize = nGramDictionarySize;
    }

    private void computeNGramCountDict()
    {
        String nGram;
        Integer count;

        // TODO: race condition check
        for (int i = 0; i < text.length()-nGramSize; i += nGramSize)
        {
            nGram = text.substring(i, i+nGramSize);
            count = nGramCountDict.get(nGram);
            if(count == null) // if the doesn't symbol exist in the lookup table
            {
                count = 0;
            }
            count++;
            nGramCountDict.put(nGram, count);
        }
    }

    /**
     * Generates and returns nGram count
     * @return alphabet count
     */
    public HashMap<String, Integer> getNGramCountDict()
    {
        if (nGramCountDict.isEmpty())
        {
            computeNGramCountDict();
        }

        return nGramCountDict;
    }

    public NavigableSet<Map.Entry<String, Integer>> getNGramCountDictSorted()
    {
        return entriesSortedByValues(getNGramCountDict());
    }

    public ArrayList<String> getNGramArraySortedByCount()
    {
        ArrayList<String> nGramArraySortedByCount = new ArrayList<String>();
        NavigableSet<Map.Entry<String, Integer>> nGramCountDictSorted =
                getNGramCountDictSorted();
        // Iterator iterator = nGramCountDictSorted.iterator();
        Iterator<Map.Entry<String, Integer>> iterator = nGramCountDictSorted.descendingIterator();
        String key;
        //Ascending order list
        while (iterator.hasNext())
        {
            key = iterator.next().getKey();
            nGramArraySortedByCount.add(key);
        }

        return nGramArraySortedByCount;
    }

    static <K, V extends Comparable<? super V>>
            NavigableSet<Map.Entry<K, V>> entriesSortedByValues(Map<K, V> map)
    {
        NavigableSet<Map.Entry<K, V>> sortedEntries = new TreeSet<Map.Entry<K, V>>(
                new Comparator<Map.Entry<K, V>>()
                {

                    @Override
                    public int compare(Map.Entry<K, V> e1, Map.Entry<K, V> e2)
                    {
                        int res = e1.getValue().compareTo(e2.getValue());
                        // Special fix to preserve items with equal values
                        return res != 0 ? res : 1;
                    }
                });
        sortedEntries.addAll(map.entrySet());
        return sortedEntries;
    }
}
