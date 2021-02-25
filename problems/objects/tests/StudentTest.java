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
    public void testSetName() {
        Student s = new Student();
        try {
            s.setName("Alice");
        catch {
            fail("Your setName method is faulty");
        }
    }

    @Test
    public void testGetName() {
        Student s = new Student();
        try {
            s.setName("Alice";
            assertEquals("Alice", s.getName();)
        catch {
            fail("Your getName method is faulty");
        }
    }

    @Test
    public void testSetGrade() {
        Student s = new Student();
        try {
            s.setGrade(10);
        catch {
            fail("Your setGrade method is faulty");
        }
    }

    @Test
    public void testGetGrade() {
        Student s = new Student();
        try {
            s.setGrade(10);
            assertEquals(10, s.getGrade());
        catch {
            fail("Your setGrade method is faulty");
        }
    }
}