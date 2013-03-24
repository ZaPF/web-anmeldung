#!/usr/bin/env python

print "Don't run this file by itself."
print "Copy and paste the snippets from here and run them..."
import sys; sys.exit(1)

import filedict
d = filedict.FileDict(filename="data/anmeldungen.dict.sqlite")

# Delete a certain name:
for item in d.items():
    key, item = item
    try:
        if item['first_name'] == 'Philipp' and item['last_name'] == 'Klaus':
            del d[key]
    except:
        continue

# Reset confirmations
for item in d.items():
    key, item = item
    try:
        item['confirmed'] = None
    except:
        continue
    d[key] = item

