# Variable Declarations and Types

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

Note how the compiler is helping us here by not only specifying the line the error is in (eg: `Declarations.java:7`) but also the exact part of the line where the error occurs.

Let's go hunt some bugs!

{% next %}

## Variable Declaration

Our first issue occurs at the start of line 7

```java
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

{% spoiler "Hint" %}
A very helpful way of quickly checking this is to double click on the troublesome variable in the editor and press `ctrl + f` (`cmd + f` on macs). How many occurrences are there?
{% endspoiler %}

{% next %}

## Variable Initialization

Our program is nearly working as we would expect it to now, but there remains the problem of what our new weight is.

Many programming languages will set uninitialized variables to 0 or a random value. Java is not one of these, and any variables which have not been assigned a value are guaranteed to throw a compiler error if we attempt to use these.

Assign a value to `newWeight` and recompile your program.

{% next %}

## Success!

Now that we have compiled our program successfully we can run it with:

```
java Declarations
```

Try it with different values of `currentWeight` and `newWeight` to ensure it works as you would expect (don't forget to recompile, or it will simply use the old version of your program)

{% next %}


## Primitive Data Types

As java is statically typed, we need to define our variables correctly before they can be used. We can see that here we have defined each of these to have the type `double`, which is a floating point number which is represented by four bytes (64 bits). 

In object oriented programming we generally define variables to be more complex data types (classes), but there are simple representations for integers, floats, boolean (true or false), and single characters. 

We will use `ints/longs`, `doubles`, and `boolean` variables in our programs extensively, with the other datatypes having slightly less relevance in modern 64 bit operating systems.

A full reference to these can be found in the [official documentation](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html).

{% next %}

## Floating Points

As you may have covered in the previous semester, when programming with numbers we generally use integers (![](img/01.gif)... etc.) or floating point numbers (![](img/02.gif) etc.). At a fundamental level inside the computer, these have to be represented in binary and as there are an infinite number of values between ![](img/03.gif) and ![](img/04.gif), we need to make approximations of some of the real values. 

As a consequence we will not be able to represent all numbers with the numeric Java data types, and this may lead to rounding issues in our code. 

Open the file explorer (by clicking on the home button in the upper left corner of the text editor) and open `FPTestApp.java`.

{% next %}

## Difference of Opinion

By reading through the code, we would expect that as ![](img/05.gif), by adding these values together 10 times we should return ![](img/06.gif). Compile and run FPTestApp to confirm this.

{% next %}

## Summing to 1

As you have seen, the fraction 1 / 10 cannot be represented perfectly in binary, and thus does not sum to 1 perfectly.  

Make ![](img/07.gif) and add this together 3 times. 

Is this equal to 1?

For your final submission change `x = 0.05` and add this together 20 times.

{% next %}

## Subtraction
What do you get when you compute ![](img/08.gif) in Java? How about ![](img/09.gif)? Or ![](img/10.gif) and so on?

Subtraction is particularly problematic in floating point arithmetic, especially when the two numbers are close. 

The original lack of precision from the approximation of the numbers becomes "magnified" because of the subtraction (i.e. the least significant digits suddenly "gain" more significance when one number is subtracted from the other).

{% next %}

## The Trouble of Being Floating Point

Floating point numbers allow us to work with numbers with decimal places, and with far higher values than we can typically use with integers.

However as seen, these come with a risk, and when used in arithmetic, these rounding errors whilst initially insignificant can lead to potentially catastrophic consequences. 

Because of this reason, it is important not to use equality when testing if two floating point variables are the same. This will often return an unexpected result. Instead, you should take the absolute difference between the two values, and ensure it is less than a small reference number. This can be done using the Math library (more on that later).

```java
double_1 == double_2 // Returns False
Math.abs(double_1 - double_2) < 0.000001; // Returns True
```
{% next %}

## Dealing With Floating Point

One take-home lesson here is that floating point arithmetic on a computer is not necessarily what you want it to be or expect it to be (although this can depend upon the programming language you are using).

There is a [commonly retold urban legend](https://www.snopes.com/fact-check/the-salami-technique/) of programmers in large corporations surreptitiously stealing huge sums of money by diverting these small rounding errors to their personal accounts. Please do not attempt to embezzle money with this technique. This is against university policy.

For the mathematically inclined, some recommended reading is David Goldberg's [What Every Computer Scientist Should Know About Floating-Point Arithmetic](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html)

{% next %}

## Some Applications of Floats

Pi is a beautiful, transcendental number which has far reaching applications to almost all areas of mathematics, physics, computer science, and philosophy. Others would argue it is roughly equal to ![](img/11.gif). 

We can use approximations of ![](img/12.gif), and the division ![](img/13.gif) leads to a number which is within 0.04% of the true value.

Rather than redefining our own value of ![](img/12.gif) which is guaranteed to introduce some error, it is preferable to use a more precise value. Luckily there is one built into the Java standard library.

## Importing Pi

We often wish to perform mathematical operations in our code, and unsurprisingly Java comes with lots of helpful functions in the [Math package](https://docs.oracle.com/javase/9/docs/api/java/lang/Math.html), which can be imported with:

```java
import java.lang.Math
```

Once we have this in our code, we may use the closest possible double value to ![](img/12.gif) with:

```java
Math.PI
```
{% next %}

## Using Pi

Open the `SimpleCircle.java` program.

You will see that we have a mostly complete program which prints the area and circumference of a circle. Finish this program to ensure that we return the right values.

{% spoiler "Hint" %}

Recall that the area of a circle is ![](img/14.gif), and the circumference is ![](img/15.gif).

{% endspoiler %}

{% next %}

## Pythagoras's Theorem

Recall the Pythagorean theorem which states that the sides of a right angled triangle labelled `a` and `b` in the diagram (where `c`) is the length of the side opposite the right angle), satisfy the relationship ![](img/16.gif).

![Pythagoras](img/pythagoras.png)

Complete the program `Pythagoras.java` which will compute and display the value of ![](img/17.gif) when `a=3` and `b=5`.

{% spoiler "Hint" %}

There is a square root function in the Math package which it would be wise to use!

{% endspoiler %}

{% next %}

## The Law of Cosines

When we do not have a right angled triangle, but we do have the values of `a`, `b`, and the angle between these ![](img/17.gif), we can see that the relationship between `c` and these values is given by the [Law of Cosines](https://www.wikipedia.org/wiki/Law_of_cosines)

![](img/18.gif)

![Cosines](img/loc.png)

Complete the program Cosines.java which will compute `c` given the values of `a=3`, `b=5`, and `theta = (2 * Math.PI) / 3` (in radians). 

{% next %}

## Submission

Submit your solution to this exercise through Canvas/CodeGrade as before.

