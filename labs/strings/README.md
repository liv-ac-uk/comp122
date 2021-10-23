## Strings
In Java, `String` is not a primitive data type.
Instead, similar to Arrays, Strings are *compound* types: A string consists of several other things (characters).
But it is more than a sequence of characters! Each individual string offers some useful methods that operate *on it*
For example, calling the `length()` method on a string will return the number of characters it contains.
So `"Hello".length()` actually equals `5`.
There are several different ways to create a string value.
The following lines of code will create three functionally equivalent `String`s. There is no particular preference as to which method to use.

~~~java
String s1 = "Hello";
String s2 = new String("Hello");

char[] charseq = {'H','e','l','l','o'};
String s3 = new String(charseq);
~~~

In OOP-speak, the above are different *constructors* allowing to *instantiate* the String *class* into an individual String *object*. But we'll look into that in much more detail from next week onwards.

Most of the built-in methods on strings are concerned with querying the content of the `String`, such as finding its length, searching for a substring or a character, or performing comparisons between different strings. Some methods will actually create a new `String` object.
Some methods defined on `String`s include the following:

* `length()`    Returns the number of characters in the String.
* `contains(s)` Does original String contain char (or String) `s`?
* `indexOf(c)`  Returns the index (as `int`) within the original String of the first occurrence of `c`. Returns -1 if the parameter String does not appear in the original String.
* `substring(n,m)` Returns another String that is a copy of the subword between index `n` and `m`.

Java interprets the symbol (+) as (inline) string concatenation when *at least one* of the arguments is a `String`.
This is why you can concatenate a string and a number, say, to get a new string. However, Java *does not* understand the multiplication operator in the context of the `String`s.

**FYI,** `String`s are "immutable", meaning that they cannot be changed once they are created.
One effect of this is is that the string methods `toUpperCase()` will
return a *new* `String` object, leaving the original one unchanged:

~~~java
String s4 = s1.toUpperCase();
System.out.println(s4);  //*  Prints HELLO
System.out.println(s1);  //*  Prints Hello
~~~

### Your Turn!

Try out these `String` methods by writing a program to play around with them.
You can use the code above (or similar code) to try these methods out.
Make sure that you understand what these methods are supposed to be doing.

Check out the [official documentation here](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html)
for what else the `String` class can do for you.

{% next %}

Let's write a small application to analyse and manipulate strings.
There will be three parts to this exercise.
Your solution to each part should live in its own method of a common class
called `StringApp`, given in the starter code.

## Part 1: Powers!

Write a (`public static`) method called `pow` that will take a `String` and a number n as
parameters and will return a `String`, which consists of
the original one repeated (concatenated) n times. 

**Caution!** The code should `return` the new string and not just print it on the terminal!
So `pow("abc", 3)` equals `"abcabcabc"`
and in the following code the second Boolean variable is set to `true`.
Can you explain why the first is not?

```java
int n = 3;
String basis = "abc";
String nFold = StringApp.pow(basis,n);

boolean b1 = "abcabcabc" ==  nFold;
boolean b2 = "abcabcabc".equals(nFold);
```
## Part 2: Factors?

How can I find *all* (non-overlapping) instances of a substring inside of another string?
For example, given the string "helloworld hellomoon hellosun hello lamp post", and I want to find the indices of all instances of the substring "hello", how can I do that?
Write a method called `factorCount` that takes two strings and returns the number of times the second string occurs in the first.

```java
factorCount("helloworld hellomoon hellosun hello lamp post", "hello") == 4;
```

{% spoiler "Hint" %}

Find the first instance (if it exists, of course), remove it
from the original string, and repeat. By "remove", I really mean
find the substring from the original string *beyond* the end
of the first instance of the target string. For example, the
first index of "hello" in the example string is 0 as it occurs
right at the beginning of the string.
If I remove the first instance of "hello", what I really want to
do is to take the substring that starts at index 5, consisting
of the remainder of the string. Then I can search through that
smaller substring of what remains.

{% endspoiler %}

```java
String s1 = "helloworld hellomoon hellosun hello lamp post";  

String targetString = "hello";
int firstIndex = s1.indexOf(targetString);
if (firstIndex != -1) {
    System.out.println(firstIndex);

    //*  Get the rest of the string to process
    String restOfString = s1.substring(firstIndex + targetString.length(), s1.length());
}
```

This would find the first instance of the string "hello" and I
would end up with a resulting string that I would get by
removing the initial part of the string up to the end of the
first occurrence of the word "hello".

**Notice:**
Strings are indexed starting from 0.
Despite this Array-like indexing, you *cannot* access elements of the `String` using array notation. E.g. `s1[2]` will cause a compilation error! `s1.charAt(2)` is how you access the character at index 2 in the String `s1`.

### Case insensitive factors?
How do I do the above operation if I don't care about the case of the original string or the search string?
In other words, searching for "hello" in the string "Hello world" will result in nothing being found (using the Java `substring(...)` method. What do I do differently if I want to consider "hello" and "Hello" (and "HeLLo", etc) as all the same?

Write an overloaded version of the `factorCount` method that takes another `boolean` to indicate if we are looking for exact matches or allow any capitalisation in factors.

```java
public static int factorCount(String a, String f, boolean caseSensitive){ ... }
```

So that in particular,
```java
String s = "helloworld heLLomoon hellosun HELLO lamp post";
System.out.println(factorCount(s, "hello", true));
System.out.println(factorCount(s, "hello", false));
```
Would print 3 an 5.


### Testing

In order to quickly test these functions out on longer strings you can use the
input helper `Comp122.readFileAsString`, which eats a (relative) path to a text file and returns its contents as a string

```java
String ttlgPar1 = (Comp122.readFileAsString("teststrings/ttlgPar1.txt");
int kittenCount = StringApp.factorCount(ttlgPar1, "kitty");  // tries your code.
```

Find some demo input files `ttlgParX.txt` given in the starter code.  
We expect there to be 3,1,3, and 3 "kitten"s in files ttlgPar1 to ttlgPar4, respectively,
and 11,9,11,and 12 times the factor "it". You can run the automarker on Codegrade as well for more checks.

{% next %}

## Part 3: Letter counts

Write a program that counts the number of times each letter of the (English) alphabet occurs in the
string given as first command line argument.

To be clear, you should include a `main` method so that the `StringApp` class is executable.
This should read the input test from the first command line argument (not from standard in via the `Comp122` helper)
and print exactly 26 lines, one for each (small) letter of the alphabet, like this.

```console
$> java StringApp "helloworld heLLomoon hellosun HELLO lamp post"
a: 1
b: 0
c: 0
d: 1
e: 4
f: 0
g: 0
h: 4
i: 0
j: 0
k: 0
l: 10
m: 2
n: 2
o: 8
p: 2
q: 0
r: 1
s: 2
t: 1
u: 1
v: 0
w: 1
x: 0
y: 0
z: 0
```

Here is another test run (that uses some shell magic to turn the content of the `ttlgPar2.txt` into a log, quoted string; don't worry about how for now) that you can use for debugging.

```console
$> java StringApp "`<teststrings/ttlgPar2.txt`"
a: 25
b: 5
c: 4
d: 13
e: 29
f: 5
g: 8
h: 25
i: 23
j: 1
k: 2
l: 10
m: 1
n: 22
o: 17
p: 4
q: 1
r: 15
s: 20
t: 31
u: 5
v: 1
w: 17
x: 0
y: 5
z: 0
```


### A word on efficiency
You could re-use your code from part 2 here but would that be the most efficient way to do it?
Yes and no! It is efficient in the sense that you do not spend time on a second implementation. Code re-use is always a good thing.
However, calling your previous `factorCount` method 26 times is inefficient in the sense that this will result in 26 readings of the original string. One can do better! For example, you could iterate over the string once, letter by letter,
and keep a record of how often you have seen each of the 26 letters in an Array of characters `char[]`.
A speedup by factor 26 will earn you brownie points with your boss if you are a software developer.
Theoreticians will be less impressed because both algorithms are O(n).

### Implementation Hint

In Java, `char` and `int` variables are (more or less) interchangeable. A Java statement like

```java
int diff = 'e' - 'b';
```

is perfectly legal, i.e. Java can interpret the "difference of two
letters" with no problem, and this will give an integer value. 

If the two letters are of the same case (both upper or both lower case), then this will give a value
between -25 and 25. In particular, if `ch` is a lower case (`char`) letter, then

```java
int diff = ch - 'a';
```

tells you how many places after 'a' that letter is in the alphabet.
(The value of `diff` will be between 0 and 25 inclusive).
