'Import the death file into a MongoDB.'
from unittest import TestCase
import datetime
import re


DATE_COMPONENTS =  {
    'year': [4, 8],
    'month': [0, 2],
    'day': [2, 4],
}

SSN = re.compile(r'^[0-9]+$')
NAMES = re.compile(r'^[A-Z ]+$')
DATETIMES = re.compile(r'^[0-9]+$')
LINELENGTH = 100

SPACES = set(' ')
ZEROES = set('0')

def _parsedate(datestring):
    'Parse a date in the format that the death file uses.'
    try:
        # All is well.
        date = datetime.datetime.strptime(datestring, '%m%d%Y').date()
        result = {'year': date.year, 'month': date.month, 'day': date.day}
    except ValueError:
        result = {'year': None, 'month': None, 'day': None}
        d = {k: int(datestring.__getslice__(*DATE_COMPONENTS[k])) for k in DATE_COMPONENTS.keys()}
        zeroes = {k: set(v) == ZEROES for k, v in d}

        if zeroes.values() == [True]*3:
            # All components missing
            pass

        elif (not zeroes['year']) and zeroes['month'] and not zeroes['day']:
            # Only year available
            if d['year'] > 1800:
                result['year'] = d['year']

        elif zeroes['year'] and (not zeroes['month']) and (not zeroes['day']):
            # Only year missing
            try:
                datetime.date(1900, d['month'], d['day']):
            except ValueError:
                pass
            else:
                result.update({'month': d['month', 'day': d['day']})

        else:
            print datestring
            raise ValueError('This date string is too weird.')

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

def is_line_valid(line):
    # White space
    padding0 = line[0]
    padding1 = line[81:]
    ssn = line[1:10]
    names = line[10:65]
    datetimes = line[65:81]

    if padding0 != ' ':
        raise ValueError('The first character is "%s" instead of a space.' % padding0)

    if set(padding1) != SPACES:
        raise ValueError('The right side margin/padding is wrong.')

    if not re.match(SSN, ssn):
        raise ValueError('"%s" doesn\'t look like a social security number.' % ssn)
        
    if not re.match(NAMES, names):
        raise ValueError('Something\'s wrong with the name.')

    if not re.match(DATETIMES, datetimes):
        raise ValueError('Something\'s wrong with the datetimes.')

    if not len(line) == LINELENGTH:
        raise ValueError('The line is %d characters long instead of %d' % (len(line), LINELENGTH))
