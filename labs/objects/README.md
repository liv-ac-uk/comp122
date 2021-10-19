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

Let's change the given starter code `Student.java` a bit, as follows.

- Most students have a name, so at the top of the class add a `public String` variable `name`.  
  We want to be able to be able to set the students name, so add a method to *set* the name, `setName()`.

- Additionally add an `int` to the class to keep track of the students score, called `grade`, initially equal to `0`.

- After each of the assignments, the lecturer will update the students score with a method which will return a `void` called `setGrade(int mark)`, which will add the students grade for that assignment to their `grade`.

- As we need to access the `grade` attribute, make sure there is also a `int getGrade()` method.

The automarker will be using these terms, so make sure to follow this specification closely (capitalisation matters)!

{% next %}

## Gather Round

Lecturers will typically store their students grades on an abacus, but some progressive types have started using software to do this for them. 

We often deal with lots of objects of the same type when building real world software, and Java makes it easy for us to bundle these together into *Arrays*. Arrays in Java allow us to structure our code and saves us from creating lots of variables (which looks messy).

Lets start creating some software to simulate a virtual classroom, similar to the one you're virtually interacting with right now!

{% next %}

## I'm So Meta, Even This Acronym

Go to the empty `VGather.java` file where we will store the code for our virtual virtual classroom. 

For now we'll keep it simple and write a `public class VGather` with a single `public static void main(String[] args)` method, and all this program will do is help the lecturer calculate the class average. 

The Lecturer has all the students grades written down so needs to enter them one by one into the terminal, and will then expect to have the average returned to them.

To do this use the `Comp122.getInt()` method to first read in the number of students, then use a `for` loop to read in the grade of each student.

Once all the `Student`s have had their grades read in, use another `for` loop to compute the class average, and print this to the terminal.
This output should display at most 2 digits after the decimal point.

Example Usages: 

```console
$> java VGather 
How Many Students In Class?
3
Enter a grade:
1
Enter a grade:
2
Enter a grade:
3
2.0
```

```console
How Many Students In Class?
2
Enter a grade:
3
Enter a grade:
4
3.5
```

```console
How Many Students In Class?
3
Enter a grade:
3
Enter a grade:
3
Enter a grade:
4
3.33
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

{% spoiler "Hint" %}

There are several ways to print a double only up to a given precision.
One easy way is to print at most the last 2 digits after the decimal point is to multiply by `100`, round to the next integer, then multiply by `100`.
Use [`Math.round`](https://docs.oracle.com/javase/8/docs/api/java/lang/Math.html#round-double-) here?
{% endspoiler %}

{% next %}

## Submission

Submit your solution to this exercise through Canvas/CodeGrade as before.

