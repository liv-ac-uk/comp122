import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assumptions.assumeTrue;
import static org.junit.Assert.assertThat;

import java.lang.reflect.*;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import org.junit.jupiter.api.Test;
import java.lang.reflect.Modifier;
import static org.hamcrest.CoreMatchers.*;

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
        assertThat(lecturer.greet(), is("sendto: " + "Test" + "Hi " + "Test" + ",\n"));
    }

    @Test
    public void testTimeTable() {
        Lecturer lecturer = new Lecturer();
        lecturer.setTimeTable("Test");

        assertThat(lecturer.getTimeTable(), is("Test"));
    }
}