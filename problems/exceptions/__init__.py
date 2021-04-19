import check50
import check50_java

check50.include("Exceptron.class")  # copy over Exceptron

@check50.check()
def select_from_exists():
    """SelectFrom.java exists."""
    check50.exists("SelectFrom.java")

@check50.check(select_from_exists)
def select_from_compiles():
    """SelectFrom.java compiles."""
    check50_java.compile("SelectFrom.java")

@check50.check(select_from_compiles)
def select_from_working():
    """Ensures SelectFrom has been fixed """
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ExceptionLabTest#selectFromTest'])

@check50.check()
def exceptron_platform_exists():
    """ExceptronPlatform.java exists."""
    check50.exists("ExceptronPlatform.java")

@check50.check(exceptron_platform_exists)
def exceptron_platform_compiles():
    """ExceptronPlatform.java compiles."""
    check50_java.compile("ExceptronPlatform.java")

@check50.check(exceptron_platform_compiles)
def first_exception():
    """Tests initial wrapping of Exception handler """
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ExceptionLabTest#firstExceptionTest'])

@check50.check(exceptron_platform_compiles)
def everythings_fine_working():
    """Tests default message works """
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ExceptionLabTest#everythingsFineTest'])

@check50.check(exceptron_platform_compiles)
def checked_exceptions_working():
    """Checked Exception handling works """
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ExceptionLabTest#checkedExceptionsTest'])

@check50.check(exceptron_platform_compiles)
def runtime_exceptions_working():
    """Runtime Exception handling works """
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ExceptionLabTest#runTimeExceptionsTest'])

@check50.check(exceptron_platform_compiles)
def loop_logic_working():
    """Handling loop and IOExceptions appropriately """
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ExceptionLabTest#loopTest'])

@check50.check(exceptron_platform_compiles)
def finally_logic_working():
    """Ensuring they turned off Exceptron with finally """
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ExceptionLabTest#finallyTest'])
