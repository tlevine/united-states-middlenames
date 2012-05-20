# Task worker
# Connects PULL socket to tcp://localhost:5557
# Collects workloads from ventilator via that socket
# Connects PUSH socket to tcp://localhost:5558
# Sends results to sink via that socket
#
# Author: Lev Givon <lev(at)columbia(dot)edu>

import zmq
import json

import datetime

context = zmq.Context()
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5557")

def process(deathfile_doc):
    watermelon_doc = {
        '_id': deathfile_doc['_id'],
        'born.date': 
    }

#   ssn,       born.date, died.date, born.dow, died.dow, born.doy,   died.doy,   state, forename, surname, middles, middles.count
    
    for datetype in ['born', 'died']:
        watermelon_doc.update(process_date(deathfile_doc[datetype], datetype))

def process_date(datedict, datetype)
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

while True:
    # Get the document
    _id = receiver.recv()
    doc = db.deathfile.find_one({'_id': _id})

    # Skip if we've already done this batch of processing.
    processed = doc.get('processed', [])
    if 'watermelon' in processed:
        continue # Already processed

    # Otherwise, process it
    watermelon = process(doc)
    db.watermelon.save(chainsaw)

    # And say that it's been processed
    db.deathfile.update({'ssn': doc['ssn']}, {'$push': {'processed': 'watermelon'})