#!/usr/bin/env python

from bottle import route, run, static_file, post, get, request, template, TEMPLATE_PATH, response
from mailer import confirmation_mail
import filedict
import time
import string
from random import choice
from datadump import pp

d = filedict.FileDict(filename="data/anmeldungen.dict.sqlite")
TEMPLATE_PATH.insert(0,'./templates/')

def check_registrant(reg):
    #return validate_email(reg['email'])
    return True

def create_id(size=8):
    return ''.join([choice(string.letters + string.digits) for i in range(size)])

def unixtime():
    return int(time.time())

@get('/')
def signup():
    return template('anmeldung')

@get('/confirm/<id:re:[a-zA-Z0-9]+>')
def confirm(id):
    try:
        reg = d[id]
    except:
        return "<p>Diese Registrierung ist uns nicht bekannt.</p>"
    if reg['confirmed']:
        return "<p>Die Anmeldung wurde bereits zuvor bestaetigt.</p>"
    else:
        reg['confirmed'] = unixtime()
        d[id] = reg
        return "<p>Die Anmeldung wurde bestaetigt.</p>"

@route('/static/<path:path>')
def callback(path):
    return static_file(path, root='./static')

@post('/')
def login_submit():
    reg = dict() # we store the registrant's details in a dictionary
    reg['time'] = unixtime()
    reg['first_name'] = request.forms.get('first_name')
    reg['last_name'] = request.forms.get('last_name')
    reg['email'] = request.forms.get('email_addr')
    if check_registrant(reg):
        reg['id'] = create_id()
        reg['confirmed'] = False
        d[reg['id']] = reg
        confirmation_mail(reg)
        return "<p>Registrierung abgeschlossen. Bitte E-Mails checken!</p>"
    else:
        return "<p>Es ist ein Fehler aufgetreten.</p>"

@get('/liste/csv')
def dump_csv():
    pp_string = pp(d.items())
    response.headers['Content-Type'] = 'text/plain'
    return pp_string

run(host='0.0.0.0', port=8080, debug=True, reloader=True)
