#!/usr/bin/env python3
import zmq

from ssn_locations import ssn_to_state
from dates import process_date
from initial import parseline

from mongo import savedoc

context = zmq.Context()
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://desk:5557")

def process(rawline):
    doc = {}
    doc.update(parseline(rawline))

    for datetype in ['born', 'died']:
        doc.update(process_date(doc[datetype], datetype))

    doc['state'] = ssn_to_state(doc['ssn'])
    doc['middles_count'] = len(doc['middles'])

    return doc

while True:
    rawline = str(receiver.recv(), 'utf-8')
    doc = process(rawline)
    savedoc(doc)
    print(doc)
