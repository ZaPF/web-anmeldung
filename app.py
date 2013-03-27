#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, static_file, post, get, request, template, response, redirect, error, PasteServer
from mailer import confirmation_mail
import filedict
import json
import time
import string
from random import choice
from datadump import pp
from data import unis, exkursionen, essen, tshirts, exkursionen_dict, essen_dict, tshirts_dict, unis_dict
import re

d = filedict.FileDict(filename="data/anmeldungen.dict.sqlite")

a_p_i = filedict.FileDict(filename="data/anmeldungen-pro-ip.dict.sqlite")

def check_registrant(reg):
    #return validate_email(reg['email'])
    return True

def create_id(size=8):
    return ''.join([choice(string.letters + string.digits) for i in range(size)])

def unixtime():
    return int(time.time())

@get('/')
def signup():
    return template('home')

@get('/anmelden')
def signup():
    return template('anmelden', unis=unis, exkursionen=exkursionen, essen=essen, tshirts=tshirts, error=None)

class ValidationError(NameError):
    pass

@post('/anmelden')
def login_submit():
    reg = dict() # we store the registrant's details in a dictionary
    error = None
    # parse and validate user input
    reg['notes'] = u""
    reg['tshirts'] = u""
    reg['food'] = u""
    reg['exkursion1'], reg['exkursion2'], reg['exkursion3'] = (u"", u"", u"")
    reg['arbeitskreise'] = u""
    reg['university_alt'] = u""
    reg['university'] = u""
    reg['nick_name'] = u""
    reg['email'] = u""
    reg['last_name'] = u""
    reg['first_name'] = u""
    try:
        reg['notes'] = request.forms.get('notes').decode('utf-8').strip()
    except:
        error = ValidationError(u'Fehler mit dem Feld Sonstige Wünsche.')
    try:
        reg['tshirt'] = request.forms.get('tshirt').decode('utf-8').strip()
        tshirts_dict[reg['tshirt']]
    except:
        error = ValidationError("Bitte T-Shirt korrekt angeben.")
    try:
        reg['food'] = request.forms.get('food').decode('ascii').strip()
    except:
        error = ValidationError(u'Bitte eine Wahl für das Essen treffen.')
    try:
        reg['exkursion3'] = request.forms.get('exkursion3').decode('utf-8').strip()
        reg['exkursion2'] = request.forms.get('exkursion2').decode('utf-8').strip()
        reg['exkursion1'] = request.forms.get('exkursion1').decode('utf-8').strip()
        exkursionen_dict[reg['exkursion1']] and exkursionen_dict[reg['exkursion2']] and exkursionen_dict[reg['exkursion3']]
    except:
        error = ValidationError(u"Exkursionen nicht ordentlich angegeben.")
    try:
        reg['arbeitskreise'] = request.forms.get('arbeitskreise').decode('utf-8').strip()
    except:
        raise ValidationError(u'Arbeitskreise nicht ordentlich angegeben.')
    try:
        reg['university_alt'] = request.forms.get('university_alt').decode('utf-8').strip()
    except:
        raise ValidationError(u'Alternative Universität nicht ordentlich angegeben.')
    try:
        reg['university'] = request.forms.get('university').decode('utf-8').strip()
    except:
        raise ValidationError(u'Universität nicht ordentlich angegeben.')
    if not (reg['university'] == u'n-i-l' or reg['university'] == u'b-w') and reg['university_alt']:
        error = ValidationError(u'Bitte entweder Universität aus Liste auswählen oder sie selbst in das Textfeld eingeben') 
    try:
        reg['nick_name'] = request.forms.get('nick_name').decode('utf-8').strip()
    except:
        raise ValidationError(u'Feld Nickname fehlt.')
    try:
        reg['email'] = request.forms.get('email_addr').decode('utf-8').strip()
        if re.match(u"^[a-zA-Z0-9\.\_%\-\+]+@[a-zA-Z0-9._%-]+\.[a-zA-Z]{2,6}$", reg['email']) == None:
            raise
    except:
        error = ValidationError(u"Bitte gültige E-Mail Adresse angeben.")
    try:
        reg['last_name'] = request.forms.get('last_name').decode('utf-8').strip().title()
        if reg['last_name'] == u'': raise
    except:
        raise ValidationError(u'Bitte Nachnamen angeben')
    try:
        reg['first_name'] = request.forms.get('first_name').decode('utf-8').strip().title()
        if reg['first_name'] == u'': raise
    except:
        error = ValidationError(u'Bitte Vornamen angeben')
    try:
        a_p_i[request.remote_route[0]]
    except:
        a_p_i[request.remote_route[0]] = 0
    a_p_i[request.remote_route[0]] += 1
    if a_p_i[request.remote_route[0]] > 2:
        error = ValidationError(u"Nicht mehr als 15 Anmeldungen pro IP Adresse erlaubt!")
    if error:
        return template('anmelden', unis=unis, exkursionen=exkursionen, essen=essen, tshirts=tshirts, registrant=reg, error=error.message)
    # set up less critical parameters
    reg['id'] = create_id()
    reg['time'] = unixtime()
    reg['ip'] = request.remote_route[0]
    reg['confirmed'] = False
    # store the registrant in the SQlite based dictionary
    try:
        confirmation_mail(reg)
    except:
        return template('anmelden', unis=unis, exkursionen=exkursionen, essen=essen, tshirts=tshirts, registrant=reg, error=u"Konnte Bestätigungs-E-Mail nicht versenden. Stimmt deine E-Mail Adresse?")
    d[reg['id']] = reg
    redirect('/anmeldung/erfolgreich')

@get('/anmeldung/erfolgreich')
def success():
    return template('info', message_title="Anmeldungs-Bestätigung", alert="Anmeldung erfolgt.", message="Jetzt bitte E-Mails checken und die Anmeldung bestätigen!")

@get('/anmeldung/unbekannt')
def unknown_id():
    return template('warning', message_title="Fehler", message="Deine Anmeldung ist uns nicht bekannt. Bitte kontaktiere uns, wenn du dir sicher bist, dass der Bestätigungs-Link funktionieren sollte.")

@get('/confirm/<id:re:[a-zA-Z0-9]+>')
def confirm(id):
    time.sleep(2.)
    try:
        reg = d[id]
    except:
        redirect('/anmeldung/unbekannt')
    if reg['confirmed']:
        return template('info', message_title="Anmeldungs-Bestätigung", alert="Alles in Ordnung", message="Die Anmeldung wurde bereits zuvor bestätigt.")
    else:
        reg['confirmed'] = unixtime()
        d[id] = reg
        return template('info', message_title="Anmeldungs-Bestätigung", alert="Danke.", message="Deine Anmeldung wurde erfolgreich bestätigt.")

@route('/static/<path:path>')
def callback(path):
    return static_file(path, root='./static')


@get('/liste/json')
def dump_json():
    response.headers['Content-Type'] = 'text/plain; charset=UTF8'
    return json.dumps(list(d.items()), sort_keys=True, indent=2)

@get('/liste/csv')
def dump_csv():
    response.headers['Content-Type'] = 'text/plain; charset=UTF8'
    return pp(d.items())

@error(404)
def error404(error):
    return template('warning', message_title="Fehler 404", message="Die aufgerufene Seite existiert nicht.")

#run(host='0.0.0.0', port=8080, debug=True, reloader=True)
run(host='0.0.0.0', port=8080)
#run(host='0.0.0.0', server=PasteServer, port=8080)

