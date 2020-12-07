# Javadoc -- Well documented code is useful code!

Your code may be amazing but without proper documentation nobody, including yourself, will use and build on it later
(Or do you enjoy reading source code just to see what it does or judge if it's useful to you?).

It is therefore no surprise that the classes in the Java standard library are really well documented:
If you ever searched for specific Java classes or types online, you will have come across documentation pages like [this one on String][String] or [this one on Arrays][Arrays].
Have you ever wondered how they are created and maintained?

Well obviously this is not done by hand!
These pages are automatically generated from the java source code files using a neat tool called *javadoc*.
It comes with the JDK, meaning if you have a Java compiler you will almost certainly also have javadoc installed. Fun fact: Javadoc was one of the very first such documentation generators and is part of the JDK since version 1.0 (Jan 1996)!

{% next %}
### How does it work?
Java code is already quite structured so that it gets past the compiler.
For instance, a classes' superclass, and the precise signatures of its public methods and attributes can be automatically extracted.
To add more info, javadoc will look for special **javadoc comments** and interpret them.

Javadoc comments are basically multi-line comments that start in `/**`, instead of just `/*`.
This way they are ignored by the compiler as it interprets the extra asterisk just as the first symbol of a comment. Javadoc, however considers only those types of comments.
In it you can put any text, HTML code and extra *tags* to document your code.

Let's have a look at an example, the file `StringTools.java` on the right.
It contains two javadoc comments: the first one at the very top which documents the class,
and another one in lines 9 to 20, which documents the method `length`.
These comments also contain some tags which mention the author and version of the code and describe method parameters and return types.

Ignoring for now that the `length` method is incredibly silly, I hope you agree that it is much more understandable -- and thus useful -- than the undocumented `swap` method below (what exactly is meant be swap?!?).

{% next %}

## Generating HTML
Let's fire up javadoc and generate the documentation page for this class.
To do this, open a terminal and enter

```
javadoc -d docs StringTools.java
```

This will generate a whole bunch of files in the `docs` folder.
{% spoiler "Command Parameters" %}
The parameter `-d docs` tells javadoc to create everything in a directory called `docs/`.
If you omit this then it will dump everything in the current folder.

You can also call this on more than just this one file like this:
```
javadoc *java
```

Check out the help page for the javadoc command: `javadoc -h` to see what else it can do for you.
{% endspoiler %}

```
ls docs/
```

Now let's have a look at the generated pages in a browser.

Open a new "Web Browser" Tab by clocking on the plus symbol next to the file and terminal tabs.
This will open a browser that shows the current folder. Clicking on "docs/" will open the file `docs/index.html` and render it. Voilà!

Notice that this page contains the documentation from our two javadoc comments plus some extra info on the class, such as listing its methods.

{% next %}

## Document the remaining two methods

As an exercise, provide javadoc comments for the remaining two methods in our class. Can you figure out just from reading the source code what `swap` means? Reading other people's code is annoying isn't it?

In your documentation, add at least tags to describe the parameters and return values.
There are a [few more tags that javadoc interprets][TAGS] and which you are welcome to use.
Re-generate the HTML pages by executing `javadoc` as above as often as you want.

{% next %}

## Check and submit
You can use the automarker to see if you've overlooked something.

```
check50 liv-ac-uk/comp122/2021/problems/javadoc
```

Submit via

```
submit50 liv-ac-uk/comp122/2021/problems/javadoc
```

[TAGS]: https://en.wikipedia.org/wiki/Javadoc#Table_of_Javadoc_tags
[String]: https://docs.oracle.com/javase/9/docs/api/java/lang/String.html
[Arrays]: https://docs.oracle.com/javase/9/docs/api/java/util/Arrays.html


