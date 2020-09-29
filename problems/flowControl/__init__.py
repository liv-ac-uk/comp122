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

@check50.check(compiles)
def test1980():
    """Ensures LeapYear is returning the specified value for 1980"""
    check50_java.run("LeapYear").stdin(1980).stdout("true\n").exit()

@check50.check(compiles)
def test2000():
    """Ensures LeapYear is returning the specified value for 2000"""
    check50_java.run("LeapYear").stdin(2000).stdout("true\n").exit()


@check50.check(compiles)
def test2016():
    """Ensures LeapYear is returning the specified value for 2016"""
    check50_java.run("LeapYear").stdin(2016).stdout("true\n").exit()

@check50.check(compiles)
def test1900():
    """Ensures LeapYear is returning the specified value for 1980"""
    check50_java.run("LeapYear").stdin(1900).stdout("false\n").exit()

@check50.check(compiles)
def test2001():
    """Ensures LeapYear is returning the specified value for 2001"""
    check50_java.run("LeapYear").stdin(2001).stdout("false\n").exit()

@check50.check(compiles)
def test2018():
    """Ensures LeapYear is returning the specified value for 2018"""
    check50_java.run("LeapYear").stdin(2018).stdout("false\n").exit()

@check50.check()
def newt_exists():
    """Newton.java exists."""
    check50.exists("Newton.java")

@check50.check(exists)
def newt_compiles():
    """Newton.java compiles."""
    check50_java.compile("Newton.java")

@check50.check(compiles)
def root_2():
    """Ensures LeapYear is returning the specified value for 2.0 1.0"""
    check50_java.run("Newton").stdin("2.0 1.0").stdout("6\n1.414213562373095").exit()

@check50.check(compiles)
def root_9():
    """Ensures Newton is returning the specified value for 9.0 3.0"""
    check50_java.run("Newton").stdin("9.0 3.0").stdout("1\n3.0").exit()

@check50.check(compiles)
def root_25():
    """Ensures Newton is returning the specified value for 25 0.1"""
    check50_java.run("Newton").stdin("25 0.1").stdout("11\n5.0").exit()

@check50.check(compiles)
def root_inf():
    """Ensures Newton is returning the correct (but incorrect) value for 25 0"""
    check50_java.run("Newton").stdin("25 0").stdout("3\nInfinity").exit()
