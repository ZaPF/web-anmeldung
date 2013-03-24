#!/usr/bin/env python

from bottle import route, run, redirect, template, TEMPLATE_PATH, static_file
TEMPLATE_PATH.insert(0,'./templates/')

@route('/static/<path:path>')
def callback(path):
    return static_file(path, root='./static')

@route('/')
@route("/<url:re:.+>")
def wartung(url=None):
    return template('warning', message_title=None, message="Die Anmeldung zur ZaPF 2013 wird gerade gewartet. Bitte versuchen Sie es in Kuerze noch einmal.")

run(host='0.0.0.0', port=8080, debug=True)
