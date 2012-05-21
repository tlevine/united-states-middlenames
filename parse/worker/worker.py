#!/usr/bin/env python
import zmq
from pymongo import Connection

from ssn_locations import ssn_to_state
from dates import process_date

context = zmq.Context()
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://desk:5557")

connection = Connection('desk')
db = connection.middlenames

def process(deathfile_doc):
    watermelon_doc = {
        '_id': deathfile_doc['_id'],
    }

    for datetype in ['born', 'died']:
        watermelon_doc.update(process_date(deathfile_doc[datetype], datetype))

    watermelon_doc['state'] = ssn_to_state(deathfile_doc['ssn'])
    watermelon_doc['middles_count'] = len(deathfile_doc['middles'])

    return watermelon_doc

while True:
    # Get the document
    _id = str(receiver.recv(), 'utf-8')
    doc = db.deathfile.find_one({'_id': _id})

#   # Skip if we've already done this batch of processing.
#   watermelon = doc.get('watermelon', {})
#   if watermelon != {}:
#       continue # Already processed

#   # Otherwise, process it
#   command = {'watermelon': process(doc)}
#   db.deathfile.update({'_id': doc['_id']}, command)

    db.watermelon.save(process(doc))