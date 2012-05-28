/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package project1_ema_tni.core;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.nio.MappedByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.charset.Charset;
import java.util.HashMap;
import java.util.logging.Level;
import java.util.logging.Logger;
import project1_ema_tni.business.Entropy;

/**
 *
 * @author andre
 */
public class Main
{

    private static String filePath = "";
    private static String fileName = "exemple1.txt";

    public static void main(String[] args)
    {
        String text;
        String fullPath = filePath + fileName;
        try
        {
            text = readFile(fullPath);
        } catch (IOException ex)
        {
            Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
            return;
        }
        Entropy entropyObj = new Entropy(text);

        System.out.println("\nChar Count:" + text.length());
        System.out.println("\nCount:");
        HashMap<Character, Integer> alphabetCountDict =
                entropyObj.getAlphabetCountDict();
        printKeysValuesDict(alphabetCountDict);

        System.out.println("\nProba:");
        HashMap<Character, Float> alphabetProbaDict =
                entropyObj.getAlphabetProbaDict();
        printKeysValuesDict(alphabetProbaDict);

        System.out.println("\nEntropy:");
        float textEntropy = entropyObj.getTextEntropy();
        System.out.println(textEntropy);
    }

    private static <K,V> void printKeysValuesDict(
            HashMap<K, V> alphabetCountDict)
    {
        V value;
        for(K key : alphabetCountDict.keySet())
        {
            value = alphabetCountDict.get(key);
            System.out.println(key + ": " + value);
        }
    }

    private static String readFile(String path) throws IOException
    {
        FileInputStream stream = new FileInputStream(new File(path));
        try
        {
            FileChannel fc = stream.getChannel();
            MappedByteBuffer bb = fc.map(
                    FileChannel.MapMode.READ_ONLY, 0, fc.size());
            /* Instead of using default, pass in a decoder. */
            return Charset.defaultCharset().decode(bb).toString();
        } finally
        {
            stream.close();
        }
    }
}
