'Import the death file into a MongoDB.'
from unittest import TestCase
import datetime
import re

def _parsedate(datestring):
    'Parse a date in the format that the death file uses.'
    if datestring[2:4] == '00':
        # We don't know the day.
        date = datetime.date(*map(int, [datestring[4:9], datestring[0:2], '1']))
        result = {'year': date.year, 'month': date.month, 'day': None}

    else:
        # All is well.
        date = datetime.datetime.strptime(datestring, '%m%d%Y').date()
        result = {'year': date.year, 'month': date.month, 'day': date.day}

    return result

def parseline(line):
    doc = {}
    doc['ssn'] = line[1:10]
    doc['born'] = _parsedate(line[73:81])
    doc['died'] = _parsedate(line[65:73])

    names = filter(None, line[10:65].split(' '))
    doc['surname'] = names[0]
    doc['forename'] = names[1]
    doc['middles'] = names[2:]
    return doc

class TestLine(TestCase):
    line = ' 001010001MUZZEY                  GRACE                          1200197504161902                   '

    def test_padding(self):
        padding0 = self.line[0]
        self.assertEqual(padding0, ' ')

    def test_ssn(self):
        'Is the SSN column what we expect?'
        ssn = self.line[1:10]
        self.assertRegexpMatches(ssn, r'[0-9]+')

    def test_name(self):
        name = self.line[10:65]
        self.assertRegexpMatches(name, r'[A-Z ]+')

    def test_dates(self):
        deathdatetime = self.line[65:81]
        self.assertRegexpMatches(deathdatetime, r'[0-9]+')
