# A Touch of Class

All of the variables we have used so far (with the exception of `Arrays` and `Comp122`) have been primitive data types. There's an awful lot you can do with primitive data types, in languages such as C we only have primitive data types (and people have done an awful lot with C).

In Java however we have the option of creating more complex datatypes, classes!

Programs of can get complex very quickly, in large pieces of software it is simply impossible to keep track of tens of thousands of lines of code when they are in a single file. To make life much easier for ourselves (honestly), we separate our code into separate functional classes.

{% next %}

## Class Half Full

You may have noticed that you have been using classes in every single Java program you have written in this course so far, nice job!

We define a class using the `class` keyword, which you may note has been near the start of each of your submissions. Each of our programs have been quite short, so we haven't used many of the features apart from a single function where we have put all of our code.

Each of our classes can contain a number of variables, as well as functions to operate on those variables.

From now on, variables when they belong to a class will be referred to as attributes, and a function which belongs to a class is called a method.

{% next %}

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

{% next %}

## My Body Is Not An Object

The body of this class defines the operations we can perform on this object. Once we have the class body written in a Java file, we can use it in any other code in the folder. 

To use classes we must first *instantiate* these as objects otherwise we will get an exception. We do this in exactly the same manner as we declared primitive types in previous labs e.g.

```java
...
Student alice = new Student();      // Instantiating a class
System.out.println("Alice Submitted Coursework: " + alice.hasSubmitted)
alice.submitCoursework()
System.out.println("Alice Submitted Coursework: " + alice.hasSubmitted)
...
```

This is a bit of a boring class currently, so let's add some functionality.

{% next %}

## What's in a Name?

Most students have a name, so at the top of the class add a `public String` variable `name`.

We want to be able to be able to set the students name, so add a method to *set* the name, `setName()`.

Additionally add an `int` to the class to keep track of the students score, called `grade`, initially equal to `0`

After each of the assignments, the lecturer will update the students score with a method which will return a `void` called `updateGrade(int mark)`, which will add the students grade for that assignment to their `grade`.

As we need to access the `grade` attribute, make sure there is also a `int getGrade()` method.

The automarker will be using these terms, so make sure to follow this specification closely!

{% next %}

## Gather Round

Lecturers will typically store their students grades on an abacus, but some progressive types have started using software to do this for them. 

We often deal with lots of objects of the same type when building real world software, and Java makes it easy for us to bundle these together into *Arrays*. Arrays in Java allow us to structure our code and saves us from creating lots of variables (which looks messy).

Lets start creating some software to simulate a virtual classroom, similar to the one you're virtually interacting with right now!

{% next %}

## I'm So Meta, Even This Acronym

Create a new file called `VGather.java` where we will store our virtual virtual classroom. You can do this in CS50 Lab Environment by clicking on the + symbol next to the tab for `Student.java`.

For now we'll keep it simple and write a `public class VGather` with a single `public static void main(String[] args)` method, and all this program will do is help the lecturer calculate the class average. 

The Lecturer has all the students grades written down so needs to enter them one by one into the terminal, and will then expect to have the average returned to them.

To do this use the `Comp122.getInt()` method to first read in the number of students, then use a `for` loop to read in the grade of each student.

Once all the `Student`s have had their grades read in, use another `for` loop to compute the class average, and print this to the terminal.

Example Usage: 

```
$ java VGather 
How Many Students In Class?  // Output
3                           // Input
Enter a grade:              // Output
25                          // Input
Enter a grade:
23
Enter a grade:
27
25                          // Output
```

{% spoiler "Hint" %}
To read in an integer and create an array of size `n` the syntax is:

```java
int n = Comp122.getInt("How Many Students in Class?");
Student[] studentArray = new Student[n];
```

You can loop through this array and modify each object individually:

```java
for (int i = 0; i < n; i++) {
    ...
    studentArray[i].setGrade(AN_INTEGER_READ_IN_EARLIER);
}    
```

{% endspoiler %}

{% next %}

## Submission

These programs will be tested automatically against a range of test cases, so ensure that the output matches the examples given otherwise these are guaranteed to fail.

Once you have completed these exercises submit these in the usual way

```
check50 liv-ac-uk/comp122/2021/problems/objects
```

and submit via

```
submit50 liv-ac-uk/comp122/2021/problems/objects
```
