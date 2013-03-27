Dies ist die Anmelde-Website für die ZaPF.

Sie ist z.Zt. unter <http://anmeldung.zapfev.de> live.

### Technische Voraussetzungen zum Betrieb

Diese Anwendung ist in Python (Version 2.6 & 2.7) geschrieben und nutzt das Web-Framework [bottle][].
Zudem nutzt sie weitere freie Software, nämlich [Twitter Bootstrap][], [jQuery][] und [filedict][].  
Zunächst muss man also Python installieren, was bei Debian und Ubuntu meist schon dabei ist, sonst aber über `sudo apt-get install python python-pip` nachgeholt werden kann.  
Bottle wird nicht hier im Projekt mitgeliefert, sondern wird am besten per `pip` installiert: `pip install bottle`. Alternativ wird einfach die Datei `bottle.py` heruntergeladen und hier in den Projektordner gespeichert.

Zudem ist in der Datei mailer.py der Mailserver eingetragen, über den Bestätigungs-Mails verschickt werden, ein solcher ist zum Betrieb natürlich auch nötig.

### Betrieb

Betrieben wird die Anmelde-Seite, indem man die Datei `app.py` startet:

    ./app.py

[bottle]: http://bottlepy.org
[Twitter Bootstrap]: http://twitter.github.com/bootstrap
[jQuery]: http://jquery.com/
[filedict]: https://github.com/erezsh/filedict
