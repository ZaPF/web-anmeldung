#!/usr/bin/env python

import filedict
import json

def pp(items):
    fields = ['id', 'first_name', 'last_name', 'confirmed', 'email', 'time']
    pp_string = "# " + ", ".join(fields) + "\n"
    for item in items:
        key, item = item
        try:
            entry = []
            for field in fields:
                entry.append("%s" % item[field])
            pp_string += ", ".join(entry) + '\n'
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
            print "missing field for entry with id " + key
            print "# " + json.dumps(item)
            del dic[key]


if __name__ == "__main__":
    d = filedict.FileDict(filename="data/anmeldungen.dict.sqlite")
    print "\n\n"
    print "# ID, Vorname, Nachname, Bestaetigt, E-Mail, Anmeldezeit"
    print pp(d.items())
    print "\n\n"
