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
def person_is_abstract():
    """Person is abstract()"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'PersonTest#testPersonAbstract'])

@check50.check(person_compiles)
def person_is_emailable():
    """Person implements emailable"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'PersonTest#testImplementedEmailable'])







@check50.check()
def emailable_exists():
    """Emailable.java exists"""
    check50.exists("Emailable.java")

@check50.check(emailable_exists)
def emailable_has_interface_method():
    with open("Emailable.java") as f:
        fileString = f.read().replace("\n", "")

    methodStr = "public void sendEmail();"

    if methodStr not in fileString:
        raise check50.Mismatch(methodStr, "", help="Your Emailable interface is missing a method")





@check50.check()
def degreeable_exists():
    """Degreeable.java exists"""
    check50.exists("Degreeable.java")

@check50.check(degreeable_exists)
def degreeable_has_interface_method():
    with open("Degreeable.java") as f:
        fileString = f.read().replace("\n", "")

    methodStr = "public void awardDegree();"

    if methodStr not in fileString:
        raise check50.Mismatch(methodStr, "", help="Your Degreeable interface is missing a method")






@check50.check()
def billable_exists():
    """Billable.java exists"""
    check50.exists("Billable.java")

@check50.check(billable_exists)
def billable_has_interface_method():
    with open("Billable.java") as f:
        fileString = f.read().replace("\n", "")

    methodStr = "public void payBill("

    if methodStr not in fileString:
        raise check50.Mismatch(methodStr, "", help="Your Billable interface is missing a method")



@check50.check()
def payable_exists():
    """Payable.java exists"""
    check50.exists("Payable.java")

@check50.check(billable_exists)
def payable_has_interface_method():
    with open("Payable.java") as f:
        fileString = f.read().replace("\n", "")

    methodStr = "public void payAmount("

    if methodStr not in fileString:
        raise check50.Mismatch(methodStr, "", help="Your Payable interface is missing a method")






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
        args=['--select-method', 'StudentTest#testGrades'])

@check50.check(student_compiles)
def student_email():
    """Student method \"sendEmail\" works as expected"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testEmail'])

@check50.check(student_compiles)
def student_degree():
    """Student method awardDegree works as expected"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testDegree'])


@check50.check(student_compiles)
def student_implements_degreeable():
    """Student is an instance of degreeable"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testImplementedDegreeable'])

@check50.check(student_compiles)
def student_bill():
    """Student can be billed as expected"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'StudentTest#testBill'])






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
def lecturer_set_name():
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

@check50.check(lecturer_compiles)
def lecturer_grade():
    """Lecturer \"TimeTable\" setters work as expected"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'LecturerTest#testTimeTable'])

@check50.check(lecturer_compiles)
def lecturer_implements_payable():
    """Lecturer implements Payable"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'LecturerTest#testImplementedPayable'])

@check50.check(lecturer_compiles)
def lecturer_gets_paid():
    """payAmount method works as expected for Lecturer"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'LecturerTest#testPayLecturer'])








@check50.check()
def professor_exists():
    """Professor.java exists"""
    check50.exists("Professor.java")

@check50.check(professor_exists)
def professor_compiles():
    """Professor.java compiles"""
    check50_java.compile("Professor.java")

@check50.check(professor_compiles)
def professor_is_lecturer():
    """Professor is an instance of \"Lecturer\""""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ProfessorTest#testInheritedLecturer'])

@check50.check(professor_compiles)
def professor_set_name():
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
def professor_grade():
    """Professor \"TimeTable\" setters work as expected"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ProfessorTest#testTimeTable'])

@check50.check(professor_compiles)
def prof_implements_payable():
    """ProfessorTest implements Payable"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ProfessorTest#testImplementedPayable'])

@check50.check(professor_compiles)
def prof_gets_paid():
    """payAmount method works as expected for ProfessorTest"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ProfessorTest#testPayProf'])









@check50.check()
def laika_exists():
    """Dog.java exists"""
    check50.exists("Dog.java")

@check50.check(laika_exists)
def laika_compiles():
    """Dog.java compiles"""
    check50_java.compile("Dog.java")

@check50.check(laika_compiles)
def test_good_girl():
    """Dog \"goodGirl\" is private"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'DogTest#testGoodGirlIsPrivate'])

@check50.check(laika_compiles)
def test_award_degree_public():
    """Dog \"awardDegree\" is public"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'DogTest#testAwardDegreeIsPublic'])

@check50.check(laika_compiles)
def test_dog_degreeable():
    """Dog implements degreeable"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'DogTest#testImplementedDegreeable'])

@check50.check(laika_compiles)
def test_award_laika_degree():
    """Degree awarded with fitting dignity"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'DogTest#testAwardDegree'])




@check50.check()
def rc_exists():
    """ResearchCouncil.java exists"""
    check50.exists("ResearchCouncil.java")

@check50.check(rc_exists)
def rc_compiles():
    """ResearchCouncil.java compiles"""
    check50_java.compile("ResearchCouncil.java")

@check50.check(rc_compiles)
def rc_name_private():
    """Research Council \"name\" is private"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ResearchCouncilTest#testNameIsPrivate'])

@check50.check(rc_compiles)
def rc_email_private():
    """Research Council \"email\" is private"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ResearchCouncilTest#testEmailIsPrivate'])

@check50.check(rc_compiles)
def rc_name_set():
    """Research Council \"name\" can be set with setter"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ResearchCouncilTest#testNameSet'])

@check50.check(rc_compiles)
def rc_test_greet():
    """Research Council \"greet\" works to spec"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ResearchCouncilTest#testGreet'])

@check50.check(rc_compiles)
def rc_test_implement_emailable():
    """Research Council implements \"Emailable\""""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ResearchCouncilTest#testImplementedEmailable'])

@check50.check(rc_compiles)
def rc_test_email():
    """Research Council \"sendEmail\" works"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ResearchCouncilTest#testEmail'])

@check50.check(rc_compiles)
def rc_test_billable():
    """Research Council implements \"Billable\""""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ResearchCouncilTest#testImplementedBillable'])

@check50.check(rc_compiles)
def rc_test_bill():
    """Research Council \"payBill\" works"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ResearchCouncilTest#testBill'])






