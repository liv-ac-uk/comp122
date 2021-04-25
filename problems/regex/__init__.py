import check50
import check50_java
import os

@check50.check()
def rebel_compiles():
    """Rebel.java compiles"""
    check50_java.compile("Rebel.java")

@check50.check(rebel_compiles)
def rebel_test_0():
    """Check Rebel.java is returning the correct output for the first regex"""
    
    check50_java.run("Rebel 0").stdout("29\s*34\s*Rebel\s*158\s*163\s*Rebel\s*", regex=True).exit()

@check50.check(rebel_compiles)
def rebel_test_1():
    """Check Rebel.java is returning the correct output for the second regex"""
    
    check50_java.run("Rebel 1").stdout("29\s*34\s*Rebel\s*131\s*137\s*Empire\s*158\s*163\s*Rebel\s*207\s*213\s*Empire\s*337\s*343\s*Empire\s*", regex=True).exit()

@check50.check(rebel_compiles)
def rebel_test_2():
    """Check Rebel.java is returning the correct output for the third regex"""
    
    check50_java.run("Rebel 2").stdout("29\s*34\s*Rebel\s*131\s*137\s*Empire\s*158\s*163\s*Rebel\s*207\s*213\s*Empire\s*337\s*343\s*Empire\s*363\s*376\s*Princess Leia\s*", regex=True).exit()

@check50.check(rebel_compiles)
def rebel_test_3():
    """Check Rebel.java is returning the correct output for the fourth regex"""
    
    check50_java.run("Rebel 3").stdout("29\s*34\s*Rebel\s*131\s*137\s*Empire\s*158\s*163\s*Rebel\s*207\s*213\s*Empire\s*237\s*242\s*DEATH\s*243\s*247\s*STAR\s*337\s*343\s*Empire\s*363\s*376\s*Princess Leia\s*", regex=True).exit()


@check50.check()
def spam_compiles():
    """Spam.java compiles"""
    check50_java.compile("Spam.java")


@check50.check(spam_compiles)
def spam_test_0():
    """Check Spam.java is returning the correct output for the first regex"""
    
    check50_java.run("Spam 0").stdout("From: makalele01@xzapmail.com\s*From: g_ineh@tiscali.co.uk\s*From: \"Michael Stevens Junior.\" <marksteven301@netscape.net>\s*From: \"Hajia Maryam Abacha\" <maraba234@anfmail.com>\s*From: \"Hajia Maryam Abacha\" <maraba234@latinmail.com>\s*From: \"BARRISTER MATHEW IKE\" <mathewike212@juno.com>\s*From: engedetamanah@post.cz\s*From: \"MR.ODIASE GEORGE\" <sunnyokogwo@post.cz>\s*From: \"DEACON ZIK R. DON\" <deacon_zik@yaoo.com>\s*From: \"Nzanga Mobutu\" <mobkuz3@kukamail.com>\s*From: adew1@mail3000.com\s*From: adew1@mail3000.com\s*From: \"DR.MUHAMMED MUSTAFA\" <muhammed303@arabtop.net>\s*From: \"BARRISTER, HOPKINS MBEKI\" <hopkinsmbeki@hknetmail.com>\s*From: ndandla@latinmail.com\s*From: <mcabacha@freesurf.fr>\s*From: shaabanbait@primposta.com\s*From: shaabanbait@primposta.com\s*From: consultant_ng3@send-mail.co.uk\s*From: mike odey <modey06@go.com>\s*From: \"DR. AKIN DADA.\" <akindada@indiatimes.com>\s*From: \"barrister vincent usman\" <2003vincent@freesurf.fr>\s*From: \"JAMIE  OPUKU.\" <jamie777@mail.biz.ly>\s*From: <jerrypeter2@freesurf.fr>\s*From: \"mona noah\" <mnoah3@hotmail.com>\s*From: \"MICHEAL  OSSAI\" <JUDE@YAHOO.COM>\s*From: test@yahoo.com\s*From: test@yahoo.com\s*From: \"Peter Bongo\" <mrbongo@themail.com>\s*From: MASTER HAROLD MBEKI <akumembeki@netscape.net>\s*From: \"maryaabacha8 maryam \" <mmaryaabacha8@caramail.com>\s*From: Mrs Maryam Abacha\s*From: \"maryaabacha8 maryam \" <mmaryaabacha8@caramail.com>\s*From: Mrs Maryam Abacha\s*From: \"H B\" <hansob@123.com>\s*From: diaka tshombe <dtshombe2@123.com>\s*From: EKONG BASSEY <ekong.bassey2@caramail.com>\s*From: Vasil Nanchev <vas_imoti@abv.bg>\s*From: frank okonjo <frankokonjo5@123.com>\s*From: \"DR. GODWIN KALALA\" <gokalala1@tiscali.co.uk>\s*From: EKONG BASSEY <ekong.bassey2@caramail.com>\s*From: HELLEN SHAKA ZUMA <hellenshaka@netscape.net>\s*From: Akande fredrick <fredsam@123.com>\s*From: esama kingdom <esamakingdom@fsmail.net>\s*", regex=True).exit()

@check50.check(spam_compiles)
def spam_test_1():
    """Check Spam.java is returning the correct output for the second regex"""
    
    check50_java.run("Spam 1").stdout("29\s*34\s*Spam\s*131\s*137\s*Empire\s*158\s*163\s*Spam\s*207\s*213\s*Empire\s*337\s*343\s*Empire\s*", regex=True).exit()

@check50.check(spam_compiles)
def spam_test_2():
    """Check Spam.java is returning the correct output for the third regex"""
    
    check50_java.run("Spam 2").stdout("29\s*34\s*Spam\s*131\s*137\s*Empire\s*158\s*163\s*Spam\s*207\s*213\s*Empire\s*337\s*343\s*Empire\s*363\s*376\s*Princess Leia\s*", regex=True).exit()

@check50.check(spam_compiles)
def spam_test_3():
    """Check Spam.java is returning the correct output for the fourth regex"""
    
    check50_java.run("Spam 3").stdout("29\s*34\s*Spam\s*131\s*137\s*Empire\s*158\s*163\s*Spam\s*207\s*213\s*Empire\s*237\s*242\s*DEATH\s*243\s*247\s*STAR\s*337\s*343\s*Empire\s*363\s*376\s*Princess Leia\s*", regex=True).exit()






