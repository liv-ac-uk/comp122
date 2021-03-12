import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assumptions.assumeTrue;
import static org.junit.Assert.assertThat;

import java.lang.reflect.*;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import org.junit.jupiter.api.Test;
import java.lang.reflect.Modifier;
import static org.hamcrest.CoreMatchers.*;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;


import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;



class DogTest {
    @Test
    public void testGoodGirlIsPrivate() {
        try {
            if (!Modifier.isPrivate(Class.forName("Dog").getDeclaredField("goodGirl").getModifiers())) {
                fail("attribute name is not private");
            }
        } catch (Exception e) {
            fail("could not find a private attribute \"goodGirl\".");
            e.printStackTrace();
        }
    }

    @Test
    public void testAwardDegreeIsPublic() {
        try {
            if (!Modifier.isPublic(Class.forName("Dog").getMethod("awardDegree").getModifiers())) {
                fail("awardDegree email is not public");
            }
        } catch (Exception e) {
            fail("could not find a public method \"awardDegree\".");
            e.printStackTrace();
        }
    }

    @Test
    public void testImplementedDegreeable() {
        Dog laika = new Dog();
        assertThat(laika, instanceOf(Degreeable.class));
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
    public void testAwardDegree() {
        Dog laika = new Dog();
        laika.awardDegree();
        assertEquals("Arruff woof woof. WOOF!", outContent.toString().trim());
    }
}