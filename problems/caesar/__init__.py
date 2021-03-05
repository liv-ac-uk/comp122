import check50
import check50_java
import check50_junit


# Caesar ##################################################################
@check50.check()
def caesar_exists():
    """Caesar.java exists"""
    check50.exists("Caesar.java")


@check50.check(caesar_exists)
def caesar_compiles():
    """Caesar.java compiles"""
    check50_java.compile("Caesar.java")


@check50.check(caesar_compiles)
def caesar_rotate_char_exists():
    """Caesar.rotate(int,char) exists"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'CaesarTest#rotateCharExists'])


@check50.check(caesar_rotate_char_exists)
def caesar_rotate_char_signature():
    """Caesar.rotate(int,char) is public static"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'CaesarTest#rotateCharSignatureCorrect'])


@check50.check(caesar_rotate_char_signature)
def caesar_rotate_lower_shift_5():
    """trying out Caesar(int,char) on "abc...z" with a shift 5"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'CaesarTest#testLowerCharShiftFive'])


@check50.check(caesar_rotate_char_signature)
def caesar_rotate_lower_shift_19():
    """trying out Caesar(int,char) on "abc...z" with a shift 19"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'CaesarTest#testLowerCharShiftNineteen'])


@check50.check(caesar_compiles)
def caesar_rotate_string_signature():
    """Caesar.rotate(int,String) is public static"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'CaesarTest#rotateStringSignatureCorrect'])


@check50.check(caesar_compiles)
def caesar_main_exists():
    """Caesar.main exists"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'CaesarTest#mainExists'])


@check50.check(caesar_main_exists)
def caesar_main_returns_successfully():
    """See if Caesar.main runs successfuly without runtime errors"""
    check50_java.run("Caesar 13 lalala").exit(0)


@check50.check(caesar_main_returns_successfully)
def caesar_many_args():
    """See if we get the right error message whe run with too many arguments"""
    out = "Too many parameters!\s*\n\s*Usage: java Caesar n \"cipher text\"\s*"
    check50_java.run("Caesar 13 The ships hung in the sky in much the same way that bricks dont.").stdout(out,regex=True)


@check50.check(caesar_main_returns_successfully)
def caesar_one_arg():
    """See if we get the right error message whe run with a single argument"""
    out = "Too few parameters!\nUsage: java Caesar n \"cipher text\"\s*"
    check50_java.run("Caesar 3").stdout(out, regex=True)


@check50.check(caesar_main_returns_successfully)
def caesar_first_example():
    """See if we get the right output for the first example and a shift of 3"""
    inp = "The ships hung in the sky in much the same way that bricks don't."
    out = r'Wkh vklsv kxqj lq wkh vnb lq pxfk wkh vdph zdb wkdw eulfnv grq\'w.\s*'
    check50_java.run("Caesar 3 \"" + inp + "\"").stdout(out, regex=True)



# Brutus ##################################################################
@check50.check()
def brutus_exists():
    """Brutus.java exists"""
    check50.exists("Brutus.java")


@check50.check(brutus_exists)
def brutus_compiles():
    """Brutus.java compiles"""
    check50_java.compile("Brutus.java")


@check50.check(brutus_compiles)
def brutus_has_count_is_public():
    """Brutus has a public static method called \"count\""""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'BrutusTest#countExists'])


@check50.check(brutus_compiles)
def brutus_has_count_signature():
    """Brutus \"count\" has right signature"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'BrutusTest#countSignatureCorrect'])


@check50.check(brutus_compiles)
def brutus_has_frequency_is_public():
    """Brutus has a public static method called \"frequency\""""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'BrutusTest#frequencyExists'])


@check50.check(brutus_compiles)
def brutus_has_frequency_signature():
    """Brutus \"frequency\" has right signature"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'BrutusTest#frequencySignatureCorrect'])


@check50.check(brutus_compiles)
def brutus_has_chi_is_public():
    """Brutus has a public static method called \"chiSquared\""""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'BrutusTest#chiExists'])


@check50.check(brutus_compiles)
def brutus_has_chi_signature():
    """Brutus \"chiSquared\" has right signature"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'BrutusTest#chiSignatureCorrect'])


@check50.check(brutus_compiles)
def brutus_main_exists():
    """Brutus has a public static method called \"main\""""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'BrutusTest#mainExists'])


@check50.check(brutus_main_exists)
def brutus_main_returns_successfully():
    """See if Brutus.main runs successfuly without runtime errors"""
    check50_java.run("Brutus lalala").exit(0)


@check50.check(brutus_main_returns_successfully)
def check_brutus_first_example():
    """See if we get the right output for the first example"""
    inp = "Vg vf n zvfgnxr gb guvax lbh pna fbyir nal znwbe ceboyrzf whfg jvgu cbgngbrf."
    out = "It is a mistake to think you can solve any major problems just with potatoes.\s*"
    check50_java.run("Brutus \"" + inp + "\"").stdout(out, regex=True)
