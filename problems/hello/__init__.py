import check50
import check50_java

@check50.check()
def exists():
    """Hello.java exists."""
    check50.exists("Hello.java")

@check50.check(exists)
def compiles():
    """Hello.java compiles."""
    check50_java.compile("Hello.java")

@check50.check(compiles)
def veronica():
    """responds to name Veronica."""
    check50_java.run("Hello").stdin("Veronica").stdout("Veronica").exit()

@check50.check(compiles)
def brian():
    """responds to name Brian."""
    check50_java.run("Hello").stdin("Brian").stdout("Brian").exit()
