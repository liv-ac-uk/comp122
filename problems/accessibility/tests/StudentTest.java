import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assumptions.assumeTrue;

import java.lang.reflect.*;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import org.junit.jupiter.api.Test;

import java.lang.reflect.Modifier;


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
            if (!Modifier.isPrivate(Class.forName("Student").getDeclaredField("allGrades").getModifiers())) {
                fail("attribute allGrades is not private");
            }
        } catch (Exception e) {
            fail("could not find a private attribute \"allGrades\".");
            e.printStackTrace();
        }
    }

    @Test
    public void testUpdateGradeIsPublic() {
        try {
            if (!Modifier.isPublic(Class.forName("Student").getDeclaredMethod("updateGrade").getModifiers())) {
                fail("method updateGrade is not public");
            }
        } catch (Exception e) {
            fail("could not find a public method \"updateGrade\".");
            e.printStackTrace();
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
        assertEquals(new int[] {0, 0, 0, 0}, s.getGrades());
    }

    @Test
    public void testGetBaseSubmitted() {
        Student s = new Student();
        assertEquals(new boolean[] {false, false, false, false}, s.getHasSubmitted());
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
        s.updateGrade(3, 24);
        assertEquals(86, s.getTotalGrade());
    }

    @Test
    public void testGetAllGrades() {
        Student s = new Student();
        s.updateGrade(0, 23);
        s.updateGrade(1, 20);
        s.updateGrade(2, 19);
        s.updateGrade(3, 24);
        assertEquals(new int[] {23, 20, 19, 24}, s.getGrades());
    }
    
    @Test
    public void testAssignment0Updates() {
        Student s = new Student();
        s.updateGrade(0, 23);
        assertEquals(new boolean[] {true, false, false, false}, s.getHasSubmitted());
    }

    @Test
    public void testAllAssignmentUpdates() {
        Student s = new Student();
        s.updateGrade(0, 23);
        s.updateGrade(1, 20);
        s.updateGrade(2, 19);
        s.updateGrade(3, 24);
        assertEquals(new boolean[] {true, true, true, true}, s.getHasSubmitted());
    }

    @Test
    public void testOutOfBoundsLower() {
        Student s = new Student();
        s.updateGrade(-1, 23);
        assertEquals(new int[] {0, 0, 0, 0}, s.getGrades());
        assertEquals(new boolean[] {false, false, false, false}, s.getHasSubmitted());
    }

    @Test
    public void testOutOfBoundsUpper() {
        Student s = new Student();
        s.updateGrade(4, 23);
        assertEquals(new int[] {0, 0, 0, 0}, s.getGrades());
        assertEquals(new boolean[] {false, false, false, false}, s.getHasSubmitted());
    }

    @Test
    public void testNegativeGrade() {
        Student s = new Student();
        s.updateGrade(0, -1);
        assertEquals(new int[] {0, 0, 0, 0}, s.getGrades());
        assertEquals(new boolean[] {false, false, false, false}, s.getHasSubmitted());
    }

    @Test
    public void testTooLargeGrade() {
        Student s = new Student();
        s.updateGrade(0, 27);
        assertEquals(new int[] {0, 0, 0, 0}, s.getGrades());
        assertEquals(new boolean[] {false, false, false, false}, s.getHasSubmitted());
    }
}
