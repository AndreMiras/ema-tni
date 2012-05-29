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

/**
 *
 * @author andre
 */
public class Helper
{
    public static <K,V> void printKeysValuesDict(
            HashMap<K, V> alphabetCountDict)
    {
        V value;
        for(K key : alphabetCountDict.keySet())
        {
            value = alphabetCountDict.get(key);
            System.out.println(key + ": " + value);
        }
    }

    public static <K,V> void printKeysValuesDict(
            SortedSet<Map.Entry<K, V>> nGramCountDict)
    {
        Map.Entry<K, V> mapEntry;
        Iterator it = nGramCountDict.iterator();
        while (it.hasNext())
        {
            mapEntry = (Map.Entry<K, V>)it.next();
            System.out.println(mapEntry.getKey() + ": " + mapEntry.getValue());
        }
    }

    public static String readFile(String path) throws IOException
    {
        FileInputStream stream = new FileInputStream(new File(path));
        try
        {
            FileChannel fc = stream.getChannel();
            MappedByteBuffer bb = fc.map(
                    FileChannel.MapMode.READ_ONLY, 0, fc.size());
            /* Instead of using default, pass in a decoder. */
            // return Charset.defaultCharset().decode(bb).toString();
            // return Charset.forName("utf-8").decode(bb).toString();
            return Charset.forName("ISO-8859-1").decode(bb).toString();
        } finally
        {
            stream.close();
        }
    }
}
