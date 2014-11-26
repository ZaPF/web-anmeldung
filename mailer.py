#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from email.charset import add_charset, QP

from data import unis_dict, exkursionen_dict, essen_dict, tshirts_dict

ME_EMAIL = 'vorstand@zapfev.de'
ME_NAME = 'ZaPF Anmeldung'
ME_REPLY_TO = 'fsr@paf.uni-jena.de'
CONFIRMATION_URL_BASE = 'http://anmeldung.zapfev.de/confirm/%s'

def confirmation_mail(reg):
    fields = dict()
    fields.update(reg)
    fields['confirmation_url'] = CONFIRMATION_URL_BASE % reg['id']
    fields['nick_name'] = reg['nick_name'] or '-'
    fields['university_alt'] = reg['university_alt'] or '-'
    fields['food'] = essen_dict[reg['food']]
    fields['arbeitskreise'] = reg['arbeitskreise'] or '-'
    fields['notes'] = reg['notes'] or ' -\n'
    text = open('MAIL_TEXT.tpl').read().format(**fields)
    
    # Create a text/plain message
    add_charset('utf-8', QP, QP, 'utf-8')
    msg = MIMEText(text, _charset='utf-8')
    
    msg['Subject'] = 'Anmeldung zur ZaPF im SoSe 2013'
    msg['From'] = formataddr((str(Header(ME_NAME, 'utf-8')), ME_EMAIL))
    msg['To'] = formataddr((str(Header(reg['first_name']+' '+reg['last_name'], 'utf-8')), reg['email']))
    msg.add_header('Reply-To', ME_REPLY_TO)
    
    server = smtplib.SMTP('fachschaft.physik.uni-frankfurt.de')
    server.set_debuglevel(1)

    server.sendmail(ME_EMAIL, [reg['email']], msg.as_string())
    server.quit()

if __name__ == "__main__":
    test_reg = dict()
    test_reg['id'] = 'pElBQ6XK'
    test_reg['first_name'] = 'Max'
    test_reg['last_name'] = 'Mustermann'
    test_reg['email'] = 'max@example.com'
    test_reg['nick_name'] = ''
    test_reg['university'] = 'MIT Cambridge, MA'
    test_reg['university_alt'] = ''
    test_reg['tshirt'] = 'M-m'
    test_reg['exkursion1'] = 'imaginata'
    test_reg['exkursion2'] = 'optisches-museum'
    test_reg['exkursion3'] = 'fraunhoferinstitut'
    test_reg['food'] = 'fleisch'
    test_reg['arbeitskreise'] = 'AK Sauna, AK Brotzeit'
    test_reg['notes'] = ''
    confirmation_mail(test_reg)
