import check50
import check50_java

@check50.check()
def exists():
    """Declarations.java exists."""
    check50.exists("Declarations.java")

@check50.check(exists)
def compiles():
    """Declarations.java compiles."""
    check50_java.compile("Declarations.java")

@check50.check(compiles)
def veronica():
    """responds to name Veronica."""
    check50_java.run("Declarations").stdin("0 250").stdout("-250").exit()

@check50.check(compiles)
def brian():
    """responds to name Brian."""
    check50_java.run("Hello").stdin("250 0").stdout("250").exit()
