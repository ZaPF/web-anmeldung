#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, redirect, template, static_file

@route('/static/<path:path>')
def callback(path):
    return static_file(path, root='./static')

@route('/')
@route("/<url:re:.+>")
def wartung(url=None):
    return template('warning', message_title=None, message="Die Anmeldung zur ZaPF 2013 wird gerade gewartet. Bitte versuchen Sie es in Kuerze noch einmal.")

run(host='0.0.0.0', port=8080, debug=True)
