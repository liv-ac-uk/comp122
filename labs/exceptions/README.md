# Exceptions

This lab aims to cover Exceptions and Exception Handling, and following completion you should understand the rationale behind Exceptions,
how to use try/catch, throw, multi catch and finally blocks. For further understanding of this material,
you can find Oracle's Exceptions tutorial at the following address: https://docs.oracle.com/javase/tutorial/essential/exceptions/index.html.
We will cover most of the material found there excepting for try with resources, which will be covered in the I/O lab next week.

Note: The document references local tests, you can check your code locally using SelectFromTest and ExceptronTest like so:
```
java SelectFromTest
java ExceptronTest
```

The latter has the following specific tests
0-5 that can be run like so:
`java ExceptronTest <Test Number>`

Different sections have relevant tests which will be referenced later on.


## What is an Exception?

An Exception is defined by Oracle as an event that occurs during the execution of a program that disrupts the normal flow of instructions. 
Exceptions can thus be though of at a high level as errors that occur during the Runtime of a program, as opposed to a syntactic error
that prevents compilation i.e. a compile time error. 

Digging a bit deeper, there is a root class Exception from which all other Exception classes inherit. We categorize Exception and its children
into two categories: Runtime Exceptions and Checked Exceptions. 
Runtime Exceptions inherit from the RuntimeException class and are usually triggered
by catastrophic errors from which the program should not recover. Examples of this are the NullPointerException and ArrayIndexOutOfBoundsException
which we will discuss in detail below. These errors are typically the result of programmer error.

Checked Exceptions are all other Exception classes that don't inherit from RuntimeException. These exceptions
are triggered by less catastrophic events from which the program potentially could recover. An example of these exceptions
is the IOException, which can be triggered while reading/writing from files. Imagine an instance where we are reading data line by line from
a file with thousands of lines. If one line is malformed, while the others are correct, we may wish to catch and log the error in the one malformed line
while still processing the others. 

Beyond philosophical differences, a technical detail to note is that in order to throw (discussed later) a Checked Exception you must explicitly add the
"`throws` (name of your Exception)" to the top of the function from which you are throwing. This is unnecessary for Runtime Exceptions, as they can be thrown
by default.



## ArrayIndexOutOfBoundsException and NullPointerException

A couple of Exceptions many of you will have already made unfortunate acquaintance with are the ArrayIndexOutOfBoundsException
and the NullPointerException.

The ArrayIndexOutOfBoundsException is the easier of the two to understand. This exception is triggered when you attempt to retrieve an element from
an array with an out of bounds index. The inbounds indices are those inclusively ranging from 0 to the length of your array subtracted by 1
i.e. [0, 1, 2, ..., n-1]. So if your program tries to access an indices greater than n-1 or less than 0, the exception gets thrown.
This error can occur in many circumstances, but the most common cause for an ArrayIndexOutOfBounds exception is going to be a mistake 
in a for loop containing the actual source of the exception.

NullPointerExceptions are a bit trickier. The `null` value is the default value of all classes which inherit from `Object`.
This includes all non-primitives such as Strings and arrays.
It does not include primitives, such as int, float, etc. who have a default value, such as 0 for int.
As per the javadoc (https://docs.oracle.com/javase/9/docs/api/java/lang/NullPointerException.html) the NullPointerException is
thrown "when an application attempts to use null in a case where an object is required. These include:
* Calling the instance method of a null object.
* Accessing or modifying the field of a null object.
* Taking the length of null as if it were an array.
* Accessing or modifying the slots of null as if it were an array.
* Throwing null as if it were a Throwable value."



The first three reasons will be the likeliest culprits in your code, and the biggest root issue in this class so far has been assigning a value to a class variable
out of a class context (e.g. main) rather than in a class context (e.g. a constructor). For more on this, you can go to the discussion board and view
the pinned topic "Common NullPointerException Errors".


## SelectFrom

Examine the provided Java class, `SelectFrom.java`. It is supposed to have a class `SelectFrom` which has a constructor that takes a list of arguments, 
all assumed
to be integers, which are added to `arrayOfNumbers`. The `selectFromArray` function then takes an index i, returning -1 if the index is out of bounds
but otherwise returning the ith element of `arrayOfNumbers`. At the moment, however, there are a couple errors that will trigger a NullPointerExceptions
and an ArrayOfIndexOutOfBoundsException. 

Run `SelectFrom` from the terminal. When you run it, an error is spit out to the console informing you of the Exception. This is a partial
printing of the stack trace for the exception, which can be fully printed by catching the exception and calling the exception's `printStackTrace()`
function. Notice how the stack trace tells you the lines of code where the error occurred. Stack traces are consequently very useful
for debugging the source of exceptions. Generally speaking, the first line of the stack trace will be the most important, as this is where the Exception
was encountered during execution. However, the reason for that exception may have occurred on another line, so you'll need to trace the steps of your 
program
that lead to the line that triggered the exception. An aside, when an exception
occurs in an external library you should keep reading from the top down until you find the line where your code is calling the library function.

Your first task is to fix `SelectFrom` such that it passes the test in the provided `SelectFromTest.java` file. Note that you do not have to call check50
to run this, for this week the tests are provided locally and return messages rather than using JUnit. The standard JUnit tests will still be called
on submission to check50, but if you pass the tests locally you should pass the tests on check50.

## try-catch
So far when we've encountered exceptions they've propogated all the way up to main and killed the program. For RuntimeException(s)
this is fine, but what about for Checked Exceptions? Further, what if we just generally want a more graceful way of handling things rather than the program
blowing up? This is where try-catch blocks come in.

When a block of code is surrounded by a try block, it will try and run the code, and, if no exceptions are encountered will
run the process as expected. If an exception is encountered, however, it kills the process in the try section,
and an Exception is thrown to (usually) be handled by an accompanying catch
block(s). The catch block(s) decides what to do dependent upon the exception encountered. You can see an example of this in SelectFromTest.java,
where the file tries to run your test but fails you if an exception is thrown into the catch Blocks. 

Note that any variables declared in the try block will be scoped such that they can only be accessed in the try block. This
even means that such variables are *not* accessible even in the catch blocks. Consequently, if you want a variable that can be accessed outside
of the try block, you need to declare it beforehand like so:

```
MyClass mc = null; //we could instantiate here, but instead we'll declare and set to null so compiler won't complain that mc might not be assigned
try{
    mc = new MyClass; //we'll instantiate here
    doSomethingWithMyClass(mc)
} catch(Exception e) {explainMyClassError(mc)}
doSomeMoreStuffWithMyClass(mc); //if it still null, we'll probably get a NullPointerException now
```


## Exceptron
To demonstrate try-catch, we will modify the provided program ExceptronPlatform.java. Exceptron is a class whose primary purpose is as it sounds:
it throws exceptions. Specifically, it has preloaded scenarios dependent upon an index that decides which exceptions to throw, and then runs
these exceptions with the aptly named function doSomeStuff(). 

For now, we'll keep it simple. In the runExceptron function uncomment exceptron.doSomeStuff(). Now, wrap this function in a try catch block,
with the `catch` catching `Exception e`. If you are unsure of what this looks like, refer to the try-catch block in SelectFromTest.java. In the catch block,
return the String `e.toString` + "\n". The Exception's toString function returns the name of the exception followed by a colon and then a message often
shedding light on why the exception occurred. The "\n" is just a newline.

If the catch block is not reached, runExceptron should return "Everything's Fine\n". Note that any code after a try-catch block runs as normal unless
the catch block explicitly decides to return from the function or throw an Exception. From the instructions above you should return a String, 
but if instead you merely printed the String the code would pick
up at the next line after the try-catch block.

To test your code, you can use ExceptronTest.java. You can run specific tests by adding the test number as the command line argument. If this
argument is omitted it will run all the tests. Once the above is completed your code should pass tests 0 and 1.

## Multi catch and throws
What we have just implemented is a General Exception handler. Because it catches the root class Exception, it will actually catch *all* possible exceptions.
Sometimes, however, we may want to have behaviour for when specific exceptions are encountered. Fortunately, the try-catch block can be expanded to 
have multiple catch blocks. An example of this can be seen in SelectFromTest.java. The catch blocks are executed in the order from top to bottom i.e.
the top block will be checked first and the bottom block will be checked last. The catch blocks have to be ordered such that any type of Exception caught
is not a parent class of a block below. Specifically, the root Exception must always be at the bottom, since it is the parent of all other exceptions. 
To demonstrate this, try moving the root Exception to be the top block in SelectFromTest.java and try to recompile. It won't work, because
the other catch blocks are now unreachable code which is a Java crime.

Back in `ExceptronPlatform`, modify the try-catch block to catch two additional classes, SQLException and SuperCoolException. You'll need to import
SQLException so add the following to the top of your code:
`import java.sql.SQLException`

SuperCoolException is actually a custom Exception included with your code. Examining it, you'll notice all it does is extend Exception and it contains
only a Constructor that allows a message to be passed in. There is obviously more stuff you can do when extending Exception, and if you want to mess
around with it you can use the following javadoc as a guide: https://docs.oracle.com/javase/7/docs/api/java/lang/Exception.html. However, SuperCoolException's
implementation is pretty much all you'll need to do to make a custom exception in the upcoming assignment.

Like before, return e.toString() + "\n" from these catch blocks. Your code should now pass test 2 in ExceptronTest.

Right now, because we have the general Exception handler we are going to catch and kill catastrophic Runtime Exceptions too. Let's now modify
our block to catch `RuntimeException`(s). When we catch one of these, we will throw the exception out of the function. To do this,
simply employ the `throw` keyword followed by your Exception object e.g. (`throw e`). 

A reasonable question one might have: if I throw an exception from a catch block catching a RunTimeException, will it then be caught by the 
catch block below that catches all exceptions? The answer is no. Similarly, one might wonder if an exception can "fall through" a catch block, 
that is to say
do something specific for a child class in the block associated with that child class but still have it reach the catch all block where further
logic is performed. This also isn't possible.
Once an exception is thrown out of a try block, it is caught by the first block that either it is exactly or is a child of, and from that block
you can throw, return from the function, or allow the program to continue onto the code after the try-catch blocks. None of the other catch blocks
in that try-catch are involved. If you wanted to emulate the behaviour from the two scenarios above, you could nest try-catch blocks like so:

```
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


Upon completion of the section above, your code should now pass tests 2 and 3 in ExceptronTest.



## Let's Wrap it in a For Loop
We're almost done. We're now going to emulate the example I gave previously for IOException. Specifically, we are going to process IOExceptions
until a certain number of failures has been encountered, at which point we will throw out of the function and kill the program.

Wrap the try-catch block in a for loop that iterates from 0 to `exceptron.getScenarioLength()`. Also, create an empty String, which we'll call
`messages`, before the loop. Now in your catch blocks where you are returning Strings, instead add these Strings to `messages`. Finally,
add an additional catch block for IOException. Note that IOException is a Checked Exception, hence we need *throws IOException* after the signature of `runExceptron`. This is already
done for you.

In this block, check the exception's message with the function `ioe.getMessage()`, assuming your IOException is named ioe. If the message
is "FATAL ERROR", then throw the IOException. Otherwise, like the other Checked Exceptions add to messages ioe.toString() + "\n".
Also, don't forget that if no exceptions
are encountered we return "Everything's Fine\n". How can we know no exceptions were encountered? `messages` would be empty, right?
Can we check this somehow?

Note: To check String equality in Java don't use ==. Use the String function `equals()`.

When your code is working, you should pass test 4 in ExceptronTest.

## Finally
We `finally` near the end of the lab. I am not a big pun guy like the normal lab author, but there's one so we can maintain consistency.

`finally` blocks are included after try-catch blocks and any code in a `finally` block will *always* be executed, even if we have thrown out of the function.
For example, consider if we had the following:
try{
    doSomething()
} catch(Exception e) {
    throw e;
} finally {
    alwaysDone()
}

When the exception is encountered it is thrown out into the next enclosing space, typically the function itself, and it will continue to propogate up through
calling functions until it is handled by a catch block or it is thrown out of main and kills the program. After it is done propogating, but before it potentially kills the program,
the control flow of the code
circles back to the finally block and executes whatever code is within it, in this case `alwaysDone()`.
This can be useful if there is some house cleaning or resource management you
know you'll always need to do.

To finish off, wrap the for loop from above in a try statement, and then follow this try statement with a finally statement. Note, you don't actually have to have 
a catch associated with a try block. In the `finally` block, call the function
`exceptron.goodBye()`. 

Once you have done this, you should pass test 5 and thus all tests in ExceptronTest.
## Submission
Copied from above.
Note: The document references local tests, you can check your code locally using SelectFromTest and ExceptronTest like so:
```
java SelectFromTest
java ExceptronTest
```

The latter has the following specific tests
0-5 that can be run like so:
`java ExceptronTest <Test Number>`

submit via:

```
submit50 liv-ac-uk/comp122/2021/problems/exceptions
```