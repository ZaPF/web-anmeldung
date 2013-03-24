#!/usr/bin/env python

from bottle import route, run, static_file, post, get, request, template, TEMPLATE_PATH, response
from mailer import confirmation_mail
import filedict
import json
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
        return template('warning', message_title="Fehler", message="Deine Anmeldung ist uns nicht bekannt. Bitte kontaktiere uns, wenn du dir sicher bist, dass der Bestaetigungs-Link funktionieren sollte.")
    if reg['confirmed']:
        return template('info', message_title="Anmeldungs-Bestaetigung", alert="In Ordnung", message="Die Anmeldung wurde bereits zuvor bestaetigt.")
    else:
        reg['confirmed'] = unixtime()
        d[id] = reg
        return template('info', message_title="Anmeldungs-Bestaetigung", alert="In Ordnung", message="Die Anmeldung wurde erfolgreich bestaetigt.")

@route('/static/<path:path>')
def callback(path):
    return static_file(path, root='./static')

@post('/')
def login_submit():
    reg = dict() # we store the registrant's details in a dictionary
    reg['time'] = unixtime()
    reg['ip'] = request.remote_route[0]
    reg['first_name'] = request.forms.get('first_name')
    reg['last_name'] = request.forms.get('last_name')
    reg['email'] = request.forms.get('email_addr')
    reg['university'] = request.forms.get('university')
    reg['university_alt'] = request.forms.get('university_alt')
    reg['food'] = request.forms.get('food')
    reg['arbeitskreise'] = request.forms.get('arbeitskreise')
    reg['notes'] = request.forms.get('notes')
    if check_registrant(reg):
        reg['id'] = create_id()
        reg['confirmed'] = False
        d[reg['id']] = reg
        confirmation_mail(reg)
        return template('info', message_title="Anmeldungs-Bestaetigung", alert="In Ordnung", message="Registrierung abgeschlossen. Bitte E-Mails checken!")
    else:
        return template('warning', message_title="Fehler", message="Ein Fehler ist aufgetreten.")

@get('/liste/json')
def dump_json():
    response.headers['Content-Type'] = 'text/plain'
    return json.dumps(list(d.items()), sort_keys=True, indent=2)

@get('/liste/csv')
def dump_csv():
    response.headers['Content-Type'] = 'text/plain'
    return pp(d.items())

run(host='0.0.0.0', port=8080, debug=True, reloader=True)
