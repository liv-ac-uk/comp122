import check50
import check50_java


@check50.check()
def student_exists():
    """Student.java exists"""
    check50.exists("Student.java")

@check50.check(student_exists)
def student_compiles():
    """Student.java compiles"""
    check50_java.compile("Student.java")

@check50.check(student_compiles)
def student_constructor_blank():
    """Student constructor with no parameters"""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testBlankConstructor'])


@check50.check(student_compiles)
def student_constructor_full():
    """Student constructor with all parameters"""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testFullConstructor'])


@check50.check(student_compiles)
def student_constructor_partial_1():
    """Student constructor with some parameters"""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testPartialConstructor1'])


@check50.check(student_compiles)
def student_constructor_partial_2():
    """Student constructor with some parameters in a different format"""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testPartialConstructor2'])


@check50.check(student_compiles)
def student_constructor_partial_3():
    """Student constructor with some parameters in a different format with different details"""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testPartialConstructor3'])

