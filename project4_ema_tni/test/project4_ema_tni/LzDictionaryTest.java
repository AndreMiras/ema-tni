/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package project4_ema_tni;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.NavigableSet;
import org.junit.*;
import static org.junit.Assert.*;

/**
 *
 * @author andre
 */
public class LzDictionaryTest
{
    
    public LzDictionaryTest()
    {
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
        LzDictionary instance = null;
        HashMap expResult = null;
        HashMap result = instance.getNGramCountDict();
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
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
