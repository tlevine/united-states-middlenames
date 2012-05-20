import datetime

def process_date(datedict, datetype):
    '''
    Convert a date dictionary into date, day of week
    and day of year, handling missing values.
    '''

    keys = set(datedict.keys())
    if keys == {'year', 'month', 'day'}:
        out = {
            datetype + '.date'] = datetime.date(date['year'], date['month'], date['day'])
            datetype + '.dow'] = out[datetype + '.date'].strftime('%a')
        #   datetype + '.doy'] = None
        }
    elif keys == {'month', 'year'}:
        out = {
            datetype + '.date'] = datetime.date(date['year'], date['month'], 15)
        #   datetype + '.dow'] = None
            datetype + '.doy'] = out[datetype + '.date'].strftime('%j')
        }
    elif keys == {'month', 'day'}:
        out = {
            datetype + '.date': datetime.date(2000, date['month'], date['day']),
        #   datetype + '.dow': None,
            datetype + '.doy': out[datetype + '.date'].strftime('%j'),
        }
    else:
        out = {}

    return out

