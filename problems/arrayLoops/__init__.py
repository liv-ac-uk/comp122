import check50
import check50_java

check50.include("Comp122.class")  # copy over input helper

@check50.check()
def CShantyExists():
    """CShanty.java exists."""    
    check50.exists("CShanty.java")

@check50.check(CShantyExists)
def CShantyCompiles():
    """CShanty.java compiles."""
    check50_java.compile("CShanty.java")

@check50.check(CShantyCompiles)
def CShantyPrintsTwo():
    """Ensures CShanty can print twice"""
    check50_java.run("CShanty").stdin("2").stdout("Soon may the compiler come,\nTo bring class files and exceptions\nSoon may the compiler come,\nTo bring class files and exceptions\nHigh level languages earn my rum\nBut my first love is the C!\n").exit()

@check50.check(CShantyCompiles)
def CShantyPrintsThree():
    """Ensures CShanty is printing thrice"""
    check50_java.run("CShanty").stdin("3").stdout("Soon may the compiler come,\nTo bring class files and exceptions\nSoon may the compiler come,\nTo bring class files and exceptions\nSoon may the compiler come,\nTo bring class files and exceptions\nHigh level languages earn my rum\nBut my first love is the C!\n").exit()

@check50.check()
def factorialExists():
    """Factorial.java exists."""
    check50.exists("Factorial.java")

@check50.check(factorialExists)
def factorialCompiles():
    """Factorial.java compiles."""
    check50_java.compile("Factorial.java")

@check50.check(factorialCompiles)
def factorialFour():
    """Ensures Factorial is printing 4!"""
    check50_java.run("Factorial").stdin("4").stdout("24\n").exit()


@check50.check(factorialCompiles)
def factorialTen():
    """Ensures Factorial is printing 10!"""
    check50_java.run("Factorial").stdin("10").stdout("3628800\n").exit()

@check50.check(factorialCompiles)
def factorialThirteen():
    """Ensures Factorial is printing 13!"""
    check50_java.run("Factorial").stdin("13").stdout("6227020800\n").exit()

@check50.check(factorialCompiles)
def factorialNineteen():
    """Ensures Factorial is printing 19!"""
    check50_java.run("Factorial").stdin("19").stdout("121645100408832000\n").exit()





@check50.check()
def largest_exists():
    """Largest.java exists"""
    check50.exists("Largest.java")

@check50.check(largest_exists)
def largest_compiles():
    """Largest.java compiles"""
    check50_java.compile("Largest.java")

@check50.check(largest_compiles)
def test315():
    """Ensures Largest is returning the specified value for [3, 1, 5]"""
    check50_java.run("Largest").stdin("3").stdin("3").stdin("2").stdin("5").stdout("5\n").exit()

@check50.check(largest_compiles)
def test8_400_54_9000():
    """Ensures Largest is returning the specified value for [8, 400, 54, 9000]"""
    check50_java.run("Largest").stdin("4").stdin("8").stdin("400").stdin("54").stdin("9000").stdout("9000\n").exit()


@check50.check(largest_compiles)
def test523_6384_3929_12837_3():
    """Ensures Largest is returning the specified value for [523, 6384, 3929, 12837, 3]"""
    check50_java.run("Largest").stdin("5").stdin("523").stdin("6384").stdin("3929").stdin("12837").stdin("3").stdout("12837\n").exit()
