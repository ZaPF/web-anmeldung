#!/usr/bin/env python
# -*- coding: utf-8 -*-

import filedict
import json

def pp(items):
    fields = ['id', 'first_name', 'last_name', 'confirmed', 'email', 'time']
    pp_string = u"# " + u", ".join(fields) + u"\n"
    for item in items:
        key, item = item
        try:
            entry = []
            for field in fields:
                entry.append(unicode(item[field]))
            pp_string += u", ".join(entry) + u'\n'
        except:
            raise
            #print "# Invalid entry with id " + key
            #print "# " + json.dumps(item)
    return pp_string


def clean(dic):
    for item in dic.items():
        key, item = item
        try:
            item['id']
            item['first_name']
            item['last_name']
            item['confirmed']
            item['email']
        except:
            print u"missing field for entry with id " + key
            print u"# " + json.dumps(item)
            del dic[key]


if __name__ == "__main__":
    d = filedict.FileDict(filename="data/anmeldungen.dict.sqlite")
    print u"\n\n"
    print u"# ID, Vorname, Nachname, Bestaetigt, E-Mail, Anmeldezeit"
    print pp(d.items())
    print u"\n\n"

    for item in d.items():
        print json.dumps(item, sort_keys=True, indent=4)
