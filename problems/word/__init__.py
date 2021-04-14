import check50
import check50_java
import os

@check50.check()
def wc_exists():
    """WC.java exists"""
    check50.exists("WC.java")

@check50.check(wc_exists)
def wc_compiles():
    """WC.java compiles"""
    check50_java.compile("WC.java")

@check50.check(wc_compiles)
def test_word_cat():
    """Ensures WC -w is still working on 'the cat sat on the mat'"""
    check50_java.run('WC -w "the cat sat on the mat"').stdout("6\n").exit()


@check50.check(wc_compiles)
def test_char_cat():
    """WC -m is returning the right value for 'the cat sat on the mat'"""
    cat = "the cat sat on the mat"

    check50_java.run(f'WC -m "{cat}"').stdout("22\n").exit()

@check50.check(wc_compiles)
def test_char_test():
    """WC -m is returning the right value for the first line of lorem ipsum"""
    ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

    check50_java.run(f'WC -m "{ipsum}"').stdout("56\n").exit()

@check50.check(wc_compiles)
def test_char_assessment():
    """WC -m is returning the right value for the first line of the Assessment 2 documentation"""
    ass2 = "In this coursework you will implement a whole bunch of simple substitution ciphers in an object oriented fashion, as depicted in the (incomplete) UML diagram below."
    check50_java.run(f'WC -m "{ass2}"').stdout("164\n").exit()

@check50.check(wc_compiles)
def test_lex_cat():
    """WC -s is returning the correct double for 'the cat sat on the mat'"""
    cat = "the cat sat on the mat"

    check50_java.run(f'WC -s "{cat}"').stdout(0.833333).exit()

@check50.check(wc_compiles)
def test_lex_test():
    """WC -s is returning the correct double for lexicographic diversity for lipsum """
    ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

    check50_java.run(f'WC -s "{ipsum}"').stdout(check50.regex.decimal("1")).exit()

@check50.check(wc_compiles)
def test_lex_assessment():
    """WC -s is returning the correct double for the Assessment 2 documenation"""
    ass2 = "In this coursework you will implement a whole bunch of simple substitution ciphers in an object oriented fashion, as depicted in the (incomplete) UML diagram below."

    check50_java.run(f'WC -s "{ass2}"').stdout("0.9615384340286255\n").exit()


@check50.check(wc_compiles)
def test_bag_cat():
    """WC -b is printing the integer array correctly for 'the cat sat on the mat'"""
    cat = "the cat sat the mat"

    check50_java.run(f'WC -b "{cat}"').stdout("[1, 1, 1, 2]\s").exit()

@check50.check(wc_compiles)
def test_bag_test():
    """WC -b is printing the integer array correctly for ipsum"""
    ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    check50_java.run(f'WC -b "{ipsum}"').stdout("[1, 1, 1, 1, 1, 1, 1, 1]\s").exit()

@check50.check(wc_compiles)
def test_bag_assessment():
    """WC -b is printing the integer array correctly for Assessment 2"""
    ass2 = "In this coursework you will implement a whole bunch of simple substitution ciphers in an object oriented fashion, as depicted in the (incomplete) UML diagram below."
    check50_java.run(f'WC -b "{ass2}"').stdout("[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]\s").exit()


@check50.check(wc_compiles)
def test_vec_cat_stat():
    """WC -v is printing the two integer arrays correctly for 'the cat sat on the mat' 'the pat sat on the stats'"""
    cat = "the cat sat on the mat"
    stat = "the pat sat on the stats"

    check50_java.run(f'WC -v "{cat}" "{stat}"').stdout("[1, 1, 1, 0, 1, 0, 2]\\s").stdout("[0, 0, 1, 1, 1, 1, 2]\\s").exit()

@check50.check(wc_compiles)
def test_vec_ipsum_cat():
    """WC -v is printing the two integer arrays correctly for ipsum and 'the cat sat on the mat'"""
    ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    cat = "the cat sat on the mat"
    check50_java.run(f'WC -v "{cat}" "{ipsum}"').stdout("[0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 2]\\s").stdout("[1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0]\\s").exit()

@check50.check(wc_compiles)
def test_vec_():
    """WC -v is printing the two integer arrays correctly for the Assessment 2 documenation and ipsum"""
    ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    ass2 = "In this coursework you will implement a whole bunch of simple substitution ciphers in an object oriented fashion, as depicted in the (incomplete) UML diagram below."

    check50_java.run(f'WC -v "{ipsum}" "{ass2}"').stdout("[0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]\\s").stdout("[1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 3, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1]\\s").exit()


@check50.check(wc_compiles)
def test_euc_cat_stat():
    """WC -d is printing the correct double for the Euclidean distance the two strings 'the cat sat on the mat' 'the pat sat on the stats'"""
    cat = "the cat sat on the mat"
    stat = "the pat sat on the stats"

    check50_java.run(f'WC -d "{cat}" "{stat}"').stdout(check50.regex.decimal("2.0")).exit()

@check50.check(wc_compiles)
def test_euc_ipsum_cat():
    """WC -d is printing the correct double for the Euclidean distance the two strings of ipsum and 'the cat sat on the mat'"""
    ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    cat = "the cat sat on the mat"
    check50_java.run(f'WC -d "{ipsum}" "{cat}"').stdout(check50.regex.decimal("4.0")).exit()

@check50.check(wc_compiles)
def test_euc_ass_ipsum():
    """WC -d is printing the correct double for the Euclidean distance the two strings of the Assessment 2 documenation and ipsum"""
    ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    ass2 = "In this coursework you will implement a whole bunch of simple substitution ciphers in an object oriented fashion, as depicted in the (incomplete) UML diagram below."

    check50_java.run(f'WC -d "{ipsum}" "{ass2}"').stdout(check50.regex.decimal("6.3245")).exit()

