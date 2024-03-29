# Exceptions

This lab covers Java's exception handling mechanism. Following completion you should understand the rationale behind exceptions, how to use try/catch, throw, multi catch and finally blocks.

For an even more elaborate intro check out [Oracle's Exceptions tutorial](https://docs.oracle.com/javase/tutorial/essential/exceptions/index.html).

{% next %}

## What is an Exception?

An exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions. 
Exceptions can thus be though of at a high level as errors that occur at runtime (when running a program) as opposed to a syntactic error that prevents compilation i.e. a compile time error. 

Digging a bit deeper, there is a root class called [`Exception`](https://docs.oracle.com/javase/8/docs/api/java/lang/Exception.html) from which all other exception classes derive. We categorize `Exception` and its children
into two categories: Checked and unchecked exceptions.

*Unchecked exceptions* are sometimes called "runtime exceptions", as they are those derived from the `RuntimeException` class (itself a subclass of `Exception`). They are usually triggered
by "catastrophic" events. Examples of this are the `NullPointerException` and `ArrayIndexOutOfBoundsException`
which we will discuss in detail below. These exceptions are typically the result of programmer error, and while the program
can recover from them, usually they should be thrown so that the program will halt. Because of this, runtime exceptions can be thrown by default.

*Checked exceptions* are all other exception classes that don't inherit from `RuntimeException`.
These exceptions are often used for less catastrophic events from which the program potentially could recover more easily. An example of these exceptions is the `IOException`, which can be triggered while reading/writing from files. Imagine an instance where we are reading data line by line from a file with thousands of lines. If one line is malformed, while the others are correct, we may wish to catch and log the error in the one malformed line
while still processing the others.

Beyond the philosophical differences with runtime exceptions there is a technical difference: In order to throw a checked exception you must explicitly add the "`throws` (name of your Exception)" to the top of the method from which you are throwing. This allows the compiler to check (hence the name) that a user of your method either handles or re-throws such an exception.

{% next %}


## ArrayIndexOutOfBoundsException and NullPointerException

A couple of exceptions many of you will have already made unfortunate acquaintance with are the   [`ArrayIndexOutOfBoundsException`](https://docs.oracle.com/javase/7/docs/api/java/lang/ArrayIndexOutOfBoundsException.html)
and the [`NullPointerException`](https://docs.oracle.com/javase/7/docs/api/java/lang/NullPointerException.html).

The `ArrayIndexOutOfBoundsException` is the easier of the two to understand. This exception is triggered when you attempt to retrieve an element from an array with an out of bounds index. The inbounds indices are those inclusively ranging from 0 to the length of your array subtracted by 1 i.e. [0, 1, 2, ..., n-1]. So if your program tries to access an indices greater than n-1 or less than 0, the exception gets thrown.
The most common cause for this to happen is a mistake  in a for loop.

[`NullPointerException`](https://docs.oracle.com/javase/9/docs/api/java/lang/NullPointerException.html) are a bit trickier. The `null` value is the default value of all object types, meaning those defined by a class (and thus derive from `Object`.
This includes all non-primitives such as Strings and arrays.
It does not include primitives, such as `int`, `float`, etc. who have a default value, such as `0` for `int`.
A [`NullPointerException`](https://docs.oracle.com/javase/9/docs/api/java/lang/NullPointerException.html) is
thrown "when an application attempts to use null in a case where an object is required. These include:

* Calling the instance method of a null object.
* Accessing or modifying the field of a null object.
* Taking the length of null as if it were an array.
* Accessing or modifying the slots of null as if it were an array.
* Throwing null as if it were a `Throwable` value."


The first three reasons will be the likeliest culprits in your code, and the biggest root issue in this class so far has been assigning a value to a class variable out of a class context (e.g. main) rather than in a class context (e.g. a constructor). 

{% next %}

## SelectFrom

Examine the provided Java class, `SelectFrom.java`. It is supposed to have a class `SelectFrom` which has a constructor that takes a list of arguments, all assumed to be integers, which are added to `arrayOfNumbers`. The `selectFromArray` method then takes an index i, returning -1 if the index is out of bounds but otherwise returning the `i`th element of `arrayOfNumbers`. At the moment, however, there are a couple errors that will trigger a `NullPointerException`
and an `ArrayOfIndexOutOfBoundsException`. 

Compile and run `SelectFrom` from the terminal. When you run it, an error is spit out to the console informing you of the exception. 

```terminal
$> java SelectFrom
Exception in thread "main" java.lang.NullPointerException
	at SelectFrom.<init>(SelectFrom.java:9)
	at SelectFrom.main(SelectFrom.java:21)
```

This is a partial printing of the "stack trace" for the exception, which can be fully printed by catching the exception and calling the exception's `printStackTrace()` method. Notice how the stack trace tells you the lines of code where the error occurred. Stack traces are consequently very useful for debugging the source of exceptions.

Generally speaking, the first line of the stack trace will be the most important, as this is where the exception was encountered during execution. However, the reason for that exception may have occurred on another line, so you'll need to trace the steps of your program that lead to the line that triggered the exception. 

An aside, when an exception occurs in an external library you should keep reading from the top down until you find the line where your code is calling the library method.

**Your task** here is to fix `SelectFrom` such that it this exception is not thrown.
While you're at it, also make the attribute `private` for good measure.

{% next %}

## try-catch

So far when we've encountered exceptions they've propagated all the way up to main and killed the program. For `RuntimeException`(s) this is fine, but what about for Checked Exceptions? Further, what if we just generally want a more graceful way of handling things rather than the program blowing up? This is where try-catch blocks come in.

When a block of code is surrounded by a try block, it will try and run the code, and, if no exceptions are encountered will run the process as expected. If an exception is encountered, however, it kills the process in the try section, and an exception is thrown to (usually) be handled by an accompanying catch block(s). The catch block(s) decides what to do dependent upon the exception encountered. You can see an example of this in `SelectFromTest.java`, where the file tries to run your test but fails you if an exception is thrown into the catch blocks. 

Note that any variables declared in the try block will be scoped such that they can only be accessed in the try block. This even means that such variables are *not* accessible even in the catch blocks. Consequently, if you want a variable that can be accessed outside of the try block, you need to declare it beforehand like so:

```java
MyClass mc = null; // we could instantiate here but instead we'll declare 
// and set to null so compiler won't complain that mc might not be assigned

try{
    mc = new MyClass; // we'll instantiate here
    doSomethingWithMyClass(mc)
} catch(Exception e) {
    explainMyClassError(mc)
}
doSomeMoreStuffWithMyClass(mc); 
// if it still null, we'll probably get a NullPointerException now
```

{% next %}

## Exceptron

To demonstrate try-catch, we have written a class called `Exceptron`. Its primary purpose is as it sounds:
it throws exceptions when one calls its aptly named method `doSomeStuff()`. If you call this method several times, it will always throw some exception but not always the same. Specifically, `Exceptron` has preloaded scenarios (1-8) and dependent upon which scenario given when instantiated, it decides which exceptions to throw.
To be clear, this class is not part of Java. It is just a small demo application that we wrote here.

Let's now modify the provided program `ExceptronPlatform.java`, which interacts with the Exceptron class.
For now, we'll keep it simple. In the `runExceptron` method uncomment `exceptron.doSomeStuff()`.
Now, wrap this method in a try catch block, with the `catch` catching `Exception e`. If you are unsure of what this looks like, refer to the try-catch block in `SelectFromTest.java`. In the catch block, return the String `e.toString()`. The Exception's `toString` method returns the name of the exception followed by a colon and then a message often
shedding light on why the exception occurred.

If the catch block is not reached, `runExceptron` should *return* `"Everything's Fine\n"`. Note that any code after a try-catch block runs as normal unless the catch block explicitly decides to return from the method or throw an exception. From the instructions above you should return a String, but if instead you merely printed the String the code would pick up at the next line after the try-catch block.

{% next %}

## Multi catch and throws
What we have just implemented is a general exception handler. Because it catches the root class `Exception`, it will actually catch *all* possible exceptions.

Sometimes, however, we may want to have behaviour for when specific exceptions are encountered. Fortunately, the try-catch block can be expanded to have multiple catch blocks. An example of this can be seen in SelectFromTest.java. The catch blocks are executed in the order from top to bottom i.e., the top block will be checked first and the bottom block will be checked last. The catch blocks have to be ordered such that any type of exception caught is not a parent class of a block below. Specifically, the root exception must always be at the bottom, since it is the parent of all other exceptions.

In `ExceptronPlatform`, modify the try-catch block to catch two additional classes, `SQLException` and `SuperCoolException`. You'll need to import `SQLException` so add the following to the top of your code:

```java
import java.sql.SQLException;
```

`SuperCoolException` is actually a custom exception included with this lab's starter code. Examining it, you'll notice all it does is extend `Exception` and it contains only a constructor that allows a message to be passed in. There is obviously more stuff you can do when extending `Exception`, for example overloading [any of its existing methods](https://docs.oracle.com/javase/7/docs/api/java/lang/Exception.html). However, `SuperCoolException`'s implementation is pretty much all you'll need to do to make a custom exception in the upcoming assignment.

Like before, return `e.toString()` from these catch blocks.

Right now, because we have the general exception handler we are going to catch and kill catastrophic `RuntimeException`s too. Let's now modify our block to catch `RuntimeException`(s). When we catch one of these, we will throw the exception out of the method. To do this, simply employ the `throw` keyword followed by your exception object e.g. (`throw e`). 

A reasonable question one might have: if I throw an exception from a catch block catching a `RunTimeException`, will it then be caught by the  catch block below that catches all exceptions? The answer is no. Similarly, one might wonder if an exception can "fall through" a catch block, 
that is to say do something specific for a child class in the block associated with that child class but still have it reach the catch all block where further logic is performed. This also isn't possible.

Once an exception is thrown out of a try block, it is caught by the first block that either it is exactly or is a child of, and from that block you can throw, return from the method, or allow the program to continue onto the code after the try-catch blocks. None of the other catch blocks in that try-catch are involved. If you wanted to emulate the behaviour from the two scenarios above, you could nest try-catch blocks like so:

```java
try{
    try{
        
    } catch(SpecificException se){
    doSomethingSpecific(se);
    throw se;
    }
} catch(Exception e){
    doSomethingForEveryone(e);
}
```


{% next %}


## Let's Wrap it in a For Loop
We're almost done. We're now going to emulate the example I gave previously for `IOException`. Specifically, we are going to process `IOExceptions` until a certain number of failures has been encountered, at which point we will throw out of the method and kill the program.

Wrap the try-catch block in a for loop that iterates from 0 to `exceptron.getScenarioLength()`. Also, create an empty String, which we'll call `messages`, before the loop. Now in your catch blocks where you are returning Strings, instead add these Strings to `messages`. Finally, add an additional catch block for [`IOException`](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html). Note that `IOException` is a checked exception, hence we need *throws IOException* after the signature of `runExceptron`. This is already done for you.

In this block, check the exception's message with the method `ioe.getMessage()`, assuming your `IOException` object is named `ioe`. If the message is "FATAL ERROR", then throw the `IOException`. Otherwise, like the other checked exceptions, add the string `ioe.toString()` to `messages`. Don't forget that if no exceptions are encountered we return "Everything's Fine". How can we know no exceptions were encountered? `messages` would be empty, right?
Can we check this somehow?

{% spoiler "Hint" %}
To check String equality in Java don't use `==`. Use the String method [`equals()`](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html#equals(java.lang.Object)). See [this post explaining the difference](https://stackoverflow.com/a/513839/11885326). Basically, `==` compares two objects (Strings) for object identity whereas `String.equals` compares two strings for equality of content.
{% endspoiler %}


{% next %}

## Finally

We `finally` near the end of the lab.
`finally` blocks are included after try-catch blocks and any code in a `finally` block will *always* be executed, even if we have thrown out of the method. For example, consider if we had the following:

```java
try{
    doSomething()
} catch(Exception e) {
    throw e;
} finally {
    alwaysDone()
}
```

When the exception is encountered it is thrown out into the next enclosing space, typically the method itself, and it will continue to propagate up through calling methods until it is handled by a catch block or it is thrown out of main and kills the program. After it is done propagating, but before it potentially kills the program,
the control flow of the code circles back to the finally block and executes whatever code is within it, in this case `alwaysDone()`. This can be useful if there is some house cleaning or resource management you know you'll always need to do.

To finish off, wrap the for loop from above in a try statement, and then follow this try statement with a finally statement. Note, you don't actually have to have a catch associated with a try block. In the `finally` block, call the method `exceptron.goodBye()`. 
