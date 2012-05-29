/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package project4_ema_tni;

import java.io.IOException;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.junit.*;
import static org.junit.Assert.*;

/**
 *
 * @author andre
 */
public class LzEncoderTest
{
    private static String filePath = "";
    private static String fileName = "exemple1.txt";
    private static String text;

    public LzEncoderTest()
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
     * Test of getEncodedCharMap method, of class LzEncoder.
     * TODO: code comments
     */
    @Test
    public void testGetEncodedCharMap()
    {
        System.out.println("getEncodedCharMap");
        LzEncoder lzEncoder = new LzEncoder(text);
        ArrayList result = lzEncoder.getEncodedCharMap();

        assertEquals(255, result.size());
        assertEquals(" ", result.get(0));
        assertEquals("e", result.get(1));
        assertEquals("s", result.get(2));
        assertEquals("n", result.get(3));
        assertEquals("a", result.get(4));

        
        assertEquals("ev", result.get(252));
        assertEquals("sp", result.get(253));
        assertEquals("va", result.get(254));
    }

    /**
     * Test of getEncodeText method, of class LzEncoder.
     */
    @Test
    public void testGetEncodeText()
    {
        System.out.println("getEncodeText");
        LzEncoder lzEncoder = new LzEncoder(text);
        ArrayList<Byte> result = lzEncoder.getEncodeText();

        assertEquals(13543, result.size()); // 13527
        assertEquals(38, result.get(0).intValue());
        assertEquals(86, result.get(1).intValue());
        assertEquals(95, result.get(13541).intValue()); // b4 06 69
        assertEquals(-79, result.get(13542).intValue());
    }
}
