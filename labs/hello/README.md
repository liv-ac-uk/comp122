# Lab 1. Hello!

## Listing Files

Hello, world! On the right you should see two windows: the *text editor* that shows our very first Java program named `Hello.java`, and right below that there is a *terminal window*.

Click the folder icon, and you'll see two files, `Hello.java` and one called `Comp122.class`, which we will use later. Click the folder icon again to hide all that.


Next, in the terminal window, immediately to the right of the dollar sign (`$`), type precisely the below (in lowercase), then hit Enter:

```
ls
```

You should see two files again. That's because you've just listed the files in that same folder, this time using a command-line interface (CLI), using just your keyboard, rather than the graphical user interface (GUI) represented by that folder icon. In particular, you *executed* (i.e., ran) a command called `ls`, which is shorthand for "list" (it's such a frequently used command that its authors called it just `ls` to save keystrokes). Make sense?

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

This time, you should also see a file named `Hello.class` listed as well (you can see the same graphically if you click that folder icon again)? That's because `javac` has translated the source code in `Hello.java` into java *bytecode* in `Hello.class`.
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

You should now see a directory `build/` listed as well? That's because `-d` is a *command-line argument*, sometimes known as a *flag* or a *switch*, that tells `javac` where to output its result. In this case we gave it the parameter `build`, causing it to create that directory and the bytecode file `build/Hello.class`.

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

Suffice it to say, our program is boring because it only ever prints `hello, world!`. Let's personalize it a bit.

Modify this program in such a way that it first prompts the user for their name and then prints "hello, so-and-so", where `so-and-so` is their actual name.

To do this we can use the Comp122 class which has been given in the current folder as so.

```java

System.out.println("Please enter your name");
String name = Comp122.getString();
System.out.println("Hello, " +  name);
```

As before, be sure to compile your program with:
`javac Hello.java`
and execute your program, testing it a few times with different inputs, with `java Hello`.

Just FYI, the `Comp122` class is not the standard way to get user input in Java but a utility we made for COMP122 so that you don't yet have to see all the scary details.
We will look into input and output (I/O) later in the semester.
Notice that you are using this class although you do not have it's source code (`Comp122.java`) file.
This is an early example of the *information hiding* principle: You can use this piece of code without knowing it's internals.

{% next %}

### Staff's Solution

You can try out our demo implementation of this problem to see how we expect the program to behave.
Just execute `java Hello` within
[this sandbox](https://bit.ly/3jYk0RQ).

{% next %}

### How to Test Your Code

Execute the below to evaluate the correctness of your code using `check50`, but be sure to compile and test it yourself!

```
check50 liv-ac-uk/comp122/2021/problems/hello
```

You can run checks as often as you like to get feedback on your code.

{% next %}

## How to Submit

Execute the below, logging in with your GitHub username and password when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your password.

```
submit50 liv-ac-uk/comp122/2021/problems/hello
```

You do not need to perfectly solve or submit every exercise and we will not manually grade these exercises.

However, attendance is worth 10% of the final module grade,
and we use submissions to lab exercises as a proxy for your participation.
You gain one percentage point per week if you submit a reasonable attempt to one of the exercises by Friday 5pm, each week. 

