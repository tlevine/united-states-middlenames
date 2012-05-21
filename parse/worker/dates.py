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
        out = {
            datetype + '_date': date,
            datetype + '_dow': date.strftime('%a'),
            datetype + '_doy': date.strftime('%j'),
        }
    elif keys == {'month', 'year'}:
        date = datetime.datetime(datedict['year'], datedict['month'], 15)
        out = {
            datetype + '_date': date, 
        #   datetype + '_dow': None,
        #   datetype + '_doy': None,
        }
    elif keys == {'month', 'day'}:
        date = datetime.datetime(2000, datedict['month'], datedict['day'])
        out = {
            datetype + '_date': date,
        #   datetype + '_dow': None,
            datetype + '_doy': date.strftime('%j'),
        }
    else:
        out = {}

    return out

