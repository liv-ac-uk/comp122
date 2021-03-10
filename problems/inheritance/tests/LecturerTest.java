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
    public void testTimetableIsPrivate() {
        try {
            if (!Modifier.isPrivate(Class.forName("Lecturer").getDeclaredField("timetable").getModifiers())) {
                fail("attribute timetable is not private");
            }
        } catch (Exception e) {
            fail("could not find a private attribute \"timetable\".");
            e.printStackTrace();
        }
    }

    @Test
    public void testSetTimeTableIsPublic() {
        try {
            if (!Modifier.isPublic(Class.forName("Lecturer").getDeclaredMethod("setTimeTable").getModifiers())) {
                fail("method setTimeTable is not public");
            }
        } catch (Exception e) {
            fail("could not find a public method \"setTimeTable\".");
            e.printStackTrace();
        }
    }

    @Test
    public void testGetTimeTableIsPublic() {
        try {
            if (!Modifier.isPublic(Class.forName("Lecturer").getDeclaredMethod("getTimeTable").getModifiers())) {
                fail("method getTimeTable is not public");
            }
        } catch (Exception e) {
            fail("could not find a public method \"getTimeTable\".");
            e.printStackTrace();
        }
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
    public void testSetTimeTable() {
        Lecturer lecturer = new Lecturer();
        lecturer.setTimeTable("Test");
        assertThat(lecturer.getTimeTable(), is("Test"));
    }
}