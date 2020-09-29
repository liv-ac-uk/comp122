# Constructing Classes
In our previous programs we haven't kept much information about the students, apart from their grades. Due to the strength of your previous software you've been asked to extend the program to have more functionality. 

In particular, the administrator is tired of writing emails to each of the students and would prefer instead to automate this entire process. 

{% next %}

## Enrolment

When we create objects we can use the default constructor. This sets each of the variables to their default values (which is normally $'0'$, `false`, or `""`).

We can then go through each of our attributes and manually change these to the values we want them to using setters.

```java
Student alice = new Student();
alice.setName("Alice");
alice.setStudentId(1234567);
alice.setEmail("aliceXtreme@aol.com");
alice.setEnrolmentYear(2021);
alice.setYearOfBirth(1984);
```

What a lot of code to do something so simple...

{% next %}

## Constructors

When we call `new Student()`, it is useful that Java has set the default values, as it stops uninitialized variable errors from being thrown.

Although we haven't put the code below into any of our programs yet, the compiler has automatically created this when we miss it out, and this is what is being called when we say `new Student();`

```java
public Student() {

}
```

{% next %}

## Better Constructors

There is no need for us to have such a simple constructor however, and constructors can take arguments the same as any other method, as well as having class level access (can change `private` variables belonging to that class). For example we could use the constructor like below.

```java
public Student(String studentName) {
    name = studentName;
}
... 
// Separate program
Student alice = new Student("Alice");

```

This enables us to save on some code when creating Student classes, which improves readability of programs all round. 

Change the constructor of the `Student` class so that it takes two `String`s and three `int`s, and creates a new `Student` object without having to call the setter of each of these variables individually, e.g.

```java
Sudent alice = new Student("Alice", "aliceXtreme@aol.com", 1984, 2021, 1234567)
```

{% next %}

## But Wait There's More

In addition to being able to define a constructor, we can define multiple constructors!

This gives wider applicability to constructors, where we may not know all of the information about an object where we create it, or maybe the information given about an object is given in different formats.

For example we might create a `Student` class when the student first applies to the university, we don't know what their student ID is at this point, and when their place is accepted they may choose to defer their placement for a year.

When we define multiple methods with the same method name, but different arguments this is called *overloading* a method.

Create a new overloaded method for the `Student` class which takes only three arguments, two `String`s and an `int` for the birth year for each of these students.

{% next %}

## Functionality of Constructors

Seeing how useful these constructors are, the administrator has asked you to change your program so that we can store all the historic details of students also. This data is mostly the same, but the date of birth for these students is in `String` format such as "01/06/1984". Add a new constructor to your `Student` class which takes three `String`s and two `int`s. 

You will still store the year of birth as an integer however, so you will need to add some more code into this constructor to process this date string and store the year as an `int`.

{% spoiler "Hint"}

`String` classes have a built in method, `split()`. This could be very useful.

The `Integer` class, has a built in method `parseInt()`.

{% endspoiler %}