# Input and Output (I/O) Part Two

This lab is the second second of our two labs covering standard use cases of reading/writing to file. That family of classes involved in Java I/O is quite large, and covering every aspect is neither feasible or necessary. If you are interested in learning more, you can find Oracle's I/O tutorial [here](https://docs.oracle.com/javase/tutorial/essential/io/).

We will cover the Scanner class, and when/why you would want to use it, and then briefly discuss writing to file.

{% next %}


## Scanner

The [`java.util.Scanner`](https://docs.oracle.com/javase/7/docs/api/java/util/Scanner.html) class provides a way to read formatted data from a file, Stream or String.
When a Scanner is called on a String, it breaks the String up into tokens based off a delimiter which is by default white space. You can then use the scanner to "scan" these tokens using several functions that follow the same format:
`hasNext<type>()`, which checks if the next token matches with the type (e.g. double), and `next<type>()`, which gets that token and moves the scanner onto the next token.

Let's demonstrate the scanning process with an example below:

```java
double sum = 0;    
try (Scanner scan = new Scanner("20.40 notadouble 30.45 gawef 49.15")) {
   while (scan.hasNext()) {
       if (s.hasNextDouble()) {
           sum += scan.nextDouble();
       } else {
           scan.next();
       }   
   }
 }
 System.out.println(sum);
```


Here we are trying to read a String, and sum up the doubles in that String while skipping the garbage text.

- The first line just gives us a double for the sum.
- The second line declares the Scanner in a try with resources, ensuring it gets closed. If we didn't do this, we would want to close it in a finally with the close function.
What the constructor is doing conceptually is breaking the input String into a list of tokens, `{20.40, notadouble, 30.45, gawef, 49.15}`. We can then scan through these token using the `hasNext<type>()` and `next<type>()` functions.
- The third line instructs scan to continue as long as there is still a token left. This works because `hasNext()` will return true if there is a String token remaining, and all tokens could be read as a String. 
- The fourth line checks if the next token is a double. This would be true for 20.40,30.45, and 49.15, and in these cases line 5 take the token from the list  with `scan.nextDouble()` and add this value to the sum.

If the next token was not in fact a double, we call `scan.next()` to grab the next token as a String. Since the text is just garbage, we don't store it, but by calling next we remove the token from the list.

This code will scan in the three doubles and discard the two Strings, and will then print the sum (100) on line 11.

## Scanner vs Reader

Scanner has pretty all of the functionality of `BufferedReader`, including a `nextLine()` function that allows you to break up a file line by line and skip the remaining tokens on a given line.

That said, it is slower and more expensive than `BufferedReader`, which is the preferred option if you just want text. Further, the `nextLine()` functionality can make the scanning process messy, as it can potentially skip a lot of tokens, and was not really designed for the use case we discussed last week.

A common use case is thus to use a `BufferedReader` to read a file in as `String`s, and then use a Scanner to break these Strings into tokens. This pattern is in fact
used in `IOLabPartTwo.java`.


{% next %}

### Our Data Structure

Repeated from last week, you'll need to use this class again to complete the lab. 

We will use a class we have written, `OurData` to store this data. 
OurData is a simple class that emulates the workings of a database. To initialize an OurData object, you use the following line:

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



{% next %}

## Parsing a CSV File

We are now going to parse a comma-separated value (CSV) file. For more on CSV's, you can read [here](https://en.wikipedia.org/wiki/Comma-separated_values), but for the purposes of this lab we will focus on the included `programs.csv`. You'll note that the data is the same as `programs.txt`, just in a different format.
The field names are headers on the first row. Each subsequent row then contains data for a single entry, where each column in that row corresponds to the field. 
The function `IOLabPartTwo.parseCSVData` extracts the headers then passes each row into a Scanner with the "," delimiter. The scanner and headers are then passed into the function `IOLabPartTwo.parseCSVLine`. 


### Your Task

Modify `IOLabPartTwo.parseCSVLine` so that it builds and returns an OurData object from the scanner, looping through the line and grabbing each token then storing in the correct format using `OurData's setField function`.

Note that the tokens can be of type `int` (`hasNextInt()`/`nextInt()`), `boolean` (`hasNextBoolean()`/`nextBoolean()`) or `String`. Further note that the field name in headers corresponds with the order the tokens are encountered i.e. the first element scanned has the fieldName of the first value in headers.

To test your code, uncomment out the first section in the constructor. If it prints out data in the same format as `programs.txt` your program is (probably) working.


{% next %}


## Writing a CSV File

To wrap up we are going to write a CSV file. 

Modify `IOLabPartTwo.printCSVFile()` such that it builds a file where the first line of the file contains the headers array, in order, separated by commas, and the subsequent lines write out `OurData` objects such that the field in the ourData object corresponds to the same column as it's header i.e. look at `programs.csv`, it should look like that. Recall that the `OurData` class has a function `getFieldAsString(fieldName)` which should be useful for this part.

We will use a `BufferedWriter`, which you can read about [here](https://docs.oracle.com/javase/7/docs/api/java/io/BufferedWriter.html). This is already instantiated for you in a try-with-resources call. Note that this automatically closes the stream, which you would otherwise need to do in a finally block after all your writing operations. Note generally you do not want to close a stream until you are sure you are done writing to file.

Use the `BufferedWriter.write(String s)` function in whatever way you see fit to get the file in the correct format.

### Hints

1. One approach would be to build the file as one big String and then pass this in with a single write call.
Alternatively, you could do a write call for each line.

2. Note that each write call adds to a buffer that is not immediately written to file. You could force this buffer to be written to file by calling the `BufferedWriter.flush()`. 
The buffer is automatically flushed when the file is closed. Since the `BufferedWriter` is in a try-with-resources, you don't need to worry about this for the lab, but it important to understand and there is more on this topic in the IO tutorial linked to at the start of the lab.

To test your code, uncomment out the second section in the constructor. It should create a csv file, and if this matches up with the content in `programs.csv` then your code is (probably) working.

