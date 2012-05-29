/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package project4_ema_tni;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.nio.MappedByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.charset.Charset;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.SortedSet;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author andre
 */
public class Main
{
    private static String filePath = "";
    private static String fileName = "exemple1.txt";

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args)
    {
        String text;
        String fullPath = filePath + fileName;
        try
        {
            text = Helper.readFile(fullPath);
        } catch (IOException ex)
        {
            Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
            return;
        }
        LzDictionary lzDictionary = new LzDictionary(text);

        System.out.println("\nChar Count: " + text.length());
        /*
        System.out.println("\nCount:");
        HashMap<String, Integer> alphabetCountDict =
                lzDictionary.getNGramCountDict();
        printKeysValuesDict(alphabetCountDict);
         */

        System.out.println("\nSorted Count:");
        SortedSet<Map.Entry<String, Integer>> nGramSortedCountDict =
                lzDictionary.getNGramCountDictSorted();
        Helper.printKeysValuesDict(nGramSortedCountDict);
        /*
        System.out.println("\nProba:");
        HashMap<Character, Float> alphabetProbaDict =
                entropyObj.getAlphabetProbaDict();
        printKeysValuesDict(alphabetProbaDict);

        System.out.println("\nEntropy:");
        float textEntropy = entropyObj.getTextEntropy();
        System.out.println(textEntropy);
         */
        LzEncoder lzEncoder = new LzEncoder(text);
    }    
}
