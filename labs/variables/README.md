# Lab 2. Variable Declarations and Types

## Declaring Variables

Despite being an incredibly important saying, in general we wish our programs to be able to do more than say hello!

At the right we can see a simple program which we will use to calculate the difference in two weights, go ahead and compile it using 

```
javac Declarations.java
```

{% next %}

## Everything's gone wrong

Hmm, that doesn't seem to work quite as we were expecting...

We can see that the compiler has found three errors in our code, which are given to us in the order in which the compiler has found them.

```
Declarations.java:7: error: cannot find symbol
        weightDifference = newWeight - curentWeight;
        ^
  symbol:   variable weightDifference
  location: class Declarations
Declarations.java:7: error: cannot find symbol
        weightDifference = newWeight - curentWeight;
                                       ^
  symbol:   variable curentWeight
  location: class Declarations
Declarations.java:10: error: cannot find symbol
        System.out.println(weightDifference); 
                           ^
  symbol:   variable weightDifference
  location: class Declarations
3 errors
```

Note how the compiler is helping us here by not only specifying the line the error is in (eg: ```Declarations.java:7```) but also the exact part of the line where the error occurs.

Let's go hunt some bugs!

{% next %}

## Variable Declaration

Our first issue occurs at the start of line 7

```
Declarations.java:7: error: cannot find symbol
        weightDifference = newWeight - curentWeight;
        ^
  symbol:   variable weightDifference
  location: class Declarations
```

Here we have told the compiler that we wish to subtract two numbers and save the result to a new variable. However java (and many other compiled languages) does not allow us to dynamically assign values to variables (as we can in python). And we need to be explicit in the type of the variable, as we have done in the previous two lines.

Fix this and recompile your program

{% next %}

## The Worlds Most Common Bug

You will have encountered this bug in your other programs (often at 2 A.M. the night before an assignment is due). Everything should compile perfectly but for some reason it keeps returning errors.

Check the code carefully and see where it could be going wrong. 

{% spoiler %}
A very helpful way of quickly checking this is to double click on the troublesome variable in the editor and press ```ctrl + f``` (```cmd + f``` on macs). How many occurrences are there?
{% endspoiler %}

{% next %}

## Variable Initialization

Our program is nearly working as we would expect it to now, but there remains the problem of what our new weight is.

Many programming languages will set uninitialized variables to 0 or a random value. Java is not one of these, and any variables which have not been assigned a value are guaranteed to throw a compiler error if we attempt to use these.

Assign a value newWeight and recompile your program.

{% next %}

## Success!

Now that we have compiled our program successfully we can run it with:

```
java Declarations
```

Try it with different values of currentWeight and newWeight to ensure it works as you would expect (don't forget to recompile, or it will simply use the old version of your program)

## Test Your Code

Execute the below command to evaluate the correctness of your code using `check50`, but be sure to compile and test it yourself!

```
check50 liv-ac-uk/comp122/2021/labs/variables
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 Hello.java
```

{% next %}

## How to Submit

Execute the below, logging in with your GitHub username and password when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your password.

```
submit50 liv-ac-uk/comp122/2021/labs/variables
```
