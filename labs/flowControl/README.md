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

In our Gregorian calendar, a leap year is a year that is divisible by `4`, except if it is also divisible by `100`, in which case it's a leap year only if it's divisible by `400`. So `1980`, `2000`, and `2016` are all leap years, while `1900`, `2001`, and `2018` are not.

Initial code for the program LeapYear.java has been given. When run the user will input a year, which will be read in as an integer (`myScanner.nextInt();`). Implement the rest of the function isLeapYear which will use Java's `if-then-else` construct to return a boolean value from the function and print this to the console. Do not modify the `main()` method.

{% spoiler "Hint" %}
Use the modulo operator `%` to test if a number divides perfectly by another. `n % 400` returns the remainder when `n` is divided by `400`, so `(n % 400 == 0)` evaluates to `true` if and only if `n` is exactly divisible by `400`.

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

## Submission

These programs will be tested automatically against a range of test cases, so ensure that the output matches the examples given otherwise these are guaranteed to fail.

Once you have completed these exercises submit these in the usual way

`check50 liv-ac-uk/comp122/2021/labs/leapYear`

`submit50 liv-ac-uk/comp122/2021/labs/leapYear`
