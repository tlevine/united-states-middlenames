import datetime

def process_date(datedict, datetype):
    '''
    Convert a date dictionary into date, day of week
    and day of year, handling missing values.
    '''

    keys = set(datedict.keys())
    if keys == {'year', 'month', 'day'}:
        date = datetime.date(datedict['year'], datedict['month'], datedict['day'])
        out = {
            datetype + '.date': date,
            datetype + '.dow': date.strftime('%a'),
            datetype + '.doy': date.strftime('%j'),
        }
    elif keys == {'month', 'year'}:
        date = datetime.date(datedict['year'], datedict['month'], 15)
        out = {
            datetype + '.date': date, 
        #   datetype + '.dow': None,
        #   datetype + '.doy': None,
        }
    elif keys == {'month', 'day'}:
        date = datetime.date(2000, datedict['month'], datedict['day'])
        out = {
            datetype + '.date': date,
        #   datetype + '.dow': None,
            datetype + '.doy': date.strftime('%j'),
        }
    else:
        out = {}

    print out
    return out

