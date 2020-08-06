import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assumptions.assumeTrue;

import java.lang.reflect.*;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import org.junit.jupiter.api.Test;

import java.lang.reflect.Modifier;


class CircleTest {
    @Test
    public void testRadiusIsPrivate() {
        try {
            if (!Modifier.isPrivate(Class.forName("Circle").getDeclaredField("radius").getModifiers())) {
                fail("attribute radius is not private");
            }
        } catch (Exception e) {
            fail("could not find a private attribute \"radius\".");
            e.printStackTrace();
        }
    }

    @Test
    public void testConstructor() {
        Circle c = new Circle();
    }
    @Test
    public void testConstructor2() {
        Circle c = new Circle(1.0);
    }

    @Test
    public void getRadius() {
        Circle c = new Circle(12);
        assertEquals(12, c.getRadius());
    }

    @Test
    public void setRadius() {
        Circle c = new Circle();
        c.setRadius(12);
        assertEquals(12, c.getRadius());
    }

    @Test
    public void testCalcPerimeter() {
        double radius = 12.0;
        double p = (2*Math.PI*radius);
        Circle c = new Circle(radius);
        assertEquals(p, c.calcPerimeter());
    }

    @Test
    public void testCalcArea() {
        double radius = 12.0;
        double area = (Math.PI*radius*radius);
        Circle c = new Circle(radius);
        assertEquals(area, c.calcArea());
    }
}

