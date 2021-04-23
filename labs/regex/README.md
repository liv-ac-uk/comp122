# Regular Expressions

A reasonably large proportion of practical computer programs work with text files in some capacity. A lot of data comes as raw text, and we must analyse this, process this, and store it consistently. 

This has been the case for much of the history of software and an early success was the development of regular expressions to do this consistently. 

These are patterns which we define, which match particular substrings of a given string. 

{% next %}

## Regex in Java

As these are such common operations, there are some included classes with the Java standard library to perform this. These are the `Pattern` and `Matcher` classes in `java.util.regex`. 

The standard usage is to define a regular expression that we wish to match, and compile this `Pattern`. We then take the string that we wish to match and compare our regular expression against this with `Matcher`.

For starters, let's search for some simple words in the first few lines of an old American folktale:

"It is a period of civil war. Rebel spaceships, striking from a hidden base, have won their first victory against the evil Galactic Empire. During the battle, Rebel spies managed to steal secret plans to the Empire's ultimate weapon, the DEATH STAR, an armored space station with enough power to destroy an entire planet. Pursued by the Empire's sinister agents, Princess Leia races home aboard her starship, custodian of the stolen plans that can save her people and restore freedom to the galaxy..."

{% next %}

## Simple Match

To do this we must first define a matching pattern for the regular expression. As we are trying to match the word "Rebel", in our input we wish to match the characters "R", "e", "b", "e", "l", in sequence. 

This is a common operation and so it is made easy in Regex, to match this the corresponding string is `"Rebel"`. 

```java
Pattern pattern = Pattern.compile("Rebel");
Matcher matcher = pattern.matcher(input);
```

{% next %}

## Find the Rebels

Now that we have a matched `Matcher` object, we can query this to find the results of our matching. There are three core methods that we will use. `start()`, `end()`, and `find()`. 

`matcher.start()` returns the integer of the 0th position of the first occurrence of the matching regex within the input array. Unsurprisingly `matcher.end()` tells us the integer position that the regex stops matching. If we call `matcher.find()` this will return `True` if the input string has another occurrence of the regex, and will move onto this part of the string. If no more matches remain, it will return `False`. 

This means the easiest way to work with this is in a `while` loop, as this method will exit the loop once it has reached the end of the `String`:

```java
while(matcher.find()) {
    System.out.println(matcher.start());
    System.out.println(matcher.end());
    System.out.println(input.substring(matcher.start(), matcher.end()));
}
```

If we run this, we see that it prints the start and end integers of each match in the input string, and we can use the `substring(start, end)` method to display each of our matches.

```
$ java Rebel
29
34
Rebel
158
163
Rebel
```

{% next %}

## Both Sides Make Very String Arguments

Regular expressions are flexible, and there are lots of special characters which enable us to match a range of things very concisely. 

If we were an undecided voter in the galaxy, and we wanted to match with either the rebels or the empire, we could use the regex OR character "|" to match with:

```java
Pattern pattern = Pattern.compile("Rebel|Empire");
```

If we were to recompile our program and run it we would see that it has matched on both of these words in the input

```
$ java Rebel
29
34
Rebel
131
137
Empire
158
163
Rebel
207
213
Empire
337
343
Empire
```

{% next %}

## Repeated Chars

Many times we do not know the specific characters we are looking for, and we may not know how many times a character should repeat. The art of regex comes in identifying which of the special characters can be combined to match what you are looking for. 

Let's say we wanted to search for any word that is fully capitalized with a regular expression, to do this we can combine a few of these standard tricks. 

First, we can define a character set with `[]`, which means match any of the characters within the square brackets. For example if we were building a spell checker and we did not mind if people used British or American spelling of words, in our lookup dictionary for the word "organize" we might have the regular expression `"organi[sz]e".

Secondly we can define a range of characters or numbers in regex using `-`, e.g. `[F-L]` would match any character between capital F and capital L, and `[0-9]` would match any single character. Therefore to match any capital letter we can use `[A-Z]`.

Unfortunately this will only match a single capital letter, and we are looking for complete words of capital letters...

## Quantifiers

We can define how many times to repeat a matching set (or character) in a regex with a number in braces (a quantifier). For example the regex `[A-Z]{5}` would match with all the sequences of five letters which are fully capitalized. We can also use the range rules from earlier, and `[A-Z]{5-7}` would match all 5, 6, and 7 letter capitalized words.

We often don't known how many times we need to repeat a matching character, and therefore regex has some looser quantifiers 

`+` - One or more, match the previous character at least once, but possibly many times.
`*` - Zero or more, if the previous character exists, then match it as many times as it repeats. 

As you are beginning to see, regex is practically a dense programming language in its own right. Therefore we often use (online regular expression helpers)[https://regexr.com/] to help us when we work things out, but do remember that Java regex is ever so slightly different to "standard" regex.

{% next %}

## All Groups Have a Wildcard

To save space in the regex, we can use wildcards instead of matching sets. These are simple escape characters (similar to the `\n` escape character that you are used to using) which match specific sets. 

For example, the character `\d` matches a single digit from 0-9, and `\w` will match any ASCII character, including letters, numbers, and standard punctuation. Additionally, the `\s` character will match a single whitespace character, such as space, tab, or newline.

If you want to be more general and match any character (except for newline) then we use a full-stop character `.` so `.*` would match any number of character until the end of the line. If we wanted to specifically match for a full stop, then we can escape this wild behaviour with a backslash. `\.*` would match any number of full-stops in a row.

{% next %}

## I am what I Spam

We will use regular expressions to parse datasets, such as a subset of emails from the (CLAIR dataset of spam emails)[https://www.kaggle.com/rtatman/fraudulent-email-corpus]. If you open this file, you will see that it follows a standard set of lines for the metadata for each email, followed by the message body of the email. 

With the power of regex, let's try and get all the email addresses that are associated with each of these spammers. 

{% next %}

## Arthur and the Knights of Spamalot 

We know that each of the headers contains the line "From:......" which has the spammers given name followed by their email address. This means that we can match on the "From:" and then use wildcards to get the rest of the line.

```java
Pattern pattern = Pattern.compile("From:.*");
```

Given that we have covered IO in the previous lab, we will use a `Scanner` class to read in this text file as a single string. You can run this basic regex with Spam.java. 

- Modify SpamFrom.java so that instead of printing Match Number, Index Start, and Index End it will just print each of the substrings which match the regex

{% spoiler "Hint" %}
Use the `substring()` method to print the string to the terminal
{% endspoiler %}

{% next %}

## Did you get the Email?

If your program is running correctly you should see the following when you run your program.

```
...
From: "DR. GODWIN KALALA" <gokalala1@tiscali.co.uk>
From: EKONG BASSEY <ekong.bassey2@caramail.com>
From: HELLEN SHAKA ZUMA <hellenshaka@netscape.net>
From: Akande fredrick <fredsam@123.com>
From: esama kingdom <esamakingdom@fsmail.net>
$
```

This is pulling our desired information out, but we really just want the email. 

To do this in regex we can look for the `@` symbol, as we know that all emails must contain an `@`. We could search for all words which contain any number of characters (apart from space) followed by an `@`, followed by any number of characters.

We can use the escape character `\w` to match any character, but in Java `String`s the `\` character indicates an escape sequence, so this won't actually get passed to the regex compiler. To pass escape characters to `Pattern.compile` properly we need to use a double slash `\\w`.

```java
Pattern pattern = Pattern.compile("\\w*@\\w*");
```

Compile this program and see the output.

{% next %}

## Better Spam

We can see that this isn't really getting us the emails correctly. The `\w` regex character only matches alpha characters, and the second half of email addresses normally contain one (or more) `.`'s.

We can change this second `\\w` to a `.` 

```java
Pattern pattern = Pattern.compile("\\w*@.*");
```

If we recompile this and run, what do we see?

There are still two big issues with how our regex is matching emails. First of all, we can have a `.` in the part of the email before the `@`, but here `\\w` will only match `a-z`. Secondly we can see that our emails end with a `>`, this is because `.` will match with this before reaching the space. 

- Modify the regex in `SpamEmail.java` so that it correctly prints every single email addresses in `spam.txt` to the terminal completely, ensuring there are no leading and trailing `<>`s.

{% next %}

## Grouping By 

Unfortunately, this is simply giving us all of the email addresses in the document, and isn't actually telling us which of these are from the spammers. 

What we really want to do is match on the "From:" part of the line, and then ignore everything else in the line until we get to the email address. We then want to take this email address and print it to the terminal. 

We can do this with regular expression capturing groups. A group in a regular expression is defined by `()`. This enables us to focus on a particular region of interest.

In `SpamSender.java` you can see that we have defined a regular expression to match on "From:(.*)". This will match all characters similar to before, however it will save all of the characters after "From:" in a specific group. We can access these using the `matcher.group()` method.

- Modify the regular expression in `SpamSender.java` so that it will return only the email addresses of each of senders of each email.

<!-- 
## It's a Match!

Let us say we have a text file, for example a copy of (Websters English Dictionary)[https://www.gutenberg.org/cache/epub/29765/pg29765.txt] (here just the letter C), given in `Dictionary.txt`.

Here's a simple example of how we could search to see if our dictionary contains the word "CLASS". 

```java
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class GREP {
    public static void main(String[] args) {
        Pattern pattern = Pattern.compile("CLASS");
        Matcher matcher = pattern.matcher(args[0]);
        boolean matchFound = matcher.find();

        if(matchFound) {
            System.out.println("Match found");
        } else {
            System.out.println("Match not found");
        }
    }
}
```

We can run this with:

```
$ java Dict
Match found
```

{% next %}

## Well Defined 

Our lookup program is now fully functional, and all we need to do is change the lookup word in the first line of `main` and we can change what to search for. However it would be even easier if our program just printed the definition instead of us having to look it up. 

If we look at the format of the Dictionary, we can see that each of the defined words are upper case, with the definitions given after. This means that if we wanted to match this, we would be searching from the start of the line for our word ("CLASS"), followed by all words and punctuation until we reach another word which is upper case. 

We build regular expressions up piece by piece, so this could be built up as so:

`(` - Capture the expression within these parentheses. 
`CLASS` - Match the word CLASS 
`[` - Start a new group of things to match
`.` - Match any character, number, or standard piece of punctuation.
`|` - Or 
`\n` - Match a new line
`]` - Finish this group
`*` - Repeat the previous matching group as many times as possible
`)` - Return this full sequence of characters as a single group
`[A-Z]` - Finish matching when we come across any of the capital letters A-Z
`{2}` - Make sure that we only end when there are two capital letters in a row, as we have capital letters in our definitions.

In code, we combine this into a single string, and we would enter this in Java as:

```java
Pattern pattern = Pattern.compile("(CLASS[.|\n]*)[A-Z]{2}"); -->
```

