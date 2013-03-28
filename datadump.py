#!/usr/bin/env python
# -*- coding: utf-8 -*-

import filedict
import json
from data import unis_dict

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

def registrants_by_university(items):
    rbu = dict()
    for item in items:
        key, item = item
        uni = item['university']
        if uni and uni != u'n-i-l' and uni != u'b-w':
            uni_code = item['university']
            uni_name = unis_dict[uni_code]
        elif item['university_alt']:
            uni_code = item['university_alt']
            uni_name = item['university_alt']
        elif item['university']:
            uni_code = u'-'
            uni_name = u'ohne Uni'
        try:
            rbu[uni_name]
        except:
            rbu[uni_name] = []
        rbu[uni_name].append(item)
    return rbu

def pp_rbu(rbu):
    pp_string = u"Anmeldungen pro Uni"
    for key in rbu.keys():
        print u"\nUni: {0}\n".format(key)
        for item in rbu[key]:
            print u"{0} {1}.".format(item['first_name'], item['last_name'][0])

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

    print pp_rbu(registrants_by_university(d.items()))
