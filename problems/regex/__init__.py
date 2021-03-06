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
    check50.include("Spam.txt")  # copy over Spam.txt for later checks


@check50.check(spam_compiles)
def spam_test_0():
    """Check Spam.java is returning the correct output for the first regex"""

    check50_java.run("Spam 0").stdout("From: makalele01@xzapmail.com\s*From: g_ineh@tiscali.co.uk\s*From: \"Michael Stevens Junior.\" <marksteven301@netscape.net>\s*From: \"Hajia Maryam Abacha\" <maraba234@anfmail.com>\s*From: \"Hajia Maryam Abacha\" <maraba234@latinmail.com>\s*From: \"BARRISTER MATHEW IKE\" <mathewike212@juno.com>\s*From: engedetamanah@post.cz\s*From: \"MR.ODIASE GEORGE\" <sunnyokogwo@post.cz>\s*From: \"DEACON ZIK R. DON\" <deacon_zik@yaoo.com>\s*From: \"Nzanga Mobutu\" <mobkuz3@kukamail.com>\s*From: adew1@mail3000.com\s*From: adew1@mail3000.com\s*From: \"DR.MUHAMMED MUSTAFA\" <muhammed303@arabtop.net>\s*From: \"BARRISTER, HOPKINS MBEKI\" <hopkinsmbeki@hknetmail.com>\s*From: ndandla@latinmail.com\s*From: <mcabacha@freesurf.fr>\s*From: shaabanbait@primposta.com\s*From: shaabanbait@primposta.com\s*From: consultant_ng3@send-mail.co.uk\s*From: mike odey <modey06@go.com>\s*From: \"DR. AKIN DADA.\" <akindada@indiatimes.com>\s*From: \"barrister vincent usman\" <2003vincent@freesurf.fr>\s*From: \"JAMIE  OPUKU.\" <jamie777@mail.biz.ly>\s*From: <jerrypeter2@freesurf.fr>\s*From: \"mona noah\" <mnoah3@hotmail.com>\s*From: \"MICHEAL  OSSAI\" <JUDE@YAHOO.COM>\s*From: test@yahoo.com\s*From: test@yahoo.com\s*From: \"Peter Bongo\" <mrbongo@themail.com>\s*From: MASTER HAROLD MBEKI <akumembeki@netscape.net>\s*From: \"maryaabacha8 maryam \" <mmaryaabacha8@caramail.com>\s*From: Mrs Maryam Abacha\s*From: \"maryaabacha8 maryam \" <mmaryaabacha8@caramail.com>\s*From: Mrs Maryam Abacha\s*From: \"H B\" <hansob@123.com>\s*From: diaka tshombe <dtshombe2@123.com>\s*From: EKONG BASSEY <ekong.bassey2@caramail.com>\s*From: Vasil Nanchev <vas_imoti@abv.bg>\s*From: frank okonjo <frankokonjo5@123.com>\s*From: \"DR. GODWIN KALALA\" <gokalala1@tiscali.co.uk>\s*From: EKONG BASSEY <ekong.bassey2@caramail.com>\s*From: HELLEN SHAKA ZUMA <hellenshaka@netscape.net>\s*From: Akande fredrick <fredsam@123.com>\s*From: esama kingdom <esamakingdom@fsmail.net>\s*", regex=True).exit()

@check50.check(spam_compiles)
def spam_test_1():
    """Check Spam.java is returning the correct output for the second regex"""

    check50_java.run("Spam 1").stdout("makalele01@xzapmail.com\s*2200384715453906@xzapmail.com\s*makalele01@xzapmail.com\s*makalele1@excite.com\s*tamb_h@latinmail.com\s*200308080119.h781JMR02653@heartbreakridge.mr.itd.UM\s*tambo_40@latinmail.com\s*tamb_h@latinmail.com\s*erickerick39@latinmail.com\s*g_ineh@tiscali.co.uk\s*webmaster@cs.CU\s*g_ineh@tiscali.co.uk\s*g_ineh@tiscali.co.uk\s*marksteven301@netscape.net\s*webmaster@cs.CU\s*200308110050.h7B0oDCB028583@cs.CU\s*marksteven301@netscape.net\s*webmaster@aclweb.org\s*markstevens301@netscape.net\s*maraba234@anfmail.com\s*webmaster@cs.CU\s*200308110903.h7B93FIo016324@bluewhale.cs.CU\s*maraba234@anfmail.com\s*hajiamaryam@libero.it\s*webmaster@aclweb.org\s*maraba234@latinmail.com\s*webmaster@cs.CU\s*200308111125.h7BBP3Io016913@bluewhale.cs.CU\s*maraba234@latinmail.com\s*maraba234@voila.fr\s*webmaster@aclweb.org\s*mathewike212@juno.com\s*200308111207.h7BC7hF23066@foxfire.mr.itd.UM\s*mathewike212@juno.com\s*mathewikeh_123@juno.com\s*engedetamanah@post.cz\s*engedetamanah@post.cz\s*engedetamanah@post.cz\s*engedetamanah@post.cz\s*engedetamanah@post.cz\s*engedetamanah@post.cz\s*2194236c1295fc9cdeefd6e63937a19e@www1.mail.post.cz\s*sunnyokogwo@post.cz\s*webmaster@cs.CU\s*200308120513.h7C5D5Io021250@bluewhale.cs.CU\s*sunnyokogwo@post.cz\s*odaisegeorge@themail.com\s*deacon_zik@yaoo.com\s*200308122220.h7CMKEl19448@fistfulofdollars.mr.itd.UM\s*deacon_zik@yaoo.com\s*zik_don@yahoo.com\s*mobkuz3@kukamail.com\s*200308122233.h7CMXoW15703@magnumforce.mr.itd.UM\s*mobkuz3@kukamail.com\s*mobkuz3@kukamail.co\s*adew1@mail3000.com\s*1060268429.3f32698de2fc2@www.mail3000.com\s*adew1@mail3000.com\s*adew1@mail3000.com\s*awilliams44@k.ro\s*awilliams44@k.ro\s*adew1@mail3000.com\s*1060268429.3f32698de2fc2@www.mail3000.com\s*adew1@mail3000.com\s*adew1@mail3000.com\s*awilliams44@k.ro\s*awilliams44@k.ro\s*muhammed303@arabtop.net\s*200308131021.h7DALWW14387@deadpool.mr.itd.UM\s*muhammed303@arabtop.net\s*muhammed303@arabtop.net\s*hopkinsmbeki@hknetmail.com\s*webmaster@cs.CU\s*200308141903.h7EJ3hCB010860@cs.CU\s*hopkinsmbeki@hknetmail.com\s*hopkinsmbek1@hknetmail.com\s*webmaster@aclweb.org\s*hacco_man@yahoo.com\s*20030816002455.94208.qmail@web80709.mail.yahoo.com\s*madu_emerem@mail.com\s*ndandla@latinmail.com\s*200308162129.h7GLTas21742@foxfire.mr.itd.UM\s*ndandla@latinmail.com\s*ndandla@latinmail.com\s*mcabacha@freesurf.fr\s*1387.192.116.71.164.1061472238.squirrel@jose.freesurf.fr\s*mcabacha@freesurf.fr\s*mcabacha@freesurf.fr\s*gregado@rxpost.net\s*mcabacha@gawab.com\s*shaabanbait@primposta.com\s*200308221643.h7MGek80019689@services.cacn.net\s*shaabanbait@primposta.com\s*shaabanbait@primposta.com\s*shaabanbait@primposta.com\s*GLENEAGLESJFXOuMARC00001ff0@gleneagles.sauk.co.uk\s*1113.216.139.180.2.1061603043.squirrel@mail.send\s*ifeanyi_uzo@yahoo.com\s*smith@sino.net\s*modey06@go.com\s*modey06@go.com\s*modey06@go.com\s*drmikeodey@rediffmail.com\s*n@hknetmail.com\s*koso@hknetmail.com\s*austin_dunger1@yahoo.com\s*20030825142910.2230.qmail@web20502.mail.yahoo.com\s*akindada@indiatimes.com\s*webmaster@cs.CU\s*200308252019.h7PKJh8I007648@cs.CU\s*akindada@indiatimes.com\s*akin511@hotmail.com\s*webmaster@aclweb.org\s*2003vincent@freesurf.fr\s*4506.81.199.84.89.1061853286.squirrel@arlette.freesurf.fr\s*2003vincent@freesurf.fr\s*2003vincent@freesurf.fr\s*2003vincent@tiscali.co.uk\s*jamie777@mail.biz.ly\s*webmaster@cs.CU\s*200308260953.h7Q9rhiw023337@bluewhale.cs.CU\s*jamie777@mail.biz.ly\s*jamie777@guessmail.com\s*webmaster@aclweb.org\s*jerrypeter2@freesurf.fr\s*1405.195.166.238.114.1061984830.squirrel@arlette.freesurf.fr\s*jerrypeter2@freesurf.fr\s*jerrypeter2@freesurf.fr\s*mnoah3@hotmail.com\s*mnoah3@hotmail.com\s*mnoah3@hotmail.com\s*mnoah12@hotmail.com\s*F1606HHGNZ4mF100009ad4@hotmail.com\s*mnoah12@hotmail.com\s*JUDE@YAHOO.COM\s*200308271346.h7RDjvfu028501@smtp.eecs.UM\s*JUDE@YAHOO.COM\s*michealossai@mailsurf.com\s*test@yahoo.com\s*webmaster@cs.CU\s*200308271356.h7RDuQix001485@bluewhale.cs.CU\s*test@yahoo.com\s*webmaster@aclweb.org\s*test@yahoo.com\s*kokormobutu@yahoo.co.uk\s*test@yahoo.com\s*test@yahoo.com\s*test@yahoo.com\s*20030827135813.7376FC1C5@krusty.si.UM\s*kokormobutu@yahoo.co.uk\s*mrbongo@themail.com\s*webmaster@cs.CU\s*200308291752.h7THqOcn008750@cs.CU\s*mrbongo@themail.com\s*mrbongo247@themail.com\s*webmaster@aclweb.org\s*akumembeki@netscape.net\s*akumembeki@netscape.net\s*haroldmbeki@netscape.net\s*20030901125714.A0A46E3A0@krusty.si.UM\s*haroldmbeki@netscape.net\s*haroldmbeki@netscape.net\s*haroldmbeki@netscape.net\s*haroldmbeki@netscape.net\s*mmaryaabacha8@caramail.com\s*mmaryaabacha8@caramail.com\s*mmaryaabacha8@caramail.com\s*mmaryaabacha8@caramail.com\s*admin@mailman.isi.edu\s*200309031427.h83ERcp28572@tnt.isi.edu\s*hansob@123.com\s*search@ISI.EDU\s*admin@mailman.isi.edu\s*admin@mailman.isi.edu\s*search@mailman.isi.edu\s*request@mailman.isi.edu\s*hansob@netzero.com\s*hansob@netzero.com\s*hansob@netzero.com\s*dtshombe2@123.com\s*0HKN00J11FI065@ismtp4.priv2.mail.entelchile.net\s*bag@citi.UM\s*dtshombe2@123.com\s*dtshombe2@123.com\s*tshombed2@thepostmaster.net\s*dae400dae871.dae871dae400@123mail.cl\s*ekong.bassey2@caramail.com\s*webmaster@cs.CU\s*200309041217.h84CHSH9021614@bluewhale.cs.CU\s*ekong.bassey2@caramail.com\s*webmaster@aclweb.org\s*ekobass2002@netscape.net\s*anonymous@newsbucks.com\s*vas_imoti@abv.bg\s*frankokonjo5@123.com\s*0HKP00B96AR6H5@ismtp7.priv2.mail.entelchile.net\s*frankokonjo5@123.com\s*frankokonjo5@123.com\s*fokonjo2@yahoo.com\s*e5b7d1e5e6c7.e5e6c7e5b7d1@123mail.cl\s*gokalala1@tiscali.co.uk\s*webmaster@cs.CU\s*200309042137.h84LZ5H9023267@bluewhale.cs.CU\s*gokalala1@tiscali.co.uk\s*gokalala5@tiscali.co.uk\s*webmaster@aclweb.org\s*ekong.bassey2@caramail.com\s*webmaster@cs.CU\s*200309042223.h84MNqH9023383@bluewhale.cs.CU\s*ekong.bassey2@caramail.com\s*webmaster@aclweb.org\s*ekobass2002@netscape.net\s*200309041817.OAA12138@list.msu.edu\s*hellenshaka@netscape.net\s*PROSODY@list.msu.edu\s*hellenshaka@netscape.net\s*PROSODY@list.msu.edu\s*hellenshakashaka@netscape.net\s*fredsam@123.com\s*0HKP00JJEW5SRL@ismtp8.priv2.mail.entelchile.net\s*fredsam@123.com\s*ed1b73ed1f4c.ed1f4ced1b73@123mail.cl\s*esamakingdom@fsmail.net\s*esamakingdom@fsmail.net\s*esamakingdom@fsmail.net\s*revcistercium@planafla.es\s*", regex=True).exit()

@check50.check(spam_compiles)
def spam_test_2():
    """Check Spam.java is returning the correct output for the third regex"""

    check50_java.run("Spam 2").stdout("marksteven301@netscape.net\s*maraba234@anfmail.com\s*maraba234@latinmail.com\s*mathewike212@juno.com\s*sunnyokogwo@post.cz\s*deacon_zik@yaoo.com\s*mobkuz3@kukamail.com\s*muhammed303@arabtop.net\s*hopkinsmbeki@hknetmail.com\s*mcabacha@freesurf.fr\s*modey06@go.com\s*akindada@indiatimes.com\s*2003vincent@freesurf.fr\s*jamie777@mail.biz.ly\s*jerrypeter2@freesurf.fr\s*mnoah3@hotmail.com\s*JUDE@YAHOO.COM\s*mrbongo@themail.com\s*akumembeki@netscape.net\s*mmaryaabacha8@caramail.com\s*mmaryaabacha8@caramail.com\s*hansob@123.com\s*dtshombe2@123.com\s*ekong.bassey2@caramail.com\s*vas_imoti@abv.bg\s*frankokonjo5@123.com\s*gokalala1@tiscali.co.uk\s*ekong.bassey2@caramail.com\s*hellenshaka@netscape.net\s*fredsam@123.com\s*esamakingdom@fsmail.net\s*", regex=True).exit()

