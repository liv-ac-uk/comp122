import check50
import check50_java
import check50_junit
import os

## Cipher ###########################
@check50.check()
def cipher_unmodified():
    """Ensure that the cipher file has not been modified"""
    check50.include("ModelCipher.java")  # copy over input helper
    exit_code = os.system('cmp -s Cipher.java ModelCipher.java')
    if exit_code != 0:
        raise check50.Failure("Your Cipher class must be unmodified")


# Substitution ###############################
@check50.check()
def substitution_exists():
    """Substitution.java exists"""
    check50.exists("Substitution.java")


@check50.check(substitution_exists)
def substitution_compiles():
    """Substitution.java compiles"""
    check50_java.compile("Substitution.java")


@check50.check(substitution_compiles)
def substitution_is_abstract():
    """Substitution.java is abstract"""
    lines = []

    with open("Substitution.java") as f:
        for line in f:
            lines.append(line.replace("\n", ""))

    for line in lines:
        if "Substitution" in line and "class" in line and "public" in line and "abstract" in line:
            return
        else:
            pass

    raise check50.Failure("Your Substitution class must be abstract")


@check50.check(substitution_compiles)
def substitution_implements_cipher():
    """Substitution.java implements cipher"""
    lines = []

    with open("Substitution.java") as f:
        for line in f:
            lines.append(line.replace("\n", ""))

    for line in lines:
        if "Substitution" in line and "class" in line and "implements" in line and "Cipher" in line:
            return
        else:
            pass

    raise check50.Failure("Your Substitution class must implement Cipher")


@check50.check(substitution_compiles)
def substitution_check_encrypt():
    """Substitution.java has an abstract method encrypt(char) that returns char"""
    lines = []

    with open("Substitution.java") as f:
        for line in f:
            lines.append(line.replace("\n", ""))

    for line in lines:
        if "public abstract char encrypt(char c);" in line:
            return
        else:
            pass

    raise check50.Failure("Your Substitution class must have the method \"public abstract char encrypt(char c);\"")


@check50.check(substitution_compiles)
def substitution_check_decrypt():
    """Substitution.java has an abstract method decrypt(char) that returns char"""
    lines = []

    with open("Substitution.java") as f:
        for line in f:
            lines.append(line.replace("\n", ""))

    for line in lines:
        if "public abstract char decrypt(char c);" in line:
            return
        else:
            pass

    raise check50.Failure("Your Substitution class must have the method \"public abstract char decrypt(char c);\"")


@check50.check(substitution_compiles)
def substitution_encrypt_string():
    """Substitution.java implements encrypt(String) as expected"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'SubstitutionTest#substitutionCheckEncrypt'])


@check50.check(substitution_compiles)
def substitution_decrypt_string():
    """Substitution.java implements decrypt(String) as expected"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'SubstitutionTest#substitutionCheckDecrypt'])


# MonoAlphaSubstitution ###############################
@check50.check()
def mas_exists():
    """MonoAlphaSubstitution.java exists"""
    check50.exists("MonoAlphaSubstitution.java")


@check50.check(mas_exists)
def mas_compiles():
    """MonoAlphaSubstitution.java compiles"""
    check50_java.compile("MonoAlphaSubstitution.java")


@check50.check(mas_compiles)
def mas_is_not_abstract():
    """MonoAlphaSubstitution.java is not abstract"""
    lines = []

    with open("MonoAlphaSubstitution.java") as f:
        for line in f:
            lines.append(line.replace("\n", ""))

    for line in lines:
        if "MonoAlphaSubstitution" in line and "class" in line and "public" in line and "abstract" not in line:
            return
        else:
            pass

    raise check50.Failure("Your MonoAlphaSubstitution class cannot be abstract")


@check50.check(mas_compiles)
def mas_has_default_constructor():
    """MonoAlphaSubstitution.java has default constructor"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'MonoAlphaSubstitutionTest#masHasDefaultConstructor'])


@check50.check(mas_compiles)
def mas_has_string_constructor():
    """MonoAlphaSubstitution.java has string constructor"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'MonoAlphaSubstitutionTest#masHasStringConstructor'])


@check50.check(mas_compiles)
def mas_encrypt_default():
    """MonoAlphaSubstitution.java encrypt(char c) works as identity using the default constructor"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'MonoAlphaSubstitutionTest#masEncryptDefault'])


@check50.check(mas_compiles)
def mas_encrypt_empty():
    """MonoAlphaSubstitution.java encrypt(char c) works as identity using the empty string"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'MonoAlphaSubstitutionTest#masEncryptEmpty'])


@check50.check(mas_compiles)
def mas_encrypt_test_01():
    """MonoAlphaSubstitution.java encrypt(char c) works as expected with key akbjcidhegffgehdicjbka on given input"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'MonoAlphaSubstitutionTest#masEncryptTest01'])



@check50.check(mas_compiles)
def mas_decrypt_test_01():
    """MonoAlphaSubstitution.java decrypt(char c) works as expected given input"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'MonoAlphaSubstitutionTest#masDecryptTest01'])


@check50.check(mas_compiles)
def mas_main_exists():
    """MonoAlphaSubstitution.java has main method"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'MonoAlphaSubstitutionTest#masMainExists'])


@check50.check(mas_main_exists)
def mas_main_returns_successfully():
    """See if MonoAlphaSubstitution.main runs successfuly without runtime errors
       and without waiting for user input"""
    check50_java.run("MonoAlphaSubstitution encrypt abcd lalala").exit(0)


@check50.check(mas_main_returns_successfully)
def mas_main_test_01():
    """java MonoAlphaSubstitution encrypt akbjcidhegffgehdicjbka "Life is wasted on the living." works as expected"""
    check50_java.run("MonoAlphaSubstitution encrypt akbjcidhegffgehdicjbka \"Life is wasted on the living.\"").stdout("Lcfg cs wkstgh on tdg lcvcne.\n")


@check50.check(mas_main_returns_successfully)
def mas_main_test_02():
    """java MonoAlphaSubstitution decrypt akbjcidhegffgehdicjbka "Life is wasted on the living." works as expected"""
    check50_java.run("MonoAlphaSubstitution decrypt akbjcidhegffgehdicjbka \"Lcfg cs wkstgh on tdg lcvcne.\"").stdout("Life is wasted on the living.\n")


@check50.check(mas_main_exists)
def mas_check_many_args():
    """See if we get the right error message when MonoAlphaSubstitution is run with too many arguments"""
    check50_java.run("MonoAlphaSubstitution 13 a 13 13").stdout("Too many parameters!\nUsage: java MonoAlphaSubstitution encrypt key \"cipher text\"\n")


@check50.check(mas_main_exists)
def mas_check_one_arg():
    """See if we get the right error message when MonoAlphaSubstitution is run with just one argument"""
    check50_java.run("MonoAlphaSubstitution 3").stdout("Too few parameters!\nUsage: java MonoAlphaSubstitution encrypt key \"cipher text\"\n")


@check50.check(mas_main_exists)
def mas_check_first_arg():
    """See if we get the right error message when MonoAlphaSubstitution is run with an incorrect first argument"""
    check50_java.run("MonoAlphaSubstitution dec akbjcidhegffgehdicjbka lala").stdout("The first parameter must be \"encrypt\" or \"decrypt\"!\nUsage: java MonoAlphaSubstitution encrypt key \"cipher text\"\n")


# # Caesar ###############################
@check50.check()
def caesar_exists():
    """Caesar.java exists"""
    check50.exists("Caesar.java")


@check50.check(caesar_exists)
def caesar_compiles():
    """Caesar.java compiles"""
    check50_java.compile("Caesar.java")


@check50.check(caesar_compiles)
def caesar_is_not_abstract():
    """Caesar.java is not abstract"""
    lines = []

    with open("Caesar.java") as f:
        for line in f:
            lines.append(line.replace("\n", ""))

    for line in lines:
        if "Caesar" in line and "class" in line and "public" in line and "abstract" not in line:
            return
        else:
            pass

    raise check50.Failure("Your Caesar class cannot be abstract")


@check50.check(caesar_compiles)
def caesar_has_default_constructor():
    """Caesar.java has default constructor"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'CaesarTest#caesarHasDefaultConstructor'])


@check50.check(caesar_compiles)
def caesar_has_integer_constructor():
    """Caesar.java has integer constructor"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'CaesarTest#caesarHasIntegerConstructor'])


@check50.check(caesar_compiles)
def caesar_encrypt_test_01():
    """Caesar.java encrypt(char c) works as expected with key 10:  fun --> pex"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'CaesarTest#caesarEncryptTest01'])


@check50.check(caesar_compiles)
def caesar_decrypt_test_01():
    """Caesar.java decrypt(char c) works as expected with key 10:  pex --> fun"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'CaesarTest#caesarDecryptTest01'])


@check50.check(caesar_compiles)
def caesar_main_exists():
    """Caesar.java has main method"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'CaesarTest#caesarMainExists'])


@check50.check(caesar_main_exists)
def caesar_main_returns_successfully():
    """See if Caesar.main runs successfuly without runtime errors or waiting for input on stdin"""
    check50_java.run("Caesar encrypt 13 lalala").exit(0)


@check50.check(caesar_main_returns_successfully)
def caesar_main_test_01():
    """java Caesar encrypt 3 \"The ships hung in the sky in much the same way that bricks don't.\" works as expected"""
    check50_java.run("Caesar encrypt 3 \"The ships hung in the sky in much the same way that bricks don\'t.\"").stdout("Wkh vklsv kxqj lq wkh vnb lq pxfk wkh vdph zdb wkdw eulfnv grq\'w.\n")


@check50.check(caesar_main_returns_successfully)
def caesar_main_test_02():
    """java Caesar decrypt 3 \"Wkh vklsv kxqj lq wkh vnb lq pxfk wkh vdph zdb wkdw eulfnv grq'w.\" works as expected"""
    check50_java.run("Caesar decrypt 3 \"Wkh vklsv kxqj lq wkh vnb lq pxfk wkh vdph zdb wkdw eulfnv grq\'w.\"").stdout("The ships hung in the sky in much the same way that bricks don\'t.\n")


@check50.check(caesar_main_exists)
def caesar_check_many_args():
    """See if we get the right error message when running Caesar with too many arguments"""
    check50_java.run("Caesar encrypt 13 The ships hung in the sky in much the same way that bricks dont.\n").stdout("Too many parameters!\nUsage: java Caesar encrypt n \"cipher text\"\n")


@check50.check(caesar_main_exists)
def caesar_check_one_arg():
    """See if we get the right error message when running Caesar with too few arguments"""
    check50_java.run("Caesar encrypt 3").stdout("Too few parameters!\nUsage: java Caesar encrypt n \"cipher text\"\n")


@check50.check(caesar_main_exists)
def caesar_check_first_arg():
    """See if we get the right error message when Caesar is run with an incorrect first argument"""
    check50_java.run("Caesar dec 12 lala").stdout("The first parameter must be \"encrypt\" or \"decrypt\"!\nUsage: java Caesar encrypt n \"cipher text\"\n")


# # # Vigenere ###############################
@check50.check()
def vigenere_exists():
    """Vigenere.java exists"""
    check50.exists("Vigenere.java")


@check50.check(vigenere_exists)
def vigenere_compiles():
    """Vigenere.java compiles"""
    check50_java.compile("Vigenere.java")


@check50.check(vigenere_compiles)
def vigenere_is_not_abstract():
    """Vigenere.java is not abstract"""
    lines = []

    with open("Vigenere.java") as f:
        for line in f:
            lines.append(line.replace("\n", ""))

    for line in lines:
        if "Vigenere" in line and "class" in line and "public" in line and "abstract" not in line:
            return
        else:
            pass

    raise check50.Failure("Your Vigenere class cannot be abstract")


@check50.check(vigenere_compiles)
def vigenere_has_default_constructor():
    """Vigenere.java has default constructor"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'VigenereTest#vigenereHasDefaultConstructor'])


@check50.check(vigenere_compiles)
def vigenere_has_string_constructor():
    """Vigenere.java has string constructor"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'VigenereTest#vigenereHasStringConstructor'])


@check50.check(vigenere_compiles)
def vigenere_encrypt_default():
    """Vigenere.java encrypt(char c) works as identity using the default constructor"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'VigenereTest#vigenereEncryptDefault'])


@check50.check(vigenere_compiles)
def vigenere_encrypt_test_01():
    """Vigenere.java encrypt(char c) works as expected given input"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'VigenereTest#vigenereEncryptTest01'])


@check50.check(vigenere_compiles)
def vigenere_decrypt_test_01():
    """Vigenere.java decrypt(char c) works as expected given input"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'VigenereTest#vigenereDecryptTest01'])


@check50.check(vigenere_compiles)
def vigenere_main_exists():
    """Vigenere.java has main method"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'VigenereTest#vigenereMainExists'])


@check50.check(vigenere_main_exists)
def vigenere_main_returns_successfully():
    """See if Vigenere.main runs successfuly without runtime errors"""
    check50_java.run("Vigenere encrypt COMP lalala").exit(0)


@check50.check(vigenere_main_returns_successfully)
def vigenere_main_test_01():
    """java Vigenere encrypt COMPONETWOTWO \"fun fun fun\" works as expected"""
    check50_java.run("Vigenere encrypt COMPONETWOTWO \"fun fun fun\"").stdout("hiz thr big\n")


@check50.check(vigenere_main_returns_successfully)
def vigenere_main_test_02():
    """java Vigenere decrypt COMPONETWOTWO \"hiz thr big\" works as expected"""
    check50_java.run("Vigenere decrypt COMPONETWOTWO \"hiz thr big\"").stdout("fun fun fun\n")



@check50.check(vigenere_main_exists)
def vigenere_check_many_args():
    """See if we get the right error message when Vigenere run with too many arguments"""
    check50_java.run("Vigenere encrypt COMPONETWOTWO fun fun fun\n").stdout("Too many parameters!\nUsage: java Vigenere encrypt key \"cipher text\"\n")


@check50.check(vigenere_main_exists)
def vigenere_check_one_arg():
    """See if we get the right error message when Vigenere run with too few arguments"""
    check50_java.run("Vigenere decrypt COMPONETWOTWO").stdout("Too few parameters!\nUsage: java Vigenere encrypt key \"cipher text\"\n")


@check50.check(vigenere_main_exists)
def vigenere_check_first_arg():
    """See if we get the right error message when Vigenere is run with an incorrect first argument"""
    check50_java.run("Vigenere enc COMPONETWOTWO lala").stdout("The first parameter must be \"encrypt\" or \"decrypt\"!\nUsage: java Vigenere encrypt key \"cipher text\"\n")
