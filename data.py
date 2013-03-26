#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import attrgetter

class Uni(object):
    def __init__(self, name, city, acronym):
        self.name = name
        self.city = city
        self.acronym = acronym

unis = []

unis.append(Uni(u'RWTH Aachen', u'Aachen', 'AA'))
unis.append(Uni(u'Uni Frankfurt', u'Frankfurt', u'FFM'))
unis.append(Uni(u'Uni Jena', u'Jena', u'J'))
unis.append(Uni(u'TU Darmstadt', u'Darmstadt', u'DA'))
unis.append(Uni(u'LMU München', u'München', u'LMU'))
unis.append(Uni(u'TU München', u'München', u'TUM'))
unis.append(Uni(u'Karlsruher Institut für Technologie', u'Karlsruhe', u'KA'))
unis.append(Uni(u'Uni Wuppertal', u'Wuppertal', 'W'))
unis.append(Uni(u'TU Cottbus', u'Cottbus', 'CB'))
unis.append(Uni(u'Uni Oldenburg', u'Oldenburg', u'OL'))
unis.append(Uni(u'FU Berlin', u'Berlin', u'FUB'))
unis.append(Uni(u'Uni Göttingen', u'Göttingen', u'GOE'))
unis.append(Uni(u'Uni Kiel', u'Kiel', u'KI'))
unis.append(Uni(u'Uni Düsseldorf', u'Düsseldorf', u'D'))
unis.append(Uni(u'HU Berlin', u'Berlin', u'HUB'))
unis.append(Uni(u'Uni Halle', u'Halle', u'HAL'))
unis.append(Uni(u'TU Chemnitz', u'Chemnitz', u'C'))
unis.append(Uni(u'TU Dresden', u'Dresden', u'DD'))
unis.append(Uni(u'Uni Augsburg', u'Augsburg', u'A'))
unis.append(Uni(u'Uni Bielefeld', u'Bielefeld', u'BI'))
unis.append(Uni(u'Uni Heidelberg', u'Heidelberg', u'HD'))
unis.append(Uni(u'Uni Leipzig', u'Leipzig', u'L'))
unis.append(Uni(u'Uni Paderborn', u'Paderborn', u'PB'))
unis.append(Uni(u'Uni Potsdam', u'Potsdam', u'P'))
unis.append(Uni(u'Uni Stuttgart', u'Stuttgart', u'S'))
unis.append(Uni(u'Uni Würzburg', u'Würzburg', u'WUE'))
unis.append(Uni(u'Uni Bonn', u'Bonn', u'BN'))
unis.append(Uni(u'TU Dortmund', u'Dortmund', u'DO'))
unis.append(Uni(u'Uni Bremen', u'Bremen', u'HB'))
unis.append(Uni(u'Uni Hamburg', u'Hamburg', u'HH'))
unis.append(Uni(u'Uni Konstanz', u'Konstanz', u'KN'))
unis.append(Uni(u'Uni Münster', u'Münster', u'MS'))
unis.append(Uni(u'TU Kaiserslautern', u'Kaiserslautern', u'KL'))
unis.append(Uni(u'Uni Rostock', u'Rostock', u'HRO'))
unis.append(Uni(u'Uni Tübingen', u'Tübingen', u'TUE'))
unis.append(Uni(u'ETH Zürich', u'Zürich', u'ETH'))
unis.append(Uni(u'TU Wien', u'Wien', u'VIE'))
unis.append(Uni(u' - bitte wählen - ', u' / ', u'b-w'))
unis.append(Uni(u' - nicht in Liste oder nicht zutreffen - ', u' / ', u'n-i-l'))
#unis.append(Uni(u'', u'', u''))

# sort the unviversities by city)
unis = sorted(unis, key=attrgetter('city'))

# create a dictionary translating acronyms into university names:
unis_dict = dict()
for uni in unis:
    unis_dict[uni.acronym] = uni.name

