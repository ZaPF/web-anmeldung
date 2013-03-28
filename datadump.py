#!/usr/bin/env python
# -*- coding: utf-8 -*-

import filedict
import json

def pp(items):
    fields = ['id', 'ip', 'first_name', 'last_name', 'email', 'nick_name', 'confirmed', 'time', 'university', 'university_alt', 'exkursion1', 'exkursion2', 'exkursion3', 'tshirt', 'food', 'arbeitskreise', 'notes']
    pp_string = u"# " + u", ".join(fields) + u"\n"
    for item in items:
        key, item = item
        try:
            entries = []
            for field in fields:
                try:
                    entries.append(unicode(item[field]))
                except KeyError:
                    entries.append(u'')
            entries = [clean_csv_entry(entry) for entry in entries]
            pp_string += u", ".join(entries) + u'\n'
        except:
            raise
            #print "# Invalid entry with id " + key
            #print "# " + json.dumps(item)
    return pp_string

def clean_csv_entry(text):
    return text.replace(u',', u' ').replace(u'\n', u' ').replace(u'\r',' ')

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

    print pp(d.items())
