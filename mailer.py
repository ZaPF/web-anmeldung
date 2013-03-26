#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

from data import unis_dict

me_mail = u'vorstand@zapfev.de'
me_name = u'ZaPF'
confirmation_url_base = u'http://anmeldung.zapfev.de/confirm/%s'

def confirmation_mail(reg):
    text  = u"Hallo {0} {1},\n".format(reg['first_name'], reg['last_name'])
    text += u"\n"
    text += u"soeben hast du dich für die ZaPF angemeldet.\n"
    text += u"\n"
    text += u"Bitte bestätige deine Anmeldung durch Aufrufen des folgenden Links:\n"
    text += u"\n"
    text += u"%s\n" % (confirmation_url_base % reg['id'])
    text += u"\n"
    text += u"Du hast die folgenden Angaben bei der Anmeldung gemacht:\n"
    text += u"\n"
    text += u"Vorname: {0}\n".format(reg['first_name'])
    text += u"Nachname: {0}\n".format(reg['last_name'])
    text += u"E-Mail: {0}\n".format(reg['email'])
    text += u"Universität: {0}\n".format(unis_dict[reg['university']])
    text += u"Universität (alternativ): {0}\n".format(reg['university_alt'])
    text += u"T-Shirt Größe: {0}\n".format(reg['tshirt'].upper())
    text += u"Exkursion: {0}\n".format(reg['exkursion'])
    text += u"Ernährung: {0}\n".format(reg['food'])
    text += u"AK-Wünsche: {0}\n".format(reg['arbeitskreise'])
    text += u"Sonstiges:\n"
    text += u"{0}\n".format(reg['notes'] if reg['notes'] else " / ")
    text += u"\n"
    text += u"Vielen Dank\n"
    text += u"Dein Organisatoren-Team\n"
    text += u"\n"
    text += u"______________________________\n"
    text += u"http://www.zapf.uni-jena.de\n"
    
    # Create a text/plain message
    msg = MIMEText(text.encode('UTF-8'), 'plain', 'UTF-8')
    
    
    msg['Subject'] = 'Anmeldung zur ZaPF im SoSe 2013'
    msg['From'] = formataddr((str(Header(me_name, 'utf-8')), me_mail))
    msg['To'] = formataddr((str(Header(reg['first_name']+' '+reg['last_name'], 'utf-8')), reg['email']))
    
    server = smtplib.SMTP('fachschaft.physik.uni-frankfurt.de')
    server.set_debuglevel(1)

    server.sendmail(me_mail, [reg['email']], msg.as_string())
    server.quit()

if __name__ == "__main__":
    test_reg = Registrant()
    test_reg.vorname = 'Philipp'
    test_reg.nachname = 'Klaus'
    test_reg.email = 'philipp.klaus@gmail.com'
    confirmation_mail(test_reg)
