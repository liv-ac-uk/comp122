import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assumptions.assumeTrue;
import static org.junit.Assert.assertThat;

import java.lang.reflect.*;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import org.junit.jupiter.api.Test;
import java.lang.reflect.Modifier;
import static org.hamcrest.CoreMatchers.*;

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
    public void testGradeIsPrivate() {
        try {
            if (!Modifier.isPrivate(Class.forName("Student").getDeclaredField("grade").getModifiers())) {
                fail("attribute grade is not private");
            }
        } catch (Exception e) {
            fail("could not find a private attribute \"grade\".");
            e.printStackTrace();
        }
    }

    @Test
    public void testSetGradeIsPublic() {
        try {
            if (!Modifier.isPublic(Class.forName("Student").getDeclaredMethod("setGrade").getModifiers())) {
                fail("method setGrade is not public");
            }
        } catch (Exception e) {
            fail("could not find a public method \"setGrade\".");
            e.printStackTrace();
        }
    }

    @Test
    public void testGetGradeIsPublic() {
        try {
            if (!Modifier.isPublic(Class.forName("Student").getDeclaredMethod("getGrade").getModifiers())) {
                fail("method getGrade is not public");
            }
        } catch (Exception e) {
            fail("could not find a public method \"getGrade\".");
            e.printStackTrace();
        }
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
        assertThat(student.greet(), is("sendto: " + "Test" + "Hi " + "Test" + ",\n"));
    }

    @Test
    public void testSetGrade() {
        Student student = new Student();
        student.setGrade(10);
        assertThat(student.getGrade(), is(10));
    }
}