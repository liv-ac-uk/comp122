import check50
import check50_java



@check50.check()
def ly_exists():
    """LeapYear.java exists."""
    check50.exists("LeapYear.java")

@check50.check(ly_exists)
def ly_compiles():
    """LeapYear.java compiles."""
    check50.include("Comp122.class")  # copy over input helper
    check50_java.compile("LeapYear.java")

@check50.check(ly_compiles)
def test1900():
    """Ensures LeapYear is returning the specified value for 1900"""
    check50_java.run("LeapYear").stdin("1900").stdout("false\n").exit()

@check50.check(ly_compiles)
def test1980():
    """Ensures LeapYear is returning the specified value for 1980"""
    check50_java.run("LeapYear").stdin("1980").stdout("true\n").exit()

@check50.check(ly_compiles)
def test2000():
    """Ensures LeapYear is returning the specified value for 2000"""
    check50_java.run("LeapYear").stdin("2000").stdout("true\n").exit()

@check50.check(ly_compiles)
def test2016():
    """Ensures LeapYear is returning the specified value for 2016"""
    check50_java.run("LeapYear").stdin("2016").stdout("true\n").exit()

@check50.check(ly_compiles)
def test1900():
    """Ensures LeapYear is returning the specified value for 1980"""
    check50_java.run("LeapYear").stdin("1900").stdout("false\n").exit()

@check50.check(ly_compiles)
def test2001():
    """Ensures LeapYear is returning the specified value for 2001"""
    check50_java.run("LeapYear").stdin("2001").stdout("false\n").exit()

@check50.check(ly_compiles)
def test2016():
    """Ensures LeapYear is returning the specified value for 2016"""
    check50_java.run("LeapYear").stdin("2016").stdout("true\n").exit()

@check50.check(ly_compiles)
def test2018():
    """Ensures LeapYear is returning the specified value for 2018"""
    check50_java.run("LeapYear").stdin("2018").stdout("false\n").exit()

@check50.check(ly_compiles)
def condensed_boolean():
    with open("LeapYear.java") as f:
        fileString = f.read().replace("\n", "")

    if "||" not in fileString and "&&" not in fileString:
        raise check50.Failure("You did not use Boolean operators")

@check50.check(condensed_boolean)
def condensed1900():
    """Ensures LeapYear can run with condensed logic for 1900"""
    check50_java.run("LeapYear").stdin("1900").stdout("false\n").exit()

@check50.check(condensed_boolean)
def condensed1980():
    """Ensures LeapYear can run with condensed logic for 1980"""
    check50_java.run("LeapYear").stdin("1980").stdout("true\n").exit()

@check50.check(condensed_boolean)
def condensed2000():
    """Ensures LeapYear can run with condensed logic for 2000"""
    check50_java.run("LeapYear").stdin("2000").stdout("true\n").exit()

@check50.check(condensed_boolean)
def condensed2001():
    """Ensures LeapYear can run with condensed logic for 2001"""
    check50_java.run("LeapYear").stdin("2001").stdout("false\n").exit()

@check50.check(condensed_boolean)
def condensed2016():
    """Ensures LeapYear can run with condensed logic for 2016"""
    check50_java.run("LeapYear").stdin("2016").stdout("true\n").exit()

@check50.check(condensed_boolean)
def condensed2018():
    """Ensures LeapYear can run with condensed logic for 2018"""
    check50_java.run("LeapYear").stdin("2018").stdout("false\n").exit()
