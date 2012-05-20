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
NAMES = re.compile(r'''^[A-Z0-9 '-.,]+$''')
DATETIMES = re.compile(r'^[0-9]+$')
LINELENGTH = 100

SPACES = set(' ')

def _parsedate(datestring):
    'Parse a date in the format that the death file uses.'
    result = {'year': None, 'month': None, 'day': None}
    components = {k: int(datestring.__getslice__(*DATE_COMPONENTS[k])) for k in DATE_COMPONENTS.keys()}

    try:
        # All is well.
        date = datetime.date(components['year'], components['month'], components['day'])
        result = {'year': date.year, 'month': date.month, 'day': date.day}
    except ValueError:
        if components.values() == [0, 0, 0]:
            # All components missing
            pass

        elif components['year'] and (not components['month']) and (not components['day']):
            # Only year available
            if components['year'] > 1800:
                result['year'] = components['year']

        elif (not components['year']) and components['month'] and components['day']:
            # Only year missing
            try:
                datetime.date(1900, components['month'], components['day'])
            except ValueError:
                pass
            else:
                result.update({'month': components['month'], 'day': components['day']})

        elif components['year'] and components['month'] and (not components['day']):
            # Only day missing
            try:
                datetime.date(components['year'], components['month'], 1)
            except ValueError:
                raise
            else:
                result.update({'year': components['year'], 'month': components['month']})

        else:
            msg = 'This date string is too weird: {year:04}-{month:02}-{day:02}'.format(**components)
            raise ValueError(msg)

    return result

def parseline(line):
    'Parse a line of the death file.'
    doc = {}

    # First, check that it looks like a valid line.
    doc['errors'] = is_line_valid(line)

    # Then parse it.
    doc['ssn'] = line[1:10]

    for key, indices in [('bord', (73, 81)), ('died', (65, 73))]:
        try:
            doc[key] = _parsedate(line.__getslice__(indices))
        except ValueError, msg:
            doc['parse_errors'].append(msg) 
            print msg
            print line

    names = filter(None, line[10:65].split(' '))
    if names[0][-1] == ',':
        doc['suffix'] = names.pop(1) # Remove the suffix
        names[0] = names[0][:-1] # Remove the comma.

    doc['surname'] = names[0]
    doc['forename'] = names[1]
    doc['middles'] = names[2:]
    return doc

def check_line(line):
    # White space
    padding0 = line[0]
    padding1 = line[81:]
    ssn = line[1:10]
    names = line[10:65]
    datetimes = line[65:81]

    errors = []
    if padding0 != ' ':
        errors.append('The first character is "%s" instead of a space.' % padding0)

    if set(padding1) != SPACES:
        errors.append('The right side margin/padding is wrong for SSN %s.' % ssn)

    if not re.match(SSN, ssn):
        errors.append('"%s" doesn\'t look like a social security number.' % ssn)
        
    if not re.match(NAMES, names):
        errors.append('Something\'s wrong with this name: %s.' % names)

    if not re.match(DATETIMES, datetimes):
        errors.append('Something\'s wrong with the datetimes.')

    if not len(line) == LINELENGTH:
        errors.append('The line is %d characters long instead of %d' % (len(line), LINELENGTH))

    return errors
