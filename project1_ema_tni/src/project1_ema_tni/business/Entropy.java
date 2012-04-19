/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package project1_ema_tni.business;

import java.util.HashMap;

/**
 *
 * @author andre
 */
public class Entropy
{
    private String text;
    private HashMap<Character, Integer> alphabetCountDict =
            new HashMap<Character, Integer>();
    private HashMap<Character, Float> alphabetProbaDict =
            new HashMap<Character, Float>();

    public Entropy(String text)
    {
        this.text = text;
        computeAlphabetCountDict();
    }

    private void computeAlphabetCountDict()
    {
        Character symbol;
        Integer count = 0;
        for (int i = 0; i < text.length(); i++)
        {
            symbol = text.charAt(i);
            count = alphabetCountDict.get(symbol);
            if(count == null) // if the doesn't symbol exist in the lookup table
            {
                count = 0;
            }
            count++;
            alphabetCountDict.put(symbol, count);
        }
    }

    private void computeAlphabetProbaDict()
    {
        getAlphabetCountDict(); // generates alphabet count if empty
        int count;
        float proba;
        int total = text.length();

        for (Character symbol : alphabetCountDict.keySet())
        {
            count = alphabetCountDict.get(symbol);
            proba = (float)count / (float)total;
            alphabetProbaDict.put(symbol, proba);
        }
    }

    public float getTextEntropy()
    {
        float probaSymbol;
        float entropy = 0;
        getAlphabetProbaDict(); // generates alphabet proba if empty

        for(Character symbol : alphabetProbaDict.keySet())
        {
            probaSymbol = alphabetProbaDict.get(symbol);
            entropy -= probaSymbol * Math.log(probaSymbol)/Math.log(2);
        }
        return entropy;
    }

    /**
     * Generates and returns alphabet count
     * @return alphabet count
     */
    public HashMap<Character, Integer> getAlphabetCountDict()
    {
        if (alphabetCountDict.isEmpty())
        {
            computeAlphabetCountDict();
        }

        return alphabetCountDict;
    }

    /**
     * Generates and returns alphabet proba
     * @return alphabet proba
     */
    public HashMap<Character, Float> getAlphabetProbaDict()
    {
        if (alphabetProbaDict.isEmpty())
        {
            computeAlphabetProbaDict();
        }

        return alphabetProbaDict;
    }
}
