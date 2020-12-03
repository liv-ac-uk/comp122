import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assumptions.assumeTrue;
import static org.junit.Assert.assertThat;

import java.lang.reflect.*;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import org.junit.jupiter.api.Test;
import java.lang.reflect.Modifier;
import static org.hamcrest.CoreMatchers.*;

class ProfessorTest {
    @Test
    public void testNameIsPrivate() {
        try {
            if (!Modifier.isPrivate(Class.forName("Professor").getDeclaredField("name").getModifiers())) {
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
            if (!Modifier.isPrivate(Class.forName("Professor").getDeclaredField("email").getModifiers())) {
                fail("attribute email is not private");
            }
        } catch (Exception e) {
            fail("could not find a private attribute \"email\".");
            e.printStackTrace();
        }
    }

    @Test
    public void testInheritedLecturer() {
        Professor professor = new Professor();
        assertThat(professor, instanceOf(Lecturer.class));
    }

    @Test
    public void testNameSet() {
        Professor professor = new Professor();
        professor.setName("Test");
        assertThat(professor.getName(), is("Test"));
    }

    @Test
    public void testGreet() {
        Professor professor = new Professor();
        professor.setName("Test");
        professor.setEmail("Test");
        assertThat(professor.greet(), is("sendto: " + "Test" + "Hi " + "Test" + ",\n"));
    }

    @Test
    public void testTimeTable() {
        Professor professor = new Professor();
        professor.setTimeTable("Test");

        assertThat(professor.getTimeTable(), is("Test"));
    }

    @Test
    public void testBudget() {
        Professor professor = new Professor();
        professor.setBudget(60);

        assertThat(professor.getTimeTable(), is(60));
    }
}