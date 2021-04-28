import check50
import check50_java

@check50.check()
def book_exists():
    """Book.java exists."""
    check50.exists("Book.java")

@check50.check(book_exists)
def book_compiles():
    """Book.java compiles."""
    check50_java.compile("Book.java")

@check50.check()
def press_exists():
    """Press.java exists."""
    check50.exists("Press.java")

@check50.check(press_exists)
def press_compiles():
    """Press.java compiles."""
    check50_java.compile("Press.java")

@check50.check()
def vm_exists():
    """VendingMachine.java exists."""
    check50.exists("VendingMachine.java")

@check50.check(vm_exists)
def vm_compiles():
    """VendingMachine.java compiles."""
    check50_java.compile("VendingMachine.java")
