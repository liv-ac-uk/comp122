import check50
import check50_java
import check50_junit


@check50.check()
def person_exists():
    """Person.java exists"""
    check50.exists("Person.java")


@check50.check(person_exists)
def person_compiles():
    """Person.java compiles"""
    check50_java.compile("Person.java")

@check50.check(person_compiles)
def person_has_greet_is_public():
    """Person has a public attribute called \"greet\""""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'PersonTest#testGreetIsPublic'])

@check50.check(person_compiles)
def person_has_greet_is_public():
    """Person has working getters/setters"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'PersonTest#testNameSet'])

@check50.check(person_compiles)
def person_has_greet_is_public():
    """Person has a working \"greet\""""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'PersonTest#testGreet'])





@check50.check()
def student_exists():
    """Student.java exists"""
    check50.exists("Student.java")


@check50.check(student_exists)
def student_compiles():
    """Student.java compiles"""
    check50_java.compile("Student.java")


@check50.check(student_compiles)
def student_is_person():
    """Student is an instance of \"Person\""""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testInheritedPerson'])

@check50.check(student_compiles)
def student_has_private_grade():
    """Student has a private variable \"grade\""""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testGradeIsPrivate'])


@check50.check(student_compiles)
def student_set_name(student_compiles):
    """Student has name setter works"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testNameSet'])


@check50.check(student_compiles)
def student_greet():
    """Student \"greet\" method works as expected"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testGreet'])


@check50.check(student_compiles)
def student_grade():
    """Student \"grade\" setters work as expected"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testSetGrade'])





@check50.check()
def lecturer_exists():
    """Lecturer.java exists"""
    check50.exists("Lecturer.java")


@check50.check(lecturer_exists)
def lecturer_compiles():
    """Lecturer.java compiles"""
    check50_java.compile("Lecturer.java")



@check50.check(lecturer_compiles)
def lecturer_is_person():
    """Lecturer is an instance of \"Person\""""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'LecturerTest#testInheritedPerson'])

@check50.check(lecturer_compiles)
def lecturer_has_private_timetable():
    """Lecturer has a private variable \"timetable\""""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'LecturerTest#testTimetableIsPrivate'])





@check50.check(lecturer_compiles)
def lecturer_has_public_getTimeTable():
    """Lecturer has a public method \"getTimeTable\""""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'LecturerTest#testGetTimeTableIsPublic'])

@check50.check(lecturer_compiles)
def lecturer_set_name(lecturer_compiles):
    """Lecturer has name setter works"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'LecturerTest#testNameSet'])


@check50.check(lecturer_compiles)
def lecturer_greet():
    """Lecturer \"greet\" method works as expected"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'LecturerTest#testGreet'])





@check50.check()
def professor_exists():
    """Professor.java exists"""
    check50.exists("Professor.java")


@check50.check(professor_exists)
def professor_compiles():
    """Professor.java compiles"""
    check50_java.compile("Professor.java")


@check50.check(professor_compiles)
def professor_is_person():
    """Professor is an instance of \"Person\""""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ProfessorTest#testInheritedPerson'])


@check50.check(professor_compiles)
def professor_is_lecturer():
    """Professor is an instance of \"Lecturer\""""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ProfessorTest#testInheritedLecturer'])


@check50.check(professor_compiles)
def professor_has_private_budget():
    """Professor has a private variable \"budget\""""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ProfessorTest#testBudgetIsPrivate'])



@check50.check(professor_compiles)
def professor_has_public_getBudget():
    """Professor has a public method \"getBudget\""""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ProfessorTest#testGetBudgetIsPublic'])



@check50.check(professor_compiles)
def professor_set_name(professor_compiles):
    """Professor has name setter works"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ProfessorTest#testNameSet'])


@check50.check(professor_compiles)
def professor_greet():
    """Professor \"greet\" method works as expected"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ProfessorTest#testGreet'])


@check50.check(professor_compiles)
def professor_budget_setter():
    """Professor \"budget\" setters work as expected"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ProfessorTest#testSetBudget'])


