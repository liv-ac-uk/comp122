import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assumptions.assumeTrue;

import java.lang.reflect.*;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import org.junit.jupiter.api.Test;

import java.lang.reflect.Modifier;
import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.assertThat;


class PersonTest {
    @Test
    public void testNameIsPrivate() {
        try {
            if (!Modifier.isPrivate(Class.forName("Person").getDeclaredField("name").getModifiers())) {
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
            if (!Modifier.isPrivate(Class.forName("Person").getDeclaredField("email").getModifiers())) {
                fail("attribute email is not private");
            }
        } catch (Exception e) {
            fail("could not find a private attribute \"email\".");
            e.printStackTrace();
        }
    }

    @Test
    public void testGreetIsPublic() {
        try {
            if (!Modifier.isPublic(Class.forName("Person").getDeclaredMethod("greet").getModifiers())) {
                fail("method greet is not public");
            }
        } catch (Exception e) {
            fail("could not find a public method \"greet\".");
            e.printStackTrace();
        }
    }

    @Test
    public void testNameSet() {
        Person person = new Person();
        person.setName("Test");
        assertThat(person.getName(), is("Test"));
    }

    @Test
    public void testGreet() {
        Person person = new Person();
        person.setName("Test");
        person.setEmail("Test");
        assertThat(person.greet(), is("sendto: " + "Test" + "Hi " + "Test" + ",\n"));
    }
}