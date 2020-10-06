# Lab 3. Program Flow Control in Java
At some point in our programs we need to make decisions, and Java implements similar program flow constructs as other programming languages. In this lab we will implement these core principles.

{% next %}

## The meaning of if

The most basic of these is the `if` statement.

This will evaluate a boolean expression, and _if_ the value of this expression is true then we will execute the next code block.

```
if (BOOLEAN_EXPRESSION) {
  YOUR_CODE_HERE;
}
```
{% next %}

## Or else...

It is good practice to include a statement which executes when our condition fails. The `else` statement. These can be chained together to handle multiple conditions to keep our code organized.

```
if (grade > 70) {
  System.out.PrintLn("Congrats on your first!");
}

else if (grade > 60) {
  System.out.PrintLn("Nicely done, you got a 2:1!");
}

else if (grade > 50) {
  System.out.PrintLn("Looks like you could have passed some more of the unit tests, but your code still passes most. ");
}

else if (grade > 40) {
  System.out.PrintLn("You've passed this lab, but try and make sure you follow the specification closely and make a good attempt at each problem. Semi-functional code is always better than no code at all.");
}

else {
  System.out.PrintLn("You haven't managed to pass this lab, but don't worry as there is still plenty of time to go back and improve. Watch the lecture videos, try to follow what's needed in the labs, and ask the TA's for help in a lab session if there's any concepts you don't get, that's what they're there for!");
}
```

{% next %}

## Leap Years

In our Gregorian calendar, a leap year is a year that is divisible by ![equation](https://latex.codecogs.com/gif.latex?4), except if it is also divisible by ![equation](https://latex.codecogs.com/gif.latex?100), in which case it's a leap year only if it's divisible by ![equation](https://latex.codecogs.com/gif.latex?400). So ![equation](https://latex.codecogs.com/gif.latex?1980), ![equation](https://latex.codecogs.com/gif.latex?2000), and ![equation](https://latex.codecogs.com/gif.latex?2016) are all leap years, while ![equation](https://latex.codecogs.com/gif.latex?1900), ![equation](https://latex.codecogs.com/gif.latex?2001) and ![equation](https://latex.codecogs.com/gif.latex?2018) are not.

Initial code for the program LeapYear.java has been given. When run the user will input a year, which will be read in as an integer (`myScanner.nextInt();`). Implement the rest of the function isLeapYear which will use Java's `if-then-else` construct to return a boolean value from the function and print this to the console. Do not modify the `main()` method.

{% spoiler "Hint" %}
Use the modulo operator `%` to test if a number divides perfectly by another. `n % 400` returns the remainder when ![equation](https://latex.codecogs.com/gif.latex?n) is divided by ![equation](https://latex.codecogs.com/gif.latex?400 ), so `(n % 400 == 0)` evaluates to `true` if and only if ![equation](https://latex.codecogs.com/gif.latex?n) is divisible by ![equation](https://latex.codecogs.com/gif.latex?400).

{% endspoiler %}

{% next %}

## Condensing our code

Often we do not need long chains of `if-else` if we are testing simple values, and it improves code readability to condense simple functions (don't overdo this though).

Uncomment and complete the second method `isLeapYearCondensed()` which will take in a single integer and return a boolean value. This method should contain only one statement, `return(...);`. Use Boolean logical operators, `&&` (and), `||` (or), `!x` (not X), and divisibility checks as before to write a condensed function.

Ensure your code returns the correct values when compiled, as so:

```
$ java LeapYear
2001     // input
false    // output
```

{% next %}

## Whiling away the hours

`while` loops are a core part of controlling the flow of our programs. These will repeatedly execute a block of code _while_ some condition is true.

```
...
boolean lessThanTen = true;

System.out.println("Enter an integer greater than or equal to ten")

while (lessThanTen) {
    myInt = myScanner.nextInt();
    lessThanTen = myInt < 10;

    if lessThanTen {
        System.out.println("That should have been greater than ten, try again...")
    }
}
...
```

{% next %}

## When to while

We should use `while` statements when we do not know how many times a loop will need to run before terminating.

{% spoiler "Hint" %}

We can introduce bugs into our code if we forget to change the condition which is being tested, meaning that the loop runs forever. Infinite while loops can appear as if your program has frozen, when in reality it is executing the same code repeatedly

{% endspoiler %}

{% next %}

## Newtons Method

In `Newton.java`, implement [Newton's method](https://www.wikipedia.com/en/Newton's_method#/Square_root_of_a_number) in the given function `sqRoot()` to give an approximation of the square root of an inputted value of ![equation](https://latex.codecogs.com/gif.latex?n).

This algorithm (also called the "Babylonian method"), approximates ![equation](https://latex.codecogs.com/gif.latex?%5Csqrt%7Bn%7D) by iteratively improving a $`guess`$ for the square root according to the formula:

![equation](https://latex.codecogs.com/gif.latex?new%5C%20guess%20%3D%20%5Cfrac%7B%28n%20/%20guess%29%20&plus;%20guess%7D%7B2%7D)

Until the last two values differ by at most, a given precision ![equation](https://latex.codecogs.com/gif.latex?%5Cepsilon).

For example, suppose you want to approximate ![equation](https://latex.codecogs.com/gif.latex?%5Csqrt%7Bn%7D) up to error ![equation](https://latex.codecogs.com/gif.latex?%5Cepsilon%3D0.0000001). If our initial guess is ![equation](https://latex.codecogs.com/gif.latex?1) , the sequence of guesses would be:

```
1.0
1.5
1.4166666666666665
1.4142156862745097
1.4142135623746899
1.414213562373095
```

These last two numbers differ by less than ϵ\epsilonϵ, so the sequence of guesses stops with the final number as the estimate of ![equation](https://latex.codecogs.com/gif.latex?%5Csqrt%7Bn%7D)​​. By taking ![equation](https://latex.codecogs.com/gif.latex?%5Cepsilon) to be smaller, one can get a better estimate of ![equation](https://latex.codecogs.com/gif.latex?%5Csqrt%7Bn%7D). Of course, this has limits based on the number of decimal places that the computer can store internally.

{% next %}

## Newtons Method

Your code will take in two positive numbers ![equation](https://latex.codecogs.com/gif.latex?n) and ![equation](https://latex.codecogs.com/gif.latex?guess) as input using `Scanner.nextDouble()`. It should calculate an ![equation](https://latex.codecogs.com/gif.latex?%5Cepsilon)-approximation of the square root of ![equation](https://latex.codecogs.com/gif.latex?n), when ![equation](https://latex.codecogs.com/gif.latex?%5Cepsilon%3D0.0000001).

Your function should print the square root of ![equation](https://latex.codecogs.com/gif.latex?n) and the total number of guesses taken (including the initial guess).

```
java Newton
2.0 1.0
6
1.414213562373095
```

{% spoiler "Hint" %}

You may want to use a `while` loop to compute ![equation](https://latex.codecogs.com/gif.latex?new%5C%20guess) and compare it to your previous guess. You can use the function Math.abs() when testing the difference between successive guesses.

{% endspoiler %}

{% next %}

## Submission

These programs will be tested automatically against a range of test cases, so ensure that the output matches the examples given otherwise these are guaranteed to fail.

Once you have completed these exercises submit these in the usual way

check50 liv-ac-uk/comp122/2021/labs/variables
