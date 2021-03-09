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
    public void testInheritedPerson() {
        Professor professor = new Professor();
        assertThat(professor, instanceOf(Person.class));
    }

    @Test
    public void testInheritedLecturer() {
        Professor professor = new Professor();
        assertThat(professor, instanceOf(Lecturer.class));
    }

    @Test
    public void testTimetableIsPrivate() {
        try {
            if (!Modifier.isPrivate(Class.forName("Professor").getDeclaredField("timetable").getModifiers())) {
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
            if (!Modifier.isPublic(Class.forName("Professor").getDeclaredMethod("setTimeTable").getModifiers())) {
                fail("method setTimeTable is not public");
            }
        } catch (Exception e) {
            fail("could not find a public method \"setTimeTable\".");
            e.printStackTrace();
        }
    }

    @Test
    public void testBudgetIsPrivate() {
        try {
            if (!Modifier.isPrivate(Class.forName("Professor").getDeclaredField("budget").getModifiers())) {
                fail("attribute budget is not private");
            }
        } catch (Exception e) {
            fail("could not find a private attribute \"budget\".");
            e.printStackTrace();
        }
    }

    @Test
    public void testSetBudgetIsPublic() {
        try {
            if (!Modifier.isPublic(Class.forName("Professor").getDeclaredMethod("setBudget").getModifiers())) {
                fail("method setBudget is not public");
            }
        } catch (Exception e) {
            fail("could not find a public method \"setBudget\".");
            e.printStackTrace();
        }
    }

    @Test
    public void testGetBudgetIsPublic() {
        try {
            if (!Modifier.isPublic(Class.forName("Professor").getDeclaredMethod("getBudget").getModifiers())) {
                fail("method getBudget is not public");
            }
        } catch (Exception e) {
            fail("could not find a public method \"getBudget\".");
            e.printStackTrace();
        }
    }

    @Test
    public void testGetTimeTableIsPublic() {
        try {
            if (!Modifier.isPublic(Class.forName("Professor").getDeclaredMethod("getTimeTable").getModifiers())) {
                fail("method getTimeTable is not public");
            }
        } catch (Exception e) {
            fail("could not find a public method \"getTimeTable\".");
            e.printStackTrace();
        }
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
    public void testSetTimeTable() {
        Professor professor = new Professor();
        professor.setTimeTable("Test");
        assertThat(professor.getTimeTable(), is("Test"));
    }

    @Test
    public void testSetBudget() {
        Professor professor = new Professor();
        professor.setBudget(10);
        assertThat(professor.getBudget(), is(10));
    }
}