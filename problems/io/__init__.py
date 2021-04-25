import check50
import check50_java
import check50_junit

@check50.check()
def io_lab_part_one_exists():
    """IOLabPartOne.java exists."""
    check50.exists("IOLabPartOne.java")

@check50.check(io_lab_part_one_exists)
def io_lab_part_one_compiles():
    """IOLabPartOne.java compiles."""
    check50.include("OurData.class")  # copy over OurData
    check50.include("programs.txt")
    check50.include("programsTwo.txt")
    check50_java.compile("IOLabPartOne.java")
    
@check50.check(io_lab_part_one_compiles)
def default_file_correct_test():
    """Tests that you are correctly processing default file programs.txt """
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'IOLabPartOneTest#defaultFileCorrect'])

@check50.check(io_lab_part_one_compiles)
def different_file_correct_test():
    """Ensures default file values aren't hardcoded """
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'IOLabPartOneTest#differentFileCorrect'])
        
@check50.check(io_lab_part_one_compiles)
def type_correct_test():
    """Ensures values are being stored to OurData as correct type """
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'IOLabPartOneTest#typeCorrectTest'])
