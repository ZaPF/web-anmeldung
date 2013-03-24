#!python

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

me_mail = u'vorstand@zapfev.de'
me_name = u'ZaPF'
confirmation_url_base = u'http://anmeldung.zapfev.de/confirm/%s'

def confirmation_mail(reg):

    text  = "Hallo %s %s,\n" % (reg['first_name'], reg['last_name'])
    text += "\n"
    text += "soeben hast du dich fuer die ZaPF angemeldet.\n"
    text += "\n"
    text += "Bitte bestaetige deine Anmeldung durch Aufrufen des folgenden Links:\n"
    text += "\n"
    text += "%s\n" % (confirmation_url_base % reg['id'])
    text += "\n"
    text += "Vielen Dank\n"
    text += "Dein Organisatoren-Team\n"
    text += "\n"
    text += "______________________________\n"
    text += "http://www.zapf.uni-jena.de\n"
    
    # Create a text/plain message
    msg = MIMEText(text)
    
    
    msg['Subject'] = 'Anmeldung zur ZaPF im SoSe 2013'
    msg['From'] = formataddr((str(Header(me_name, 'utf-8')), me_mail))
    msg['To'] = formataddr((str(Header(reg['first_name']+' '+reg['last_name'], 'utf-8')), reg['email']))
    
    server = smtplib.SMTP('fachschaft.physik.uni-frankfurt.de')
    server.set_debuglevel(1)

    print msg.as_string()
    print msg['From']
    print msg['To']

    server.sendmail(me_mail, [reg['email']], msg.as_string())
    server.quit()

if __name__ == "__main__":
    test_reg = Registrant()
    test_reg.vorname = 'Philipp'
    test_reg.nachname = 'Klaus'
    test_reg.email = 'philipp.klaus@gmail.com'
    confirmation_mail(test_reg)
