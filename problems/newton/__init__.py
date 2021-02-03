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
    """Ensures Newton is returning the specified value for 25 0.1 1"""
    check50_java.run("Newton 25 0.1 1").stdout("8\n5.060078220517644").exit()

@check50.check(newt_compiles)
def root_inf_00001():
    """Ensures Newton is returning the correct (but incorrect) value for 25 0.1 0.1"""
    check50_java.run("Newton 25 0.1 0.1").stdout("9\n5.000356653832537").exit()

@check50.check(newt_compiles)
def too_few_parameters():
    """Ensures Newton is returning the correct error message for 25"""
    check50_java.run("Newton 25").stdout("Incorrect Number of Parameters\nUsage: java Newton number initial_guess (optional)epsilon").exit()


@check50.check(newt_compiles)
def too_many_parameters():
    """Ensures Newton is returning the correct error message for 25 0 3 4"""
    check50_java.run("Newton 25 0 3 4").stdout("Incorrect Number of Parameters\nUsage: java Newton number initial_guess (optional)epsilon\n").exit()

    

