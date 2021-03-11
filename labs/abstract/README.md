# Abstract Classes

Now that we are starting to build up some complexity in our programs, lets start to add some more structure to these to make our code easy to understand.

There are two routes we will be looking at to doing this in this lab, through abstract classes, and interfaces. This will be applied to a similar class hierarchy to the previous lab.

![](img/PersonStudentLec.PNG)

{% next %}

## They're a very abstract person...

In our code, `Person` is a fully instantiable class, which doesn't make sense in this program. Every person we keep track of at a university will have a specific role which we should write a class for. 

Lets make sure that a future coder can't make a mistake here and accidentally include it in a program. 

Modify the `Person.java` class so that it is abstract, and `extend` each of the `Professor`, `Lecturer`, and `Student` classes so they match the class hierarchy.

{% next %}

## Interfaces

Let's now create some more classes for our program to increase the functionality!

We have established, that all of the Persons of faculty need to be sent emails, therefore `Person.java` should definitely implement some email functionality. 

Create a new interface class `Emailable.java`, ensure this includes the method `public void sendEmail();`.

Modify `Person.java` to include a simple implementation of this method, by adding this to the method body of the definition of `sendEmail()`:

`System.out.println(greet());`

{% next %}

## Do you find this arrangement degreeable?

At the end of university, students will be awarded a degree, and there needs to be some method in the `Student` class to show this. 

Create another new interface class `Degreeable.java`.

This interface will contain a single method `awardDegree();`.

Make sure `Student.java` implements this class, and include the following body to the method in `Student.java`.

```java
if totalGrade > 40 {
    System.out.println("You Passed Your Degree, hooray!");
}
```

{% next %}

## Extra Round of Applause for the Liverpoodle

Additionally, from the amount of overtime the university therapy dog Laika, has put in this year, faculty have decided to award her a degree too.

We will need to create a new class for Laika, as she is not a Person.

The class `Dog.java` should implement `Degreeable.java`. There will be a single `boolean` value, `goodGirl = true;`, and the method body for `awardDegree()` should be:

```java
if goodGirl {
    System.out.println("Arruff woof woof. WOOF!");
}
```

{% next %}

## Where's my pay?

As much as teachers find philosophical satisfaction from passing knowledge to the next generation of great thinkers, they would also like to get paid to do it.

Create an interface class `Payable.java`, with a single method `payAmount(int   );`

This should be implemented in `Lecturer.java` (and thus will be inherited by `Professor.java`). Make this method take in a single integer `amount`, and make the body of the method simply print to the terminal as so:

`System.out.println(amount);`

{% next %}

## I wanna bill just like you

The university also likes to take in money as well as give it away. Students must pay to attend, and research councils must pay to fund lecturers and researchers to investigate new fields.

Create an interface class `Billable.java`, again with a single method `payBill();`. The body of this method should again take in the amount to be billed, and simply print this to the console:

`System.out.println(amount);`

Additionally create an entirely new class `ResearchCouncil.java`, which should implement both `Billable` and `Emailable`. To ensure that we can do this make private variables `name`, and `email`, as well as a public method `greet()`. The method body of `greet()` should be:

```java
return "sendto: " + email + "Dear " + name + ",\n";
```

Implement `sendEmail` and `payBill()` as before.

{% next %}

## Diagramatically

The final class diagram of your solution should be:

![](img/CompleteUML.PNG)

{% next %}

## Submission

You can test your code with 

`check50 liv-ac-uk/comp122/abstract/problems/abstract`

And submit your code with:
`submit50 liv-ac-uk/comp122/polymorphism/problems/polymorphism`