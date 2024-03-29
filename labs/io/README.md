# Input and Output (I/O) Part One

This lab will be the first of two covering standard use cases of reading/writing to file. That family of classes involved in Java I/O is quite large, and covering every aspect is
neither feasible or necessary. If you are interested in learning more, you can find Oracle's I/O tutorial [here](https://docs.oracle.com/javase/tutorial/essential/io/).

We will cover a few different approaches to reading and storing text from a text file. You will then apply one
of these approaches to parse text to store it in a helper class, `OurData`, we have written and included for you.

{% next %}


## java.nio.Files

There is a large family of classes dedicated to Java I/O. Consequently, there are in fact several classes in Java
that can be used to read/write files. These classes are usually children of the Reader/Writer class  (with the exception of Scanner, which we will get to next week) and each of them has utility for specific use cases.

To help simplify the use of this menagerie of classes, Java 7 introduced the [`java.nio.Files`](https://docs.oracle.com/javase/8/docs/api/java/nio/file/Files.html) class, which consists of several static function calls that cater to common use cases. Generally speaking, if you have an I/O task to perform, it is a good idea to look at this class before anything else. We will focus on three methods in `java.nio.Files` that assist in the task of reading a text file.
{% next %}

## Reading from File

A classic approach to reading from a text file uses a
[`BufferedReader`](https://docs.oracle.com/javase/10/docs/api/java/io/BufferedReader.html) to read the file line by line, and looks something like this:


```java
File file = new File(filePathAsString);
try(BufferedReader br = Files.newBufferedReader(file.toPath())) {
    String str = "";
    while ((str = br.readLine()) != null) {
        //do some logic with str
    }
} catch(IOException ioe) {
    throw ioe;
}
```
Let's go line by line.

1. The first line of this code creates a `java.io.File `class from a file path String (e.g. "myDirectory/myFile.txt"). 

2. The second line uses the [`Files.newBufferedReader`](https://docs.oracle.com/javase/8/docs/api/java/nio/file/Files.html#newBufferedReader-java.nio.file.Path-) method to instantiate a `BufferedReader`. It takes as its first argument the [`Path`](https://docs.oracle.com/javase/8/docs/api/java/nio/file/Path.html) object
associated to a file, and then allows for optional parameters that alter things like the charset. We omit these so it will have default settings and charset, UTF-8.
This line is an example of [try with resources](https://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html), which is syntactic sugar for a lengthy try/catch construct. By declaring `br` inside the try, we ensure that it will be closed, which prevents resource leaks. If we didn't use try with resources, we'd need to call `br.close()` in a finally block.

3. The third line just initializes an empty String.

4. The strange looking fourth line tries to read the next line of the file into `str` using [`BufferedReader's readLine method`](https://docs.oracle.com/javase/10/docs/api/java/io/BufferedReader.html#readLine()). Once this operation is performed,
the result of that assignment is null checked, and if str has become null we know we've reached the end of the file. So, this is just a loop that says
read every line in as a String until the end of file. A note,`readLine()` discards the trailing newline ("\n"), so if you wanted to reproduce the file's content exactly you would need to add this back to string.

5. The code enclosed by the while loop is where you would do your logic using the newly read str. There is then a catch block that throws an IOException if the BufferedReader runs
into one.

{% next %}

## Alternative approaches

The code above is a perfectly functional way to handle file I/O, but `java.nio.Files` offers a couple of simpler alternatives to cover this use case.

The first, and what is probably most useful, is `Files.readAllLines(path)`, which returns a `List` of every line, in order. That looks like this:

```java
File file = new File(filePathAsString);
ArrayList<String> yourList = (ArrayList<String>) Files.readAllLines(file.toPath());
```

In two lines of code we now have every line of the file, ordered, in an ArrayList we can traverse with a simple for loop. This code practically is just a tidier repackaging of the code above, where the inner loop adds str to a `List<String>` initialized as empty before the try. 

Another two-liner if you just want the whole file as one big String with the white space and new lines of the file preserved, is given below.

```java
File file = new File(filePathAsString);
String yourFilesContent = Files.readString(file.toPath());
```

A couple words of warning are in order.

First, as you can see from their javadoc documentation, both the `readAllLines` and `readString` methods throw `IOExceptions`. This is a checked exception type so you need to throw or catch them (as in the initial example).
Further, these methods are not performance optimized, so if you need to read a very large file in a performance intensive setting (e.g. developing an industry strength library) these aren't the way to go. However, in most cases and for this class both are fine.


{% next %}


## Program Analysis Exercise

### A Data Structure

Now that we know how to read the text content from a file we are almost ready to go about parsing data from it. We will use a class we have written, `OurData` to store this data. OurData is a simple class that emulates the workings of a database. To initialize an OurData object, you use the following line:

```java
OurData ourData = new OurData(fieldNames);
```

Where `fieldNames` is a `String[]` containing the names of the data fields in our database.
To then set a field's value, you would just use the following:

```java
ourData.setField(fieldName,value);
```

A note, this method can take value as a `String`, `int` or `boolean` (it is overloaded for all three signatures). It will then store the value as that data type. 

We can look up an individual field's value and get this back as a String with the following:

```java
ourData.getFieldAsString(fieldName);
```

Finally, we can print a whole data object with the following line:

```java
ourData.printData();
```

We now have everything we need to do the final exercise.

{% next %}

### Your Turn!

Examine the file "programs.txt". It contains Program Descriptions, a form of data describing a computer program being applied to a problem, all of which have 6 fields that 
adhere to the format "fieldName-fieldValue" i.e. the name of the field, followed by "-", followed by the value of the field.
Of these 6 fields, 
- "problem" and "program"  are of type `String`, 
- "program_length", "passed_tests", "total_tests" are of type `int`, and 
- "correct" is of type `boolean`.
Before these 6 fields is `"Program Description n"`, where n corresponds to the Program Description's order in the file, and after these 6 fields is a blank line.


In the included file `IOLabPartOne.java` modify the function `parseStructuredTextFile(Path path)`, where path is the corresponding file path to the file of interest, such that it returns an `ArrayList<OurData>` corresponding to data in the file. You can be assured that the file will be in the same format as `programs.txt`, though the values and number of entries may be different in tests. 


#### Hints

1. You need to read fields into `OurData` as their appropriate type e.g. "program_length" needs to be an `int`, so you'll need its value to be parsed as `int` with `Integer.parseInt` before storing it with `setField("program_length", value)`.

2. Remember that `Integer.parseInt` can throw an exception. Which one?

3. In the case where an `IOException` is encountered you can just re-throw it. The starter code already does this so you do not need to make any changes here.

4. You'll notice the long comments in the starter code, you should read these as they give significant hints on how to approach the problem. If you are confused about the String substring or split functions mentioned in these comments you can consult the String javadoc [here](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html).

#### Testing

We have also included some code in the constructor to help you check your work. Just uncomment it, then compile and run IOLab. If your code is working, the terminal should print output identical to `programs.txt`.
Once you're done, submit your attempt to CodeGrade for more feedback.
