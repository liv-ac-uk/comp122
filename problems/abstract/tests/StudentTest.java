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


class StudentTest {
    @Test
    public void testNameIsPrivate() {
        try {
            if (!Modifier.isPrivate(Class.forName("Student").getDeclaredField("name").getModifiers())) {
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
            if (!Modifier.isPrivate(Class.forName("Student").getDeclaredField("email").getModifiers())) {
                fail("attribute email is not private");
            }
        } catch (Exception e) {
            fail("could not find a private attribute \"email\".");
            e.printStackTrace();
        }
    }

    @Test
    public void testInheritedPerson() {
        Student student = new Student();
        assertThat(student, instanceOf(Person.class));
    }

    @Test
    public void testNameSet() {
        Student student = new Student();
        student.setName("Test");
        assertThat(student.getName(), is("Test"));
    }

    @Test
    public void testGreet() {
        Student student = new Student();
        student.setName("Test");
        student.setEmail("Test");
        assertThat(student.greet(), is("sendto: " + "Test" + " Hi " + "Test" + ",\n"));
    }

    @Test
    public void testGrades() {
        Student student = new Student();
        student.setGrade(5);
        assertThat(student.getGrade(), is(5));
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
        Student student = new Student();
        student.setEmail("test@liv.ac.uk");
        student.setName("test");
        student.setGrade(70);
        student.sendEmail();
        assertEquals("sendto: test@liv.ac.uk Hi test,", outContent.toString().trim());
    }

    @Test
    public void testDegree() {
        Student student = new Student();
        student.setGrade(70);
        student.awardDegree();
        assertEquals("You Passed Your Degree, hooray!", outContent.toString().trim());
    }


    @Test
    public void testBill() {
        Student student = new Student();
        student.payBill(10);
        assertEquals("10", outContent.toString().trim());
    }


    @Test
    public void testImplementedDegreeable() {
        try {
            if (!Degreeable.class.isAssignableFrom(Class.forName("Student"))) {
                fail("class student does not implement degreeable");
            }
        } catch (Exception e) {
            fail("could not find class \"Student\".");
            e.printStackTrace();
        }
    }

}