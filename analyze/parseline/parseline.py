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
    # First, check that it looks like a valid line.
    is_line_valid(line)

    # Then parse it.
    doc = {}
    doc['ssn'] = line[1:10]
    doc['born'] = _parsedate(line[73:81])
    doc['died'] = _parsedate(line[65:73])

    names = filter(None, line[10:65].split(' '))
    doc['surname'] = names[0]
    doc['forename'] = names[1]
    doc['middles'] = names[2:]
    return doc

SSN = re.compile(r'^[0-9]+$')
NAMES = re.compile(r'^[A-Z ]+$')
DATETIMES = re.compile(r'^[0-9]+$')
LINELENGTH = 100

def is_line_valid(line):
    # White space
    padding0 = line[0]
    padding1 = line[81:]
    ssn = line[1:10]
    names = line[10:65]
    datetimes = line[65:81]

    if padding0 != ' ':
        raise ValueError('The first character is "%s" instead of a space.' % padding0)

    if set(padding1) != set(' '):
        raise ValueError('The right side margin/padding is wrong.')

    if not re.match(SSN, ssn):
        raise ValueError('"%s" doesn\'t look like a social security number.' % ssn)
        
    if not re.match(NAMES, names):
        raise ValueError('Something\'s wrong with the name.')

    if not re.match(DATETIMES, datetimes):
        raise ValueError('Something\'s wrong with the datetimes.')

    if not len(line) == LINELENGTH:
        raise ValueError('The line is %d characters long instead of %d' % (len(line), LINELENGTH))
