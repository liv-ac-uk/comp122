import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assumptions.assumeTrue;

import java.lang.reflect.*;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import org.junit.jupiter.api.Test;

import java.lang.reflect.Modifier;


class StudentTest {
    @Test
    public void testBlankConstructor() {
        Student s = new Student();
    }

    @Test
    public void testFullConstructor() {
        Student s = new Student("Alice", "aliceXtreme@aol.com", 1984, 2021, 1234567);
        assertEquals("Alice", s.getName());
        assertEquals("aliceXtreme@aol.com", s.getEmail());
        assertEquals(1984, s.getYearOfBirth());
        assertEquals(2021, s.getEnrolmentYear());
        assertEquals(1234567, s.getStudentId());
    }

    @Test
    public void testPartialConstructor1() {
        Student s = new Student("Alice", "aliceXtreme@aol.com", 1984);
        assertEquals("Alice", s.getName());
        assertEquals("aliceXtreme@aol.com", s.getEmail());
        assertEquals(1984, s.getYearOfBirth());
    }

    @Test
    public void testPartialConstructor2() {
        Student s = new Student("Alice", "aliceXtreme@aol.com", "01/09/1984");
        assertEquals("Alice", s.getName());
        assertEquals("aliceXtreme@aol.com", s.getEmail());
        assertEquals(1984, s.getYearOfBirth());
    }

    @Test
    public void testPartialConstructor3() {
        Student s = new Student("Alice", "aliceXtreme@aol.com", "01/09/2001");
        assertEquals("Alice", s.getName());
        assertEquals("aliceXtreme@aol.com", s.getEmail());
        assertEquals(2001, s.getYearOfBirth());
    }
}