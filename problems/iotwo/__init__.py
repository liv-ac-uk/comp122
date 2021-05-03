import check50
import check50_java
import check50_junit


@check50.check()
def io_lab_part_two_exists():
    """IOLabPartTwo.java exists."""
    check50.exists("IOLabPartTwo.java")


@check50.check(io_lab_part_two_exists)
def io_lab_part_two_compiles():
    """IOLabPartTwo.java compiles."""
    check50.include("OurData.class")  # copy over OurData
    check50.include("programs.csv")
    check50.include("programsTwo.csv")
    check50_java.compile("IOLabPartTwo.java")


@check50.check(io_lab_part_two_compiles)
def default_file_correct_test():
    """Tests that you are correctly processing default file programs.csv """
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'IOLabPartTwoTest#defaultFileCorrect'])


@check50.check(io_lab_part_two_compiles)
def different_file_correct_test():
    """Ensures default file values aren't hardcoded """
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'IOLabPartTwoTest#differentFileCorrect'])


@check50.check(io_lab_part_two_compiles)
def type_correct_test():
    """Ensures values are being stored to OurData as correct type """
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'IOLabPartTwoTest#typeCorrectTest'])


@check50.check(io_lab_part_two_compiles)
def print_file_test():
    """Ensures printCSVFile correctly prints a csv file """
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'IOLabPartTwoTest#printFileCorrect'])
