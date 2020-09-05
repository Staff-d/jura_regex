#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys

# Für Erläuterung der Regex siehe README.md
p = re.compile(r""" # Die Regex wird in p kompiliert
(§+|Art|Artikel)\.?\s*
(?P<norm>\d+(?:\w\b)?)\s*
(?:Abs\.\s*(?P<absatz>\d+(?:\w\b)?))?\s*
(?:S\.\s*(?P<satz>\d+))?\s*
(?:Nr\.\s*(?P<nr>\d+(?:\w\b)?))?\s*
(?:lit\.\s*(?P<lit>[a-z]?))?
.{0,10}?
(?P<gesetz>\b[A-Z][A-Za-z]*[A-Z](?:(?P<buch>(?:\s|\b)[XIV]+)?))
""", re.VERBOSE)

if sys.argv[1] == '--':
    Teststring = sys.stdin.read()
else:
    Teststring = ''
    for arg in sys.argv[1:]:
        with open(arg, 'r') as h:
            Teststring += h.read()

alle_treffer = list(p.finditer(Teststring.replace('\n', ' ')))

liste_der_treffer = '\n'.join(map(lambda t: t.group(),alle_treffer))
liste_der_gesetze = set(list(map(lambda t: t.group('gesetz'),alle_treffer)))

print(liste_der_treffer)
# print(f"Folgende Treffer gibt es:\n{liste_der_treffer}")
# print(f"Im Einzelnen konnten die folgenden Gesetze erkannt werden:")
#
# for x in liste_der_gesetze:
#     print(x.strip() + ' ')
