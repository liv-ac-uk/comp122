import check50
import check50_java
import check50_junit


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


@check50.check()
def student_exists():
    """Student.java exists"""
    check50.exists("Student.java")

@check50.check(student_exists)
def student_compiles():
    """Student.java compiles"""
    check50_java.compile("Student.java")

@check50.check(student_compiles)
def student_submitAll():
    """Create object and return submittedAll with no parameters"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testSubmittedAll'])

@check50.check(student_compiles)
def student_updateGrade_30():
    """Create object and return submittedAll with no parameters"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testSubmittedAll'])


@check50.check(student_compiles)
def student_updateGrade_30_20_submitAll():
    """Create object and return submittedAll with no parameters"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testSubmittedAll'])
