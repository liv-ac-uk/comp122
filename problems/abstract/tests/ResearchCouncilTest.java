import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assumptions.assumeTrue;
import static org.junit.Assert.assertThat;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;

import java.lang.reflect.*;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import org.junit.jupiter.api.Test;
import java.lang.reflect.Modifier;
import static org.hamcrest.CoreMatchers.*;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;


class ResearchCouncilTest {
    @Test
    public void testNameIsPrivate() {
        try {
            if (!Modifier.isPrivate(Class.forName("ResearchCouncil").getDeclaredField("name").getModifiers())) {
                fail("attribute name is not private");
            }
        } catch (Exception e) {
            fail("could not find a private attribute \"name\".");
            e.printStackTrace();
        }
    }

    @Test
    public void testEmailIsPrivate() {
        try {
            if (!Modifier.isPrivate(Class.forName("ResearchCouncil").getDeclaredField("email").getModifiers())) {
                fail("attribute email is not private");
            }
        } catch (Exception e) {
            fail("could not find a private attribute \"email\".");
            e.printStackTrace();
        }
    }

    @Test
    public void testNameSet() {
        ResearchCouncil researchCouncil = new ResearchCouncil();
        researchCouncil.setName("Test");
        assertThat(researchCouncil.getName(), is("Test"));
    }

    @Test
    public void testGreet() {
        ResearchCouncil researchCouncil = new ResearchCouncil();
        researchCouncil.setName("Test");
        researchCouncil.setEmail("Test");
        assertThat(researchCouncil.greet(), is("sendto: " + "Test" + " Dear " + "Test" + ",\n"));
    }

    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private final ByteArrayOutputStream errContent = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;
    private final PrintStream originalErr = System.err;

    @BeforeEach
    public void setUpStreams() {
        System.setOut(new PrintStream(outContent));
        System.setErr(new PrintStream(errContent));
    }

    @AfterEach
    public void restoreStreams() {
        System.setOut(originalOut);
        System.setErr(originalErr);
    }

    @Test
    public void testEmail() {
        ResearchCouncil researchCouncil = new ResearchCouncil();
        researchCouncil.setEmail("test@liv.ac.uk");
        researchCouncil.setName("test");
        researchCouncil.sendEmail();
        assertEquals("sendto: test@liv.ac.uk Dear test,", outContent.toString().trim());
    }


    @Test
    public void testImplementedBillable() {
        ResearchCouncil researchCouncil = new ResearchCouncil();
        assertThat(researchCouncil, instanceOf(Billable.class));
    }

    @Test
    public void testImplementedEmailable() {
        ResearchCouncil researchCouncil = new ResearchCouncil();
        assertThat(researchCouncil, instanceOf(Emailable.class));
    }

    @Test
    public void testBill() {
        ResearchCouncil researchCouncil = new ResearchCouncil();
        researchCouncil.payBill(10);
        assertEquals("10", outContent.toString().trim());
    }
}