import check50
import check50_java
import check50_junit
import check50_checkstyle
import re


#####################################
# Item
#####################################
@check50.check()
def item_exists():
    """Item.java exists"""
    check50.exists("Item.java")


@check50.check(item_exists)
def item_compiles():
    """Item.java compiles"""
    check50_java.compile("Item.java")


@check50.check(item_compiles)
def item_constructor():
    """Item constructor as expected"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ItemTest#testInstantiate'])


@check50.check(item_constructor)
def item_getPrice():
    """Item.getPrice()"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ItemTest#getPrice'])


@check50.check(item_constructor)
def item_getDescription():
    """Item.getDescription()"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ItemTest#getDescription'])


@check50.check(item_constructor)
def item_pricePerUnitWeight():
    """Item.pricePerUnitWeight()"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ItemTest#pricePerUnitWeight'])


@check50.check(item_constructor)
def item_toString():
    """Item.toString()"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'ItemTest#testToString'])


@check50.check(item_compiles)
def item_checkstyle_naming_conventions():
    """Item.java follows naming conventions"""
    style_file = "naming-conventions.xml"
    target = "Item.java"

    check50.include("checkstyle/" + style_file)
    check50_checkstyle.run_and_interpret_checkstyle(
        checks_file=style_file,
        rationale="{report}",
        target=target)


@check50.check(item_compiles)
def item_checkstyle_javadoc_missing():
    """Item.java has javadocs for all methods"""
    style_file = "javadoc-missing-methods.xml"
    target = "Item.java"

    check50.include("checkstyle/" + style_file)
    check50_checkstyle.run_and_interpret_checkstyle(
        checks_file=style_file,
        rationale="{report}",
        target=target)


@check50.check(item_checkstyle_javadoc_missing)
def item_checkstyle_javadoc_picky():
    """Item.java has pretty Javadocs"""
    style_file = "javadoc-picky.xml"
    target = "Item.java"

    check50.include("checkstyle/" + style_file)
    check50_checkstyle.run_and_interpret_checkstyle(
        checks_file=style_file,
        rationale="{report}",
        target=target)

###############################################
# Drink
###############################################

@check50.check()
def drink_exists():
    """Drink.java exists"""
    check50.exists("Drink.java")


@check50.check(drink_exists)
def drink_compiles():
    """Drink.java compiles."""
    check50_java.compile("Drink.java")


@check50.check(drink_compiles)
def drink_isItem():
    """Drink is Item"""
    check50.include("tests/HierarchyTest.java")
    check50_junit.compile_test("HierarchyTest.java")
    check50_junit.run_and_interpret_test(
        args=['--select-method', 'HierarchyTest#drinkIsItem'])


@check50.check(drink_compiles)
def drink_constructor():
    """Drink constructor as expected"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'DrinkTest#testInstantiate'])


@check50.check(drink_constructor)
def drink_getVolume():
    """Drink.getVolume()"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'DrinkTest#getVolume'])


@check50.check(drink_constructor)
def drink_toString():
    """Drink.toString()"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'DrinkTest#testToString'])


@check50.check(drink_compiles)
def drink_checkstyle_naming_conventions():
    """Drink.java follows naming conventions"""
    style_file = "naming-conventions.xml"
    target = "Drink.java"

    check50.include("checkstyle/" + style_file)
    check50_checkstyle.run_and_interpret_checkstyle(
        checks_file=style_file,
        rationale="{report}",
        target=target)


@check50.check(drink_compiles)
def drink_checkstyle_javadoc_missing():
    """Drink.java has javadocs for all methods"""
    style_file = "javadoc-missing-methods.xml"
    target = "Drink.java"

    check50.include("checkstyle/" + style_file)
    check50_checkstyle.run_and_interpret_checkstyle(
        checks_file=style_file,
        rationale="{report}",
        target=target)


@check50.check(drink_checkstyle_javadoc_missing)
def drink_checkstyle_javadoc_picky():
    """Drink.java has pretty Javadocs"""
    style_file = "javadoc-picky.xml"
    target = "Drink.java"

    check50.include("checkstyle/" + style_file)
    check50_checkstyle.run_and_interpret_checkstyle(
        checks_file=style_file,
        rationale="{report}",
        target=target)

###############################################
# Sandwich
###############################################

@check50.check()
def sandwich_exists():
    """Sandwich.java exists"""
    check50.exists("Sandwich.java")


@check50.check(sandwich_exists)
def sandwich_compiles():
    """Sandwich.java compiles."""
    check50_java.compile("Sandwich.java")


@check50.check(sandwich_compiles)
def sandwich_isItem():
    """Sandwich is Item"""
    check50.include("tests/HierarchyTest.java")
    check50_junit.compile_test("HierarchyTest.java")
    check50_junit.run_and_interpret_test(
        args=['--select-method', 'HierarchyTest#sandwichIsItem'])


@check50.check(sandwich_compiles)
def sandwich_constructor():
    """Sandwich constructor as expected"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'SandwichTest#testInstantiate'])


@check50.check(sandwich_constructor)
def sandwich_getCalories():
    """Sandwich.getCalories()"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'SandwichTest#getCalories'])


@check50.check(sandwich_constructor)
def sandwich_toString():
    """Sandwich.toString()"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'SandwichTest#testToString'])


@check50.check(sandwich_compiles)
def sandwich_checkstyle_naming_conventions():
    """Sandwich.java follows naming conventions"""
    style_file = "naming-conventions.xml"
    target = "Sandwich.java"

    check50.include("checkstyle/" + style_file)
    check50_checkstyle.run_and_interpret_checkstyle(
        checks_file=style_file,
        rationale="{report}",
        target=target)


@check50.check(sandwich_compiles)
def sandwich_checkstyle_javadoc_missing():
    """Sandwich.java has javadocs for all methods"""
    style_file = "javadoc-missing-methods.xml"
    target = "Sandwich.java"

    check50.include("checkstyle/" + style_file)
    check50_checkstyle.run_and_interpret_checkstyle(
        checks_file=style_file,
        rationale="{report}",
        target=target)


@check50.check(sandwich_checkstyle_javadoc_missing)
def sandwich_checkstyle_javadoc_picky():
    """Sandwich.java has pretty Javadocs"""
    style_file = "javadoc-picky.xml"
    target = "Sandwich.java"

    check50.include("checkstyle/" + style_file)
    check50_checkstyle.run_and_interpret_checkstyle(
        checks_file=style_file,
        rationale="{report}",
        target=target)

###############################################
# Snack
###############################################

@check50.check()
def snack_exists():
    """Snack.java exists"""
    check50.exists("Snack.java")


@check50.check(snack_exists)
def snack_compiles():
    """Snack.java compiles"""
    check50_java.compile("Snack.java")


@check50.check(snack_compiles)
def snack_isItem():
    """Snack is Item"""
    check50.include("tests/HierarchyTest.java")
    check50_junit.compile_test("HierarchyTest.java")
    check50_junit.run_and_interpret_test(
        args=['--select-method', 'HierarchyTest#snackIsItem'])


@check50.check(snack_compiles)
def snack_constructor():
    """Snack constructor as expected"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'SnackTest#testInstantiate'])


@check50.check(snack_constructor)
def snack_getHealthy():
    """Snack.getHealthy()"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'SnackTest#getHealthy'])


@check50.check(snack_constructor)
def snack_toString():
    """Snack.toString()"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'SnackTest#testToString'])


@check50.check(snack_compiles)
def snack_checkstyle_naming_conventions():
    """Snack.java follows naming conventions"""
    style_file = "naming-conventions.xml"
    target = "Snack.java"

    check50.include("checkstyle/" + style_file)
    check50_checkstyle.run_and_interpret_checkstyle(
        checks_file=style_file,
        rationale="{report}",
        target=target)


@check50.check(snack_compiles)
def snack_checkstyle_javadoc_missing():
    """Snack.java has javadocs for all methods"""
    style_file = "javadoc-missing-methods.xml"
    target = "Snack.java"

    check50.include("checkstyle/" + style_file)
    check50_checkstyle.run_and_interpret_checkstyle(
        checks_file=style_file,
        rationale="{report}",
        target=target)


@check50.check(snack_checkstyle_javadoc_missing)
def snack_checkstyle_javadoc_picky():
    """Snack.java has pretty Javadocs"""
    style_file = "javadoc-picky.xml"
    target = "Snack.java"

    check50.include("checkstyle/" + style_file)
    check50_checkstyle.run_and_interpret_checkstyle(
        checks_file=style_file,
        rationale="{report}",
        target=target)

#####################################
# Basket
#####################################
@check50.check()
def basket_exists():
    """Basket.java exists"""
    check50.exists("Basket.java")


@check50.check(basket_exists)
def basket_compiles():
    """Basket.java compiles"""
    check50_java.compile("Basket.java")


#@check50.check(basket_compiles)
#@check50.hidden("basket needs all Item subclasses.")
#def basket_all_items():
#    item_compiles.__wrapped__()


@check50.check(basket_compiles)
def basket_constructor():
    """Basket constructor as expected"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'BasketTest#testInstantiate'])


@check50.check(basket_constructor)
def basket_add():
    """Basket.add()"""
    # compile Item class imported in BasketTest.java
    # to ensure that junit runs successfully.
    item_compiles.__wrapped__()
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'BasketTest#testAdd'])


@check50.check(basket_constructor)
def basket_getPrice():
    """Basket.getPrice()"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'BasketTest#getPrice'])


@check50.check(basket_getPrice)
def basket_addAndGetPrice():
    """Basket.add() and Basket.getPrice() work together"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'BasketTest#addAndGetPrice'])


@check50.check(basket_constructor)
def basket_getWeight():
    """Basket.add() and Basket.getWeight()"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'BasketTest#getWeight'])


@check50.check(basket_getWeight)
def basket_addAndGetWeight():
    """Basket.add() and Basket.getWeight() work together"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'BasketTest#addAndGetWeight'])


@check50.check(basket_add)
def basket_toString():
    """Basket.toString()"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'BasketTest#testToString'])


@check50.check(basket_compiles)
def basket_main_exists():
    """Basket is application class"""
    check50_java.checks.is_application_class("Basket")


def read_mainsrc():
    with open("Basket.java") as f:
        src = f.read()

        # remove multiline comments
        src = re.sub(r'/\*\*.*?\*\/', r'', src, flags=re.DOTALL)

        # remove normal comments
        src = re.sub(r'\s*\/\/.*$', '', src)

        src = src.strip()
        mainsrc = ""
        m = re.match(r'.*(public static void main\(.*})', src, re.DOTALL)
        if m:
            mainsrc = m.groups()[0]
        return mainsrc


@check50.check(basket_main_exists)
def basket_main_instantiates_basket():
    """Basket main instantiates Basket"""
    mainsrc = read_mainsrc()
    if not r'new Basket(' in mainsrc:
        raise check50.Failure("Basket.main does not instantiate Basket")


@check50.check(basket_main_exists)
def basket_main_uses_add():
    """Basket main uses Basket.add"""
    mainsrc = read_mainsrc()
    if not r'.add(' in mainsrc:
        raise check50.Failure("Basket.main does not use Basket.add")


@check50.check(basket_main_exists)
def basket_main_output():
    """Basket.main()"""
    expected = """---
[Cola; price:100p weight:400g volume:330ml]
[OJ; price:100p weight:300g volume:200ml]
[BLT; price:200p weight:200g calories:450kcal]
[Grapes; price:50p weight:200g healthy:Yes]
---
Total weight: 1300g
Total price: 450p
"""
    actual = check50_java.run("Basket").stdout()
    actual = actual.replace('\r', '')
    help = "did you introduce training newline or whitespace characters?"
    if actual != expected:
        raise check50.Mismatch(expected, actual, help=help)


@check50.check(basket_compiles)
def basket_checkstyle_naming_conventions():
    """Basket.java follows naming conventions"""
    style_file = "naming-conventions.xml"
    target = "Basket.java"

    check50.include("checkstyle/" + style_file)
    check50_checkstyle.run_and_interpret_checkstyle(
        checks_file=style_file,
        rationale="{report}",
        target=target)


@check50.check(basket_compiles)
def basket_checkstyle_javadoc_missing():
    """Basket.java has javadocs for all methods"""
    style_file = "javadoc-missing-methods.xml"
    target = "Basket.java"

    check50.include("checkstyle/" + style_file)
    check50_checkstyle.run_and_interpret_checkstyle(
        checks_file=style_file,
        rationale="{report}",
        target=target)


@check50.check(basket_checkstyle_javadoc_missing)
def basket_checkstyle_javadoc_picky():
    """Basket.java has pretty Javadocs"""
    style_file = "javadoc-picky.xml"
    target = "Basket.java"

    check50.include("checkstyle/" + style_file)
    check50_checkstyle.run_and_interpret_checkstyle(
        checks_file=style_file,
        rationale="{report}",
        target=target)


@check50.check()
def report_exists():
    """UML diagram exists"""
    check50.exists("UML.pdf")

