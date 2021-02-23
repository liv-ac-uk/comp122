import check50
import check50_java

@check50.check()
def newt_exists():
    """Newton.java exists."""
    check50.exists("Newton.java")

@check50.check(newt_exists)
def newt_compiles():
    """Newton.java compiles."""
    check50_java.compile("Newton.java")

@check50.check(newt_compiles)
def root_2():
    """Ensures LeapYear is returning the specified value for 2.0 1.0"""
    check50_java.run("Newton 2.0 1.0").stdout("6\n1.414213562373095").exit()

@check50.check(newt_compiles)
def root_9():
    """Ensures Newton is returning the specified value for 9.0 3.0"""
    check50_java.run("Newton 9.0 3.0").stdout("1\n3.0").exit()

@check50.check(newt_compiles)
def root_25():
    """Ensures Newton is returning the specified value for 25 0.1"""
    check50_java.run("Newton 25 0.1").stdout("11\n5.0").exit()

@check50.check(newt_compiles)
def root_inf():
    """Ensures Newton is returning the correct (but incorrect) value for 25 0"""
    check50_java.run("Newton 25 0").stdout("3\nInfinity").exit()


@check50.check(newt_compiles)
def root_9_001():
    """Ensures Newton is returning the specified value for 9.0 3.0 0.01"""
    check50_java.run("Newton 9.0 3.0 0.01").stdout("1\n3.0").exit()

@check50.check(newt_compiles)
def root_25_0001():
    """Ensures Newton is returning the specified value for 25 0.1 0.0001"""
    check50_java.run("Newton 25 0.1 0.0001").stdout("11\n5.0").exit()

@check50.check(newt_compiles)
def root_inf_00001():
    """Ensures Newton is returning the correct (but incorrect) value for 25 0 0.00001"""
    check50_java.run("Newton 25 0 0.00001").stdout("3\nInfinity").exit()

@check50.check(newt_compiles)
def too_few_parameters():
    """Ensures Newton is returning the correct error message for 25"""
    actual = check50_java.run("Newton 25").stdout()
    expected = "Incorrect Number of Parameters\nUsage: java Newton number guess epsilon\n"
    if expected != actual:
        raise check50.Mismatch(expected, actual)


@check50.check(newt_compiles)
def too_many_parameters():
    """Ensures Newton is returning the correct error message for 25 0 3 4"""
    expected = "Incorrect Number of Parameters\nUsage: java Newton number guess epsilon\n"
    actual = check50_java.run("Newton 25 0 3 4").stdout()
    if expected != actual:
        raise check50.Mismatch(expected, actual)
