import check50
import check50_java
import check50_junit

@check50.check()
def student_exists():
    """Student.java exists"""
    check50.exists("Student.java")

@check50.check(student_exists)
def student_compiles():
    """Student.java compiles"""
    check50_java.compile("Student.java")

@check50.check(student_compiles)
def student_construction():
    """Create student object successfully"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testBlankConstructor'])

@check50.check(student_compiles)
def student_setName():
    """ Ensure that the student setName() method is working properly """
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testSetName'])


@check50.check(student_compiles)
def student_getName():
    """Ensure that the student getName() method is working properly"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testGetName'])

        
@check50.check(student_compiles)
def student_getName():
    """Ensure that the student setGrade() method is working properly"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testSetGrade'])

        
@check50.check(student_compiles)
def student_getName():
    """Ensure that the student getGrade() method is working properly"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testGetGrade'])



@check50.check()
def vgather_exists():
    """VGather.java exists"""
    check50.exists("VGather.java")

@check50.check(vgather_exists)
def vgather_compiles():
    """VGather.java compiles"""
    check50_java.compile("VGather.java")

@check50.check(vgather_compiles)
def vgather_single():
    """ vgather runs with a single student"""
    check50_java.run("VGather").stdin("1", prompt=False).stdin("5", prompt=False).stdout("5\n").exit()



@check50.check(vgather_compiles)
def vgather_two():
    """ vgather runs with two students"""
    check50_java.run("VGather").stdin("2", prompt=False).stdin("5", prompt=False).stdin("15", prompt=False).stdout("10\n").exit()

    
@check50.check(vgather_compiles)
def vgather_five():
    """ vgather runs with five students"""
    check50_java.run("VGather").stdin("5", prompt=False).stdin("5", prompt=False).stdin("15", prompt=False).stdin("25", prompt=False).stdin("35", prompt=False).stdin("45", prompt=False).stdout("25\n").exit()