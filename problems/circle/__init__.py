import check50
import check50_java


@check50.check()
def circle_exists():
    """Circle.java exists"""
    check50.exists("Circle.java")


@check50.check(circle_exists)
def circle_compiles():
    """Circle.java compiles"""
    check50_java.compile("Circle.java")


@check50.check(circle_compiles)
def circle_radius_is_private():
    """Circle has a private attribute called \"radius\""""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'CircleTest#testRadiusIsPrivate'])

@check50.check(circle_compiles)
def circle_default_constructor():
    """Circle default constructor"""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'CircleTest#testConstructor'])


@check50.check(circle_compiles)
def circle_constructor():
    """Circle constructor with double parameter"""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'CircleTest#testConstructor2'])


@check50.check(circle_constructor)
def circle_getRadius():
    """radius getter"""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'CircleTest#getRadius'])


@check50.check(circle_constructor)
def circle_setRadius():
    """radius setter"""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'CircleTest#setRadius'])


@check50.check(circle_constructor)
def circle_calcPerimeter():
    """calcPerimeter()"""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'CircleTest#testCalcPerimeter'])


@check50.check(circle_constructor)
def circle_calcArea():
    """calcArea()"""
    check50_java.junit5.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'CircleTest#testCalcArea'])


@check50.check()
def app_exists():
    """CircleApp.java exists"""
    check50.exists("Circle.java")


@check50.check(app_exists)
def app_compiles():
    """CircleApp.java compiles"""
    check50_java.compile("CircleApp.java")


@check50.check(app_compiles)
def main():
    """CircleApp output"""
    e = "perimeter: 75.39822368615503\narea: 452.3893421169302"

    check50_java.run("CircleApp").stdin("12.0").stdout(e).exit()
