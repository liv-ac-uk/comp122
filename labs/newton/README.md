# Whiling away the hours

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

## When to while

We should use `while` statements when we do not know how many times a loop will need to run before terminating.

{% spoiler "Hint" %}

We can introduce bugs into our code if we forget to change the condition which is being tested, meaning that the loop runs forever. Infinite while loops can appear as if your program has frozen, when in reality it is executing the same code repeatedly

{% endspoiler %}

{% next %}

## Newtons Method

In `Newton.java`, implement [Newton's method](https://www.wikipedia.com/en/Newton's_method#/Square_root_of_a_number) in the given function `sqRoot()` to give an approximation of the square root of an inputted value of ![equation](https://latex.codecogs.com/gif.latex?n).

This algorithm (also called the "Babylonian method"), approximates ![equation](https://latex.codecogs.com/gif.latex?%5Csqrt%7Bn%7D) by iteratively improving a ![equation](https://latex.codecogs.com/gif.latex?guess) for the square root according to the formula:

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

These last two numbers differ by less than ![equation](https://latex.codecogs.com/gif.latex?%5Cepsilon), so the sequence of guesses stops with the final number as the estimate of ![equation](https://latex.codecogs.com/gif.latex?%5Csqrt%7Bn%7D)​​. By taking ![equation](https://latex.codecogs.com/gif.latex?%5Cepsilon) to be smaller, one can get a better estimate of ![equation](https://latex.codecogs.com/gif.latex?%5Csqrt%7Bn%7D). Of course, this has limits based on the number of decimal places that the computer can store internally.


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


## Submission

These programs will be tested automatically against a range of test cases, so ensure that the output matches the examples given otherwise these are guaranteed to fail.

Once you have completed these exercises submit these in the usual way

```
check50 liv-ac-uk/comp122/2021/labs/newton
```

and submit via

```
submit50 liv-ac-uk/comp122/2021/labs/newton
```
