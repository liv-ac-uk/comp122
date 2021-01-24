# Loops

In almost all imperative programs of any complexity we must repeat a section of code a fixed number of times.

The most common method of doing this in C like languages (such as Java) is with a `for` loop.

{% next %}

## What's It All For?

A `for` loop has the same normal syntax, we define an initial state (setting integer `i` to 0), the state when we should terminate (how we should break out of the loop, when `i=10`), and an action to take on each iteration of the loop (increase the value of `i` by one each time).

```java
for(int i = 0; i < 5; i++) {
    System.out.println("I've said 'Hello there' " + i + " times previously!");
}
```

Complete the program Hello.java so that it prompts the user for an integer, `n`, and then print the phrase to the terminal `n` times. The output of your program should be as below:

```
$ java Hello
2                                               // User Input
I've said 'Hello there' 0 times previously!     // Console Output
I've said 'Hello there' 1 times previously!
```

{% next %}

## As A Matter of Factorial

Factorials are a useful tool in combinatorics, algebra, calculus, probability theory, and number theory. They're pretty neat.

We calculate the factorial of a positive integer `n`by taking the product of all integers from `1` to `n`, denoted by `n!`.

`n! = n \times (n-1) \times (n-2) ... \times 3 \times 2 \times 1`

{% next %}

## Making Arrangements

Take a standard deck of cards, and select all of the spade, non face cards (ace of spades to the ten of spades).

How many unique permutations can we get if we shuffle these cards completely randomly?

We could get a deck of cards, and spend a long afternoon shuffling until we are sure we have found every permutation. Or we could use factorials.

There are $`10`$ possible cards for the top card in our shuffled deck to take. Once we have remove this, there are $`9`$ possible card values the second card could take. Carrying this forward we can see that there there must be $`10!`$ permutations in total.

{% next %}

## Computing Permuting

Instead of calculating this in our heads, let's write a quick program to do the work for us.

Open the file `Factorial.java` and complete the rest of the code to ensure that it compiles, reads in a value of the integer $`n`$ from the user, and prints the value of $`n!`$.

The correct output should be as follows.

```
$ java Factorial
4          // User input
24
```

{% spoiler "Hint" %}

When defining the starting and ending conditions of your for loop, you aren't forced to make your iterating variable start from 0, nor do we have to use `<` for our final value. You could start this from $`1`$ and use `<=` for example...

{% endspoiler %}

{% next %}

## Improving Our Program

Now that we've found out how many different permutations there are, isn't it a good job we didn't do that by hand.

Unfortunately our program still has a flaw...

If we were to add the jack of spades and queen of spades into our deck, how many different permutations are there now?

```
$ java Factorial
12
479001600
```

Now let's add the king of spades into our pile and use your program to compute the new number of permutations. Now use your calculator to calculate $`13!`$...

Fix your program so that it will correctly output the factorial of integers up to $`20!`$.

{% spoiler "Hint" %}

Use an online [decimal to binary](https://www.rapidtables.com/convert/number/decimal-to-binary.html) calculator to see what is $`12!`$ in binary? How about $`13!`$? If we count the number of bits can we use a 32-bit integer to store this value?

{% endspoiler %}

{% next %}

# Arrays

As covered in previous labs, we have a range of primitive data types for the fundamental problems we frequently encounter when programming.

As we often deal with lists of values of the same type, these are built into the language directly as arrays.

We declare these using square brackets, and we must specify the type and size of the array when we create it.

```java
String[] meAlong = new String[7];
long[] johnSilver = new long[10];
int[] niceUpNorth = new int[5]; 
```
{% next %}

## Show Me the Array

Arrays are naturally complimented by for loops, where we may use the property (more on this later) of the array `.length`.

For example we could declare an array of ten integers, and fill the values with the digits `0-9` (remember arrays start at $'0'$ in Java) with the following code:

```java
int[] numbers = new int[10]

for (int i = 0; i < numbers.length; i++) {
    numbers[i] = i
}
```

{% next %}

## Does My Int Look Big In This

Check out the sample code `Largest.java` where we will use for loops and int arrays together.

This program will take an integer input, `n`, from the user and create an array of integers of length `n`. We will then loop `n` times, reading in an integer each time. In a second for loop your program should then calculate which is the largest value of the array, before printing this value to the terminal.

Example Usage:

```
$ java Largest
3       // Input
17
5
10
17      // Output
```

{% next %}

## Submitting

You can check your code with

`check50 liv-ac-uk/comp122/2021/problems/arrayLoops`

And submit with:

`submit50 liv-ac-uk/comp122/2021/problems/arrayLoops`