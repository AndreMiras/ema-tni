/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package project4_ema_tni;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.NavigableSet;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.junit.*;
import static org.junit.Assert.*;

/**
 *
 * @author andre
 */
public class LzDictionaryTest
{
    private static String filePath = "";
    private static String fileName = "exemple1.txt";
    private static String text;
    
    public LzDictionaryTest()
    {
        String fullPath = filePath + fileName;
        try
        {
            text = Helper.readFile(fullPath);
        } catch (IOException ex)
        {
            Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
            text = "";
        }
    }

    @BeforeClass
    public static void setUpClass() throws Exception
    {
    }

    @AfterClass
    public static void tearDownClass() throws Exception
    {
    }
    
    @Before
    public void setUp()
    {
    }
    
    @After
    public void tearDown()
    {
    }

    /**
     * Test of getNGramCountDict method, of class LzDictionary.
     */
    @Test
    public void testGetNGramCountDict()
    {
        System.out.println("getNGramCountDict");
        LzDictionary lzDictionary = new LzDictionary(text, 2);
        int expResult = 551;

        HashMap<String, Integer> alphabetCountDict =
                lzDictionary.getNGramCountDict();
        // there are 551 different digrams in the exemple1.txt file
        assertEquals(expResult, alphabetCountDict.size());
    }

    /**
     * Testing few known digrams
     */
    @Test
    public void testDiGrams()
    {
        System.out.println("Testing few digrams");
        LzDictionary lzDictionary = new LzDictionary(text, 2);

        HashMap<String, Integer> alphabetCountDict =
                lzDictionary.getNGramCountDict();

        assertEquals(18, alphabetCountDict.get("fo").intValue());
        assertEquals(4, alphabetCountDict.get("ob").intValue());
        assertEquals(57, alphabetCountDict.get("ar").intValue());
    }

    /**
     * Test of getNGramCountDictSorted method, of class LzDictionary.
     */
    @Test
    public void testGetNGramCountDictSorted()
    {
        System.out.println("getNGramCountDictSorted");
        LzDictionary instance = null;
        NavigableSet expResult = null;
        NavigableSet result = instance.getNGramCountDictSorted();
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of getNGramArraySortedByCount method, of class LzDictionary.
     */
    @Test
    public void testGetNGramArraySortedByCount()
    {
        System.out.println("getNGramArraySortedByCount");
        LzDictionary instance = null;
        ArrayList expResult = null;
        ArrayList result = instance.getNGramArraySortedByCount();
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of entriesSortedByValues method, of class LzDictionary.
     */
    /*
    @Test
    public void testEntriesSortedByValues()
    {
        System.out.println("entriesSortedByValues");
        Map<K, V> map = null;
        NavigableSet expResult = null;
        NavigableSet result = LzDictionary.entriesSortedByValues(map);
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }
    */
}
