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

locations = [
    000     unused   387-399 WI    528-529 UT
    001-003 NH       400-407 KY    530     NV
    004-007 ME       408-415 TN    531-539 WA
    008-009 VT       416-424 AL    540-544 OR
    010-034 MA       425-428 MS    545-573 CA
    035-039 RI       429-432 AR    574     AK
    040-049 CT       433-439 LA    575-576 HI
    050-134 NY       440-448 OK    577-579 DC
    135-158 NJ       449-467 TX    580     VI Virgin Islands
    159-211 PA       468-477 MN    581-584 PR Puerto Rico
    212-220 MD       478-485 IA    585     NM
    221-222 DE       486-500 MO    586     PI Pacific Islands*
    223-231 VA       501-502 ND    587-588 MS
    232-236 WV       503-504 SD    589-595 FL
    237-246 NC       505-508 NE    596-599 PR Puerto Rico
    247-251 SC       509-515 KS    600-601 AZ
    252-260 GA       516-517 MT    602-626 CA
    261-267 FL       518-519 ID    *Guam, American Samoa,
    268-302 OH       520     WY     Northern Mariana Islands,
    303-317 IN       521-524 CO     Philippine Islands
    318-361 IL       525     NM
    362-386 MI       526-527 AZ
]

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
