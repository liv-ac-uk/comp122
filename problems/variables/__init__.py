import check50
import check50_java

@check50.check()
def declarations_exists():
    """Declarations.java exists."""
    check50.exists("Declarations.java")

@check50.check(declarations_exists)
def declarations_compiles():
    """Declarations.java compiles."""
    check50_java.compile("Declarations.java")

@check50.check(declarations_compiles)
def declarations_returnsFloat():
    """Ensures declarations is returning the specified value"""
    check50_java.run("Declarations").stdout("-62.5").exit()

@check50.check()
def fp_compiles():
    """FPTestApp.java compiles."""
    check50_java.compile("FPTestApp.java")

@check50.check(fp_compiles)
def fp_working():
    """Ensures FPTestApp is printing the specified value"""
    check50_java.run("FPTestApp").stdout("1.0000000000000002").exit()

@check50.check()
def circle_compiles():
    """SimpleCircle.java compiles."""
    check50_java.compile("SimpleCircle.java")

@check50.check(circle_compiles)
def circle_working():
    """Ensures SimpleCircle is printing the specified value"""
    check50_java.run("SimpleCircle").stdout("2.5\n19.634954084936208\n15.707963267948966").exit()

@check50.check()
def pythag_compiles():
    """Pythagoras.java compiles."""
    check50_java.compile("Pythagoras.java")

@check50.check(pythag_compiles)
def pythag_working():
    """Ensures Pythagoras is printing the specified value"""
    check50_java.run("Pythagoras").stdout("5.830951894845301").exit()

@check50.check()
def cosines_compiles():
    """Cosines.java compiles."""
    check50_java.compile("Cosines.java")

@check50.check(cosines_compiles)
def cosines_working():
    """Ensures Cosines is printing the specified value"""
    check50_java.run("Cosines").stdout("6.999999999999999").exit()
