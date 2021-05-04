import check50
import check50_java
import check50_junit


@check50.check()
def book_exists():
    """Book.java exists."""
    check50.exists("Book.java")


@check50.check(book_exists)
def book_compiles():
    """Book.java compiles."""
    check50_java.compile("Book.java")


@check50.check(book_compiles)
def book_testConstructorSignature():
    """Book constructor signature as prescribed"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'BookTest#testConstructorSignature'])


@check50.check(book_testConstructorSignature)
def book_testConstructor():
    """Book constructor works without blowing up"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'BookTest#testConstructor'])


@check50.check(book_compiles)
def book_testTitleField():
    """Book.title is declared as private attribute"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'BookTest#testTitleField'])


@check50.check(book_compiles)
def book_testGetTitleSignature():
    """Book.getTitle signature"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'BookTest#testGetTitleSignature'])


@check50.check(book_testGetTitleSignature)
def book_testGetTitle():
    """Book.getTitle just returns title"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'BookTest#testGetTitle'])


@check50.check(book_compiles)
def book_testGetPagesSignature():
    """Book.getPages signature"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'BookTest#testGetPagesSignature'])


@check50.check(book_testGetPagesSignature)
def book_testGetPages():
    """Book.getPages counts as expected (1600 chars --> 2 pages)"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'BookTest#testGetPages'])


@check50.check()
def press_exists():
    """Press.java exists."""
    check50.exists("Press.java")


@check50.check(press_exists)
def press_compiles():
    """Press.java compiles."""
    check50_java.compile("Press.java")
    check50.include("testDir/")
    check50.include("badDir/")


@check50.check(press_compiles)
def press_testEditionField():
    """Press.edition declared as prescribed"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'PressTest#testEditionField'])


@check50.check(press_compiles)
def press_testShelfField():
    """Press.shelf declared as private attribute"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'PressTest#testShelfField'])


@check50.check(press_compiles)
def press_testConstructorShelf():
    """Press constructor sets up shelf if used as new Press("testDir", 3)"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'PressTest#testConstructorShelf'])


@check50.check(press_compiles)
def press_testPrintSignature():
    """Press.print signature as prescribed"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'PressTest#testPrintSignature'])

@check50.check(press_testPrintSignature)
def press_testPrint():
    """Press.print behaves as expected when instantiated as new Press("testDir", 3)"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'PressTest#testPrint'])


@check50.check(press_compiles)
def press_testRequestSignature():
    """Press.request signature as prescribed"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'PressTest#testRequestSignature'])

@check50.check(press_testRequestSignature)
def press_testRequestSingleEdition():
    """Press.request works as expected if instantiated as new Press("testDir", 3)"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'PressTest#testRequestSingleEdition'])


@check50.check()
def vm_exists():
    """VendingMachine.java exists."""
    check50.exists("VendingMachine.java")


@check50.check(vm_exists)
def vm_compiles():
    """VendingMachine.java compiles."""
    check50_java.compile("VendingMachine.java")
    check50.include("testDir/")


@check50.check(vm_compiles)
def vm_testLocationFactorField():
    """VendingMachine.locationFactor defined as private attribute"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'VendingMachineTest#testLocationFactorField'])


@check50.check(vm_compiles)
def vm_testSupplierField():
    """VendingMachine.supplier defined as private attribute"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'VendingMachineTest#testSupplierField'])


@check50.check(vm_compiles)
def vm_testConstructorSignature():
    """VendingMachine constructor signature"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'VendingMachineTest#testConstructorSignature'])


@check50.check(vm_compiles)
def vm_testConstructor():
    """VendingMachine constructor works without blowing up"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'VendingMachineTest#testConstructor'])


@check50.check(vm_compiles)
def vm_testInsertCoinSignature():
    """VendingMachine.insertCoin signature"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'VendingMachineTest#testInsertCoinSignature'])


@check50.check(vm_testInsertCoinSignature)
def vm_testInsertCoinValidDenomination():
    """use VendingMachine.insertCoin with valid denomination (0.05)"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'VendingMachineTest#testInsertCoinValidDenomination'])


@check50.check(vm_testInsertCoinSignature)
def vm_testInsertCoinInvalidDenomination():
    """use VendingMachine.insertCoin with invalid denomination (0.04)"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'VendingMachineTest#testInsertCoinInvalidDenomination'])


@check50.check(vm_compiles)
def vm_testGetCassetteSignature():
    """VendingMachine.getCassette signature"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'VendingMachineTest#testGetCassetteSignature'])


@check50.check(vm_testGetCassetteSignature)
def vm_testGetCassette():
    """VendingMachine.getCassette works as expected if instantiated as new Press("testDir", 3)"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'VendingMachineTest#testGetCassette'])


@check50.check(vm_compiles)
def vm_testBuyBookSignature():
    """VendingMachine.buyBook signature"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'VendingMachineTest#testBuyBookSignature'])


@check50.check(vm_testBuyBookSignature)
def vm_testBuyBookSingle():
    """buy a single book as intended"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'VendingMachineTest#testBuyBookSingle'])
