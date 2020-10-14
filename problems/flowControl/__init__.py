import check50
import check50_java

@check50.check()
def ly_exists():
    """LeapYear.java exists."""
    check50.exists("LeapYear.java")

@check50.check(exists)
def ly_compiles():
    """LeapYear.java compiles."""
    check50_java.compile("LeapYear.java")

@check50.check(ly_compiles)
def test1980():
    """Ensures LeapYear is returning the specified value for 1980"""
    check50_java.run("LeapYear").stdin(1980).stdout("true\n").exit()

@check50.check(ly_compiles)
def test2000():
    """Ensures LeapYear is returning the specified value for 2000"""
    check50_java.run("LeapYear").stdin(2000).stdout("true\n").exit()


@check50.check(ly_compiles)
def test2016():
    """Ensures LeapYear is returning the specified value for 2016"""
    check50_java.run("LeapYear").stdin(2016).stdout("true\n").exit()

@check50.check(ly_compiles)
def test1900():
    """Ensures LeapYear is returning the specified value for 1980"""
    check50_java.run("LeapYear").stdin(1900).stdout("false\n").exit()

@check50.check(ly_compiles)
def test2001():
    """Ensures LeapYear is returning the specified value for 2001"""
    check50_java.run("LeapYear").stdin(2001).stdout("false\n").exit()

@check50.check(ly_compiles)
def test2018():
    """Ensures LeapYear is returning the specified value for 2018"""
    check50_java.run("LeapYear").stdin(2018).stdout("false\n").exit()
