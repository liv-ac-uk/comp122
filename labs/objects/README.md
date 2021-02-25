# A Touch of Class

All of the variables we have used so far (with the exception of Scanner) have been primitive data types. There's an awful lot you can do with primitive data types, in languages such as C we only have primitive data types (and people have done an awful lot with C).

In Java however we have the option of creating more complex datatypes, classes!

Programs of can get complex very quickly, in large pieces of software it is simply impossible to keep track of tens of thousands of lines of code when they are in a single file. To make life much easier for ourselves (honestly), we separate our code into separate functional classes.

## Class Half Full

You may have noticed that you have been using classes in every single Java program you have written in this course so far (nice job!).

We define a class using the `class` keyword, which you may note has been near the start of each of your submissions. Each of our programs have been quite short, so we haven't used many of the features apart from a single function where we have put all of our code.

Each of our classes can contain a number of variables, as well as functions to operate on those variables.

From now on, variables when they belong to a class will be referred to as attributes, and a function which belongs to a class is called a method.

## Method in the Madness

This ability to separate methods into classes is what makes object oriented programming so powerful.

We define a method by first specifying the access modifier of the method, which for now we will make `public`, then the return type of the method, which will be either a primitive data type, another class or `void` to indicate no return type. We then have the name of the method, followed by the types and names of each of the variables the method will take. An example class with a single variable and a single method could be:

```java
public class Student {
    public boolean hasSubmitted = false;

    public void submitCoursework() {
        hasSubmitted = true;
    }
}
```

The body of this class defines the operations we can perform on this object.

## My Body Is Not An Object

To use classes we must first *instantiate* these as objects. We do this in exactly the same manner as we declared the arrays earlier in this lab e.g.

```java
...
Student alice = new Student();      // Instantiating a class
System.out.println("Alice Submitted Coursework: " + alice.hasSubmitted)
alice.submitCoursework()
System.out.println("Alice Submitted Coursework: " + alice.hasSubmitted)
...
```

This is a bit of a boring class currently, so let's add some functionality

## What's in a Name?

Most students have a name, so at the top of the class add a `public String` variable `name`.

We want to be able to be able to set the students name, so add a method to *set* the name, `setName()`.

Additionally add an `int` to the class to keep track of the students score, called `grade`, initially equal to `0`

After each of the assignments, the lecturer will update the students score with a method which will return a `void` called `updateGrade(int mark)`, which will add the students grade for that assignment to their `grade`.

The automarker will be using these terms, so make sure to follow this specification closely!
