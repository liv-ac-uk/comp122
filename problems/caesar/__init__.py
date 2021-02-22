import check50
import check50_java
import check50_junit
import check50_checkstyle


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
def caesar_has_rotate_is_public():
    """Caesar has a public static methos called \"rotate\""""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'CaesarTest#rotateExists'])


@check50.check(caesar_compiles)
def caesar_rotate_signature():
    """Caesar has the correct signature for \"rotate\""""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'CaesarTest#rotateCharSignatureCorrect'])


@check50.check(caesar_compiles)
def caesar_rotate_lower_shift_5():
    """Caesar rotates lower case chars to the right values with a shift 5"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'CaesarTest#testLowerCharShiftZero'])


@check50.check(caesar_compiles)
def caesar_rotate_lower_shift_19():
    """Caesar rotates lower case chars to the right values with a shift 19"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'CaesarTest#testLowerCharShiftNineteen'])


@check50.check(caesar_compiles)
def caesar_rotate_signature():
    """Caesar has the correct signature for \"rotate\""""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'CaesarTest#rotateStringSignatureCorrect'])


@check50.check(caesar_compiles)
def caesar_main_exists():
    """Test main exists"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'CaesarTest#mainExists'])


@check50.check(caesar_main_exists)
def caesar_first_example():
    """See if we get the right output for the first example and a shift of 3"""
    check50_java.run("Caesar 3 \"The ships hung in the sky in much the same way that bricks don't.\"").stdout(
        "Wkh vklsv kxqj lq wkh vnb lq pxfk wkh vdph zdb wkdw eulfnv grq'w.\n")



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
def check_brutus_first_example():
    """See if we get the right output for the first example"""
    check50_java.run("Brutus \"Vg vf n zvfgnxr gb guvax lbh pna fbyir nal znwbe ceboyrzf whfg jvgu cbgngbrf.\"").stdout("It is a mistake to think you can solve any major problems just with potatoes.\n")

@check50.check(brutus_main_exists)
def check_brutus_second_example():
    """See if we get the right output for the second example"""
    check50_java.run("Brutus").stdout("Too few parameters!\nUsage: java Brutus \"cipher text\"\n")
