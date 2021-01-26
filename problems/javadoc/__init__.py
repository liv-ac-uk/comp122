import check50
import check50_java
import check50_checkstyle


@check50.check()
def compiles():
    """StringTools.java compiles."""
    check50.include("Terminal.class")
    check50_java.compile("StringTools.java")


@check50.check()
def exists():
    """docs/index.html has been generated"""
    check50.exists("docs/index.html")


@check50.check()
def checkstyle_javadoc_methods():
    """all methods have javadoc strings"""
    stylefile = "styles/javadoc-missing-methods.xml"
    check50.include("styles")
    check50_checkstyle.run_and_interpret_checkstyle(
        checks_file=stylefile,
        rationale="{report}",
        target='StringTools.java')


@check50.check(checkstyle_javadoc_methods)
def checkstyle_javadoc_tags():
    """all javadoc strings have @param and @return tags"""
    stylefile = "styles/javadoc-tags.xml"
    check50.include("styles")
    check50_checkstyle.run_and_interpret_checkstyle(
        checks_file=stylefile,
        rationale="{report}",
        target='StringTools.java')


@check50.check(checkstyle_javadoc_methods)
def checkstyle_javadoc_all():
    """extra javadoc styling feedback"""
    stylefile = "styles/javadoc-all.xml"
    check50.include("styles")
    check50_checkstyle.run_and_interpret_checkstyle(
        checks_file=stylefile,
        rationale="{report}",
        target='StringTools.java')
