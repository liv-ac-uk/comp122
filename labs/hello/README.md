# Lab 1. Hello!

## Listing Files

Hello, world! At right, in the *text editor*, is the very first program we wrote in Java, in a file called `Hello.java`.

Click the folder icon, and you'll see that `Hello.java` is the only file that's present at the moment. Click the folder icon again to hide all that.

Next, in the *terminal window* at right, immediately to the right of the dollar sign (`$`), otherwise known as a *prompt*, type precisely the below (in lowercase), then hit Enter:

```
ls
```

You should see just `Hello.java`? That's because you've just listed the files in that same folder, this time using a command-line interface (CLI), using just your keyboard, rather than the graphical user interface (GUI) represented by that folder icon. In particular, you *executed* (i.e., ran) a command called `ls`, which is shorthand for "list" (it's such a frequently used command that its authors called it just `ls` to save keystrokes). Make sense?

Here on out, to execute (i.e., run) a command means to type it into a terminal window and then hit Enter. Commands are "case-sensitive," so be sure not to type in uppercase when you mean lowercase or vice versa.

{% next %}

## Compiling Programs

Now, before we can execute the program at right, recall that we must *compile* it with a *compiler* (e.g., `javac`), translating it from *source code* into machine executable binary code.
Execute the command below to do just that:

```
javac Hello.java
```

And then execute this one again:

```
ls
```

This time, you should see not only `Hello.java` but `Hello.class` listed as well (you can see the same graphically if you click that folder icon again)? That's because `javac` has translated the source code in `Hello.java` into java *bytecode* in `Hello.class`.
Bytecode can be interpreted by the Java Virtual Machine (JVM).

Now run the program by executing the below. Notice that the parameter is just the name of the class, so not `Hello.class` nor `Hello.java`.

```
java Hello
```

Hello, world, indeed!

{% next %}


## Classpath

Sometimes you may want to separate the directories containing source code and compiled bytecode, for example in large projects.
Let's remove the file `Hello.class` and compile `Hello.java` again, this time saving the bytecode in a separate directory called `build`.
Execute the commands below.

```
rm Hello.class
```

This will remove the bytecode file. Alternatively you can also delete that file via the file tree GUI.
Now compile the code again like this.


```
javac -d build Hello.java
```

Take care not to overlook any of those spaces therein! Then execute this one again:

```
ls
```

You should now see not only `Hello.java` but also a directory `build/` listed as well? That's because `-d` is a *command-line argument*, sometimes known as a *flag* or a *switch*, that tells `javac` where to output its result. In this case we gave it the parameter `build`, causing it to create that directory and the bytecode file `build/Hello.class`.

Let's try to execute our program once more.

```
java Hello
Error: Could not find or load main class Hello
Caused by: java.lang.ClassNotFoundException: Hello
```

What happened? We started the java interpreter and told it to execute a class called "Hello".
By default, it will only look for classes in the current folder, so does not find our class.
Execute the below to tell it where to look for class files.
This uses the `-cp` switch (for "classpath") and passes it the name of the directory containing our byte code.

```
java -cp build Hello
```

Hello there again!

{% next %}


## Getting User Input

Suffice it to say, our program is boring because it only ever prints `hello, world`. Let's personalize it a bit, just as we did in class.

Modify this program in such a way that it first prompts the user for their name and then prints "hello, so-and-so", where `so-and-so` is their actual name.

As before, be sure to compile your program with:
`javac Hello.java`
and execute your program, testing it a few times with different inputs, with `java Hello`.

### Staff's Solution

You can try out our demo implementation of this problem to see how we expect the program to behave.
Just execute `java Hello` within
[this sandbox](https://bit.ly/3jYk0RQ).

### Hints

#### Don't recall how to prompt the user for their name?

You can use a [`Scanner` to get user input](https://www.w3schools.com/java/java_user_input.asp) as follows.

```java
Scanner myScanner = new Scanner(System.in);
String name = myScanner.nextLine();
```

The first line actually creates a Scanner object called `myScanner`.
The second line calls the method `nextLine` on that scanner, which will cause it to prompt the user for a string,
and stores the result in a new variable called `name` of type `String`.

#### Error: Cannot find symbol? 

Are you getting an error message like this when trying to compile the code?

```
Hello.java:6: error: cannot find symbol
        Scanner input = new Scanner(System.in);
        ^
```

This is the compiler telling you that your code uses a name "Scanner" that has not been introduced.
In order to make the name "Scanner" known to the compiler, remember to import the class at the top of your source code.

```java
import java.util.Scanner;
```


### How to Test Your Code

Execute the below to evaluate the correctness of your code using `check50`, but be sure to compile and test it yourself!

```
check50 liv-ac-uk/comp122/2021/labs/00_hello
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 Hello.java
```

{% next %}

## How to Submit

Execute the below, logging in with your GitHub username and password when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your password.

```
submit50 liv-ac-uk/comp122//2021/labs/00_hello
```
