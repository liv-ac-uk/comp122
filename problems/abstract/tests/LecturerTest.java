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

class LecturerTest {
    @Test
    public void testNameIsPrivate() {
        try {
            if (!Modifier.isPrivate(Class.forName("Lecturer").getDeclaredField("name").getModifiers())) {
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
            if (!Modifier.isPrivate(Class.forName("Lecturer").getDeclaredField("email").getModifiers())) {
                fail("attribute email is not private");
            }
        } catch (Exception e) {
            fail("could not find a private attribute \"email\".");
            e.printStackTrace();
        }
    }

    @Test
    public void testInheritedPerson() {
        Lecturer lecturer = new Lecturer();
        assertThat(lecturer, instanceOf(Person.class));
    }

    @Test
    public void testNameSet() {
        Lecturer lecturer = new Lecturer();
        lecturer.setName("Test");
        assertThat(lecturer.getName(), is("Test"));
    }

    @Test
    public void testGreet() {
        Lecturer lecturer = new Lecturer();
        lecturer.setName("Test");
        lecturer.setEmail("Test");
        assertThat(lecturer.greet().trim(), is("sendto: " + "Test" + " Hi " + "Test,"));
    }

    @Test
    public void testTimeTable() {
        Lecturer lecturer = new Lecturer();
        lecturer.setTimeTable("Test");

        assertThat(lecturer.getTimeTable(), is("Test"));
    }

    @Test
    public void testImplementedPayable() {
        Lecturer lecturer = new Lecturer();
        assertThat(lecturer, instanceOf(Payable.class));
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
    public void testPayLecturer() {
        Lecturer lecturer = new Lecturer();
        lecturer.payAmount(10);
        assertEquals("10", outContent.toString().trim());
    }
}