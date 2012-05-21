import datetime

def process_date(datedict, datetype):
    '''
    Convert a date dictionary into date, day of week
    and day of year, handling missing values.
    '''

    # Convert to integers.
    for k, v in set(datedict.items()):
        if v == None:
            del(datedict[k])
        else:
            datedict[k] = int(v)

    # Handle incompleteness.
    keys = set(datedict.keys())
    if keys == {'year', 'month', 'day'}:
        date = datetime.datetime(datedict['year'], datedict['month'], datedict['day'])
        doy = datetime.datetime(2000, datedict['month'], datedict['day'])
        out = {
            datetype + '_date': date,
            datetype + '_dow': date.strftime('%a'),
            datetype + '_doy': doy,
        }
    elif keys == {'month', 'year'}:
        date = datetime.datetime(datedict['year'], datedict['month'], 15)
        out = {
            datetype + '_date': date, 
            datetype + '_dow': None,
            datetype + '_doy': None,
        }
    elif keys == {'month', 'day'}:
        date = datetime.datetime(2000, datedict['month'], datedict['day'])
        out = {
            datetype + '_date': None,
            datetype + '_dow': None,
            datetype + '_doy': date,
        }
    else:
        out = {
            datetype + '_date': None, 
            datetype + '_dow': None,
            datetype + '_doy': None,
        }

    if datedict['month'] != None:
        fakedate = datetime.date(2000, datedict['month'], 1)
        out[datetype + '_month'] = fakedate.strftime('%b')

    return out
