In the last labs we implemented a `Student` class. Here we will explore this class in a bit more detail.
Previously, all our methods and attributes were simply made public, but in general this does not provide much assurance that other users will misuse our application.


## Change of Hands
Your student class has a `public int grade;`, which allows the lecturer to change the grade of the student. In the following year the lecturer has left the university and the codebase has been passed to an administrator who is a much worse coder, but is still keen to use software to save time.
Instead of using the `updateGrade()` method, the new administrator has decided to set the `grade` attribute directly for each student. 

```java
...
alice.grade = 72;
bob.grade = 9000;
charlie.grade = 20000;
```

They also have an old keyboard where the <kbd>0</kbd> key often gets stuck.
This is causing some angry emails.

When designing software we cannot trust the end user. If software can be accidentally misused, it will be misused eventually. *It is our responsibility as engineers to prevent this from happening*.
Luckily we can force people to use our software correctly with access modifiers.

{% next %}

## Privacy is Important

There are four access modifiers in Java:

* `public`
* `private`
* `protected`
* no modifier

For now let us look at `public` and `private`.

`public` variables, as you have seen now, are publicly accessible to change in any part of the code, which enables other people to make a lot more mistakes.
In contrast, `private` variables cannot be seen by other instantiated objects. Trying to access these directly will throw an exception (which is a good thing).
Are `private` variables useless then? No, because these *can* be changed within the class body. We can assume that the end user won't be able to modify our class, and therefore we can build error correction into our program from the start. This gives us full control over how these variables can be interacted with.



{% next %}

## Your turn: Encapsulation to the rescue!

You've been called in to streamline the system. Going forward 
we want there to be two attributes related to coursework in our student class: `hasSubmitted` and `grade`. These *should not* be changeable directly.

Having learned from the past mistakes, once we have created a student, there should only be a single method we can call to change the grade of the student.

This method will take a grade as an argument and update the appropriate entry in the `grade` attribute and mark the assignment as submitted in the `hasSubmitted` attribute.
To make sure that only valid grade values are inputted, the method should check
if the grade is between 0 and 100 and complain otherwise.
This should be done by printing an error as below to the terminal and by not further setting attribute values.

```java
public void updateGrade(int newGrade) {

    // ensure a valid grade has been entered. Otherwise...
    System.out.println("Enter a grade from 0-100.");
    return;
    
    // otherwise set grade and hasSubmitted.
```

{% next %}

Whilst it can be useful to keep `private` attributes which are only used by internal methods, here the students would like to see their grades eventually.
For this purpose we will implemented a "getter" method `getGrade()`. 
*This should method `return` the value. Do not just print these to the console*.

Once done, we have a nicely controlled way to update and read the `grade` attribute in the Student class.

To complete the exercise, make all other attributes `private` as well and add "getter" methods for each. Make sure that the return type for these match the respective attribute type.
Now, users (code outside the class context) can read the attribute values indirectly by calling getters, but they cannot modify these values at all, as they were set *only* in the constructor method and do not have "setters" like the `updateGrade` method.

## Submission

Submit your solution to this exercise through Canvas/CodeGrade as before.

