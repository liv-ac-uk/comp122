import check50
import check50_java
import check50_checkstyle


@check50.check()
def compiles():
    """StringTools.java compiles."""
    check50.include("Comp122.class")
    check50_java.compile("StringTools.java")


@check50.check()
def exists():
    """docs/index.html has been generated"""
    check50.exists("docs/index.html")


@check50.check()
def checkstyle_javadoc_methods():
    """methods `swap` and `main` documented?"""
    stylefile = "styles/javadoc-method.xml"
    check50.include("styles")
    check50_checkstyle.run_and_interpret_checkstyle(
        checks_file=stylefile,
        rationale="{report}",
        target='StringTools.java')


@check50.check(checkstyle_javadoc_methods)
def checkstyle_javadoc_all():
    """javadoc being extra picky"""
    stylefile = "styles/javadoc-all.xml"
    check50_checkstyle.run_and_interpret_checkstyle(
        checks_file=stylefile,
        rationale="{report}",
        target='StringTools.java')
