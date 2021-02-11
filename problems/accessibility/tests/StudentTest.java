import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assumptions.assumeTrue;

import java.lang.reflect.*;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import org.junit.jupiter.api.Test;

import java.lang.reflect.Modifier;
// import org.junit.jupiter.api.Assert.*;
import java.io.StringWriter;
import java.io.PrintWriter;


class StudentTest {
    @Test
    public void testHasSubmittedIsPrivate() {
        try {
            if (!Modifier.isPrivate(Class.forName("Student").getDeclaredField("hasSubmitted").getModifiers())) {
                fail("attribute radius is not private");
            }
        } catch (Exception e) {
            fail("could not find a private attribute \"hasSubmitted\".");
            e.printStackTrace();
        }
    }

    @Test
    public void testGradeIsPrivate() {
        try {
            if (!Modifier.isPrivate(Class.forName("Student").getDeclaredField("finalGrades").getModifiers())) {
                fail("attribute finalGrades is not private");
            }
        } catch (Exception e) {
            fail("could not find a private attribute \"finalGrades\".");
            e.printStackTrace();
        }
    }

    @Test
    public void testUpdateGradeIsPublic() {
        try {
            if (!Modifier.isPublic(Class.forName("Student").getDeclaredMethod("updateGrade", int.class, int.class).getModifiers())) {
                fail("method updateGrade is not public");
            }
        } catch (Exception e) {
            StringWriter sw = new StringWriter();
            PrintWriter pw = new PrintWriter(sw);
            e.printStackTrace(pw);
            fail("Ensure you have a public updateGrade(int, int) method");

        }
    }

    @Test
    public void testGetHasSubmittedIsPublic() {
        try {
            if (!Modifier.isPublic(Class.forName("Student").getDeclaredMethod("getHasSubmitted").getModifiers())) {
                fail("method getHasSubmitted is not public");
            }
        } catch (Exception e) {
            fail("could not find a public method \"getHasSubmitted\".");
            e.printStackTrace();
        }
    }

    @Test
    public void testGetGradesIsPublic() {
        try {
            if (!Modifier.isPublic(Class.forName("Student").getDeclaredMethod("getGrades").getModifiers())) {
                fail("method getGrades is not public");
            }
        } catch (Exception e) {
            fail("could not find a public method \"getGrades\".");
            e.printStackTrace();
        }
    }

    @Test
    public void testGetTotalGradeIsPublic() {
        try {
            if (!Modifier.isPublic(Class.forName("Student").getDeclaredMethod("getTotalGrade").getModifiers())) {
                fail("method getTotalGrade is not public");
            }
        } catch (Exception e) {
            fail("could not find a public method \"getTotalGrade\".");
            e.printStackTrace();
        }
    }

    @Test
    public void testConstructor() {
        Student s = new Student();
    }

    @Test
    public void testGetBaseGrades() {
        Student s = new Student();
        assertArrayEquals(new int[] {0, 0, 0}, s.getGrades());
    }

    @Test
    public void testGetBaseSubmitted() {
        Student s = new Student();
        assertArrayEquals(new boolean[] {false, false, false}, s.getHasSubmitted());
    }

    @Test
    public void testGetBaseTotalGrade() {
        Student s = new Student();
        assertEquals(0, s.getTotalGrade());
    }

    @Test
    public void testUpdateFirstGrade() {
        Student s = new Student();
        s.updateGrade(0, 23);
        assertEquals(23, s.getTotalGrade());
    }

    @Test
    public void testGetTotalGrades() {
        Student s = new Student();
        s.updateGrade(0, 23);
        s.updateGrade(1, 20);
        s.updateGrade(2, 19);
        assertEquals(62, s.getTotalGrade());
    }

    @Test
    public void testGetAllGrades() {
        Student s = new Student();
        s.updateGrade(0, 23);
        s.updateGrade(1, 20);
        s.updateGrade(2, 19);
        assertArrayEquals(new int[] {23, 20, 19}, s.getGrades());
    }

    @Test
    public void testAssignment0Updates() {
        Student s = new Student();
        s.updateGrade(0, 23);
        assertArrayEquals(new boolean[] {true, false, false}, s.getHasSubmitted());
    }

    @Test
    public void testAllAssignmentUpdates() {
        Student s = new Student();
        s.updateGrade(0, 23);
        s.updateGrade(1, 20);
        s.updateGrade(2, 19);
        assertArrayEquals(new boolean[] {true, true, true}, s.getHasSubmitted());
    }

    @Test
    public void testOutOfBoundsLower() {
        Student s = new Student();
        s.updateGrade(-1, 23);
        assertArrayEquals(new int[] {0, 0, 0}, s.getGrades());
        assertArrayEquals(new boolean[] {false, false, false}, s.getHasSubmitted());
    }

    @Test
    public void testOutOfBoundsUpper() {
        Student s = new Student();
        s.updateGrade(4, 23);
        assertArrayEquals(new int[] {0, 0, 0}, s.getGrades());
        assertArrayEquals(new boolean[] {false, false, false}, s.getHasSubmitted());
    }

    @Test
    public void testNegativeGrade() {
        Student s = new Student();
        s.updateGrade(0, -1);
        assertArrayEquals(new int[] {0, 0, 0}, s.getGrades());
        assertArrayEquals(new boolean[] {false, false, false}, s.getHasSubmitted());
    }

    @Test
    public void testTooLargeGrade() {
        Student s = new Student();
        s.updateGrade(0, 57);
        assertArrayEquals(new int[] {0, 0, 0}, s.getGrades());
        assertArrayEquals(new boolean[] {false, false, false}, s.getHasSubmitted());
    }
}
