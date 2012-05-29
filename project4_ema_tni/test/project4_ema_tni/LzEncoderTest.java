/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package project4_ema_tni;

import java.util.ArrayList;
import org.junit.*;
import static org.junit.Assert.*;

/**
 *
 * @author andre
 */
public class LzEncoderTest
{
    
    public LzEncoderTest()
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
     * Test of getEncodedCharMap method, of class LzEncoder.
     */
    @Test
    public void testGetEncodedCharMap()
    {
        System.out.println("getEncodedCharMap");
        LzEncoder instance = null;
        ArrayList expResult = null;
        ArrayList result = instance.getEncodedCharMap();
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of getEncodeText method, of class LzEncoder.
     */
    @Test
    public void testGetEncodeText()
    {
        System.out.println("getEncodeText");
        LzEncoder instance = null;
        ArrayList expResult = null;
        ArrayList result = instance.getEncodeText();
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }
}
