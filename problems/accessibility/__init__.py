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
def student_has_submitted_is_private():
    """Student has a private attribute called \"hasSubmitted\""""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testHasSubmittedIsPrivate'])

@check50.check(student_compiles)
def student_has_grade_is_private():
    """Student has a private attribute called \"allGrades\""""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testGradeIsPrivate'])

@check50.check(student_compiles)
def student_has_update_grade_is_public():
    """Student has a public method called \"updateGrade\""""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testUpdateGradeIsPublic'])

@check50.check(student_compiles)
def student_has_submitted_is_public():
    """Student has a public method called \"getHasSubmitted\""""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testGetHasSubmittedIsPublic'])

@check50.check(student_compiles)
def student_test_grades_is_public():
    """Student has a public method called \"getGrades\""""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testGetGradesIsPublic'])

@check50.check(student_compiles)
def student_test_total_grade_is_public():
    """Student has a public method called \"getTotalGrade\""""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testGetTotalGradeIsPublic'])


@check50.check(student_compiles)
def student_constructor():
    """Student constructor with no parameter"""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testConstructor'])


@check50.check(student_constructor)
def student_getBaseGrades():
    """base grades getter"""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testGetBaseGrades'])

@check50.check(student_constructor)
def student_getBaseSubmitted():
    """base submitted getter"""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testGetBaseSubmitted'])

@check50.check(student_constructor)
def student_total_grade_single_assignment():
    """getTotalGrade() with a single assignment"""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testUpdateFirstGrade'])

@check50.check(student_constructor)
def student_total_grade_multiple_assignment():
    """getTotalGrade() with a multiple assignment"""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testGetTotalGrades'])

@check50.check(student_constructor)
def student_bool_multiple_assignment():
    """getGrades() with a multiple assignment"""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testGetAllGrades'])

@check50.check(student_constructor)
def student_all_grade_single_assignment():
    """getHasSubmitted() with a single assignment"""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testAssignment0Updates'])

@check50.check(student_constructor)
def student_all_grade_multiple_assignment():
    """getHasSubmitted() with a multiple assignment"""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testAllAssignmentUpdates'])

@check50.check(student_constructor)
def student_not_update_lower():
    """getGrades() with assignment number out of bounds below"""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testOutOfBoundsLower'])

@check50.check(student_constructor)
def student_not_update_lower():
    """getGrades() with assignment number out of bounds above"""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testOutOfBoundsUpper'])


@check50.check(student_constructor)
def student_not_update_lower():
    """getGrades() with assignment grade out of bounds below"""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testNegativeGrade'])

@check50.check(student_constructor)
def student_not_update_lower():
    """getGrades() with assignment grade out of bounds above"""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testTooLargeGrade'])


