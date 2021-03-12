import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assumptions.assumeTrue;

import java.lang.reflect.*;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import org.junit.jupiter.api.Test;

import java.lang.reflect.Modifier;
import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.assertThat;
import static org.junit.Assert.assertTrue;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;


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
    public void testPersonAbstract() {
        try {
            if (!Modifier.isAbstract(Class.forName("Person").getModifiers())) {
                fail("class person is not abstract");
            }
        } catch (Exception e) {
            fail("could not find an abstract class \"Person\".");
            e.printStackTrace();
        }
    }


    @Test
    public void testImplementedEmailable() {
        try {
            if (!Emailable.class.isAssignableFrom(Class.forName("Person"))) {
                fail("class person does not implement emailable");
            }
        } catch (Exception e) {
            fail("could not find class \"Person\".");
            e.printStackTrace();
        }
    }

}