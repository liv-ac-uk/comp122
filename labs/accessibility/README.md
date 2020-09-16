# Method Access
In the last lab we implemented the `Student.java` class, here we will explore this class in a bit more detail.

In the previous lab all of our methods and attributes were simply made public, but in general this does not provide much assurance that other users will misuse our application.

## Change of Hands
You should have implemented a `public int grade;`, which allows the lecturer to change the grade of the student. In the following year the lecturer has left the university and the codebase has been passed to an administrator who is a much worse coder, but is still keen to use software to save time. 

Instead of using the `updateGrade()'` method, the new administrator has decided to set the `grade` attribute manually for each student. They also have an old keyboard where the $`0`$ key often gets stuck.

```java
...
alice.grade = 72;
bob.grade = 9000;
charlie.grade = 20000;
```

This is causing some angry emails.

## Saving People From Themselves

When designing software we cannot trust the end user. If software can be accidentally misused, it will be misused eventually. *It is our responsibility as engineers to prevent this from happening*. 

Luckily we can force people to use our software correctly with access modifiers.

## Privacy is Important

There are four access modifiers in Java, `public`, `protected`, no modifier, and `private`. For now let us look at `public` and `private`.

`public` variables, as you have seen now, are publicly accessible to change in any part of the code, which enables other people to make a lot more mistakes.

In contrast `private` variables cannot be seen by the instantiated objects. Trying to access these directly will throw an exception (which is a good thing). 

Are `private` variables useless then? No, because these *can* be changed within the class body. We can assume that the end user won't be able to modify our class, and therefore we can build error correction into our program from the start. This gives us full control over how these variables can be interacted with.

## Saving the System

You've been called in to streamline the system. Going forward the module will have four assignments, each worth 25% of the total grade. 

We want there to be two array attributes for our student classes, `hasSubmitted` and `grade`. These *should not* be changeable manually, but will enable us to tell quickly how many of the students have submitted an assignment. 

Having learned from the past mistakes, once we have created a student, there should only be a single method we can call to change the attributes of the student.

This method will take the assignment number and grade from the user, and update the appropriate entry in the `private grade;` array, as well as marking the assignment as complete in `hasSubmitted`.

## Error Checking and Accessing

Note in the code stub that we have added some error messages, do not change these, but insert the rest of the code to make sure that the error checking has been implemented properly.

Whilst it can be useful to keep `private` attributes which are only used by internal methods, here the students would like to see their grades eventually.

For this purpose we have implemented some "getter" methods. Make sure that the return types for these match the attribute type.

Additionally to save the administrator some calculation, they also wish for the program to sum up the grades for them. 

*These getter methods will `return` the values, do not print these to the console*