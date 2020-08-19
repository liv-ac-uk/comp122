# Build Tools

As you can imagine, large software projects often consist of multiple subcomponents and have dependencies on other software. Therefore, compiling and running the most recent version can be complicated and is better done automatically than by hand.

This is where [build tools][wiki-BAT] come in: these are programs that
carry out the tasks of making sure that all dependencies are met, running tests, compiling (sub) components, and help with deployment (assembling packages that can be "shipped to customers").
The idea of automating these things is of course as old as it gets, as this is what programmers are trained to do: automate tedious tasks, so no surprise here. Also unsurprisingly, there are many different such build tools and some are very specialized to a particular programming language.

Let's familiarise ourselves with a very powerful build tool called [Gradle][Gradle]
which is popular with the Java crowd.

{% next %}

## Installing Gradle

### On your own computer
To install gradle on your own computer have a look at the [installation notes][install].
(The online documentation <https://docs.gradle.org> is very detailed and highly recommended by the way!)

### On cs50.io
For the rest of this lab let's assume we are using our browser and are on <https://lab.cs50.io>
or the online IDE <https://ide.cs50.io>.

Install gradle by pasting and running the following snippet into the terminal.

```
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
sdk install gradle
```
In addition we need to set the `JAVA_HOME` path like this.

```
export JAVA_HOME=`ls -d /opt/jdk*`
```

If you are using the IDE then you only need to do this once, as the IDE environment is not reset after every logout.

Now you should be able to run `gradle` on the command line.

```terminal
~/ $ gradle --version

------------------------------------------------------------
Gradle 6.6
------------------------------------------------------------

Build time:   2020-08-10 22:06:19 UTC
Revision:     d119144684a0c301aea027b79857815659e431b9

Kotlin:       1.3.72
Groovy:       2.5.12
Ant:          Apache Ant(TM) version 1.10.8 compiled on May 10 2020
JVM:          13.0.1 (Oracle Corporation 13.0.1+9)
OS:           Linux 4.14.104-95.84.amzn2.x86_64 amd64

```

Cool. We're good to go.


{% next %}


## Setting up a gradle project for a Java application


We will follow the documentation [here][gradle-java] to initialise a new gradle project
and populate it with dummy code for a Java application.
I summarize the important steps here, for more detailed explanations follow the link above.
All listed commands should by typed into a terminal.

1. Create a directory for the project and change into it. 
    ```
    mkdir demo
    cd demo
    ```

2. Make a new gradle project using the step-by-step wizzard.

    ```
    gradle init
    ```

    When asked which type of project to generate, select "application" (2) here.
    As implementation language chose Java (3), and as test framework selece "JUnit Jupiter" (4).
    For the remaining questions just hit enter to select the default value.
    Don't worry if you made a mistake, you can always delete the `demo` directory and start again.

    Afterwards, you should now see that the `demo` directory is populated with several new project files.

    ```
    $ ls
    build.gradle  gradle/  gradlew*  gradlew.bat  settings.gradle  src/
    ```

    These include some configuration files for gradle and source code for a simple hello-world application (under `src`).
    Most interestingly, there are "wrapper scripts", for unix (`gradlew`) and windows (`gradlew.bat`), that can from now on be used to do stuff.

3. Open and have a look at the demo app in `src/main/java/demo/App.java`.

    You will notice that this defines an application class (one with a `main` method).
    which is part of the package `demo` (see line 4).

    This is because gradle has created the project to follow the (sensible) convention to
    store source code in the directory `src/main/java/` and to organize java code into packages.
    In this case there is only one package, called `demo`, to which the App belongs.

    We could compile this class
    using `javac src/main/java/demo/App.java` (which creates a class file `src/main/java/demo/App.class`)
    and run it with `java -cp src/main/java demo.App` (can you explain what happens here?).
    But let's not do that and use gradle to compile and run this program.


4. Run `./gradlew run` from within the `demo` directory. 
    This will run the wrapper script `gradlew` created in step 2. Notice the trailing "w" here.

    What happens now is that gradle does a couple of tasks for us:
    it will compile the code, run some tests on it, and then execute it. In the end, you should see
    something like this on the console:

    ```
    > Task :run
    Hello world.

    BUILD SUCCESSFUL in 3s
    2 actionable tasks: 2 executed
    ```

    Here, `Hello World` is the output of our application.

{% next %}

## Playing with gradle tasks

Gradle actually offers several "tasks" for you to execute.
For example, you can clean your project directory using the `clean` task like this.

```
./gradlew clean
```
This will remove all compiled class files (the directory `demo/build/`).

To compile (but not run) your code you can use the `compileJava` task.
This will compile all java source files in `demo/src/main/java`
and outputs the compiled bytecode files into `demo/build/main`.

```
./gradlew compileJava
```

Executing the application can be done with the `run` task that you have seen before.
Notice that some tasks depend on others, which will called for you automatically.
For example, when we ran the `run` task before, gradle automatically executed
`compileJava` for us.

You can explore other features by browsing the online documentation
or simply calling `./gradlew help` to get you started.

There are many useful tasks readily available,
for example to generate javadoc html, or to run unit tests (more on that later in the semester).
List all available tasks for you project `./gradlew tasks`.

[Gradle]: https://gradle.org
[wiki-BAT]: https://en.wikipedia.org/wiki/Build_automation
[install]: https://docs.gradle.org/current/userguide/installation.html
[gradle-java]: https://guides.gradle.org/building-java-applications/
