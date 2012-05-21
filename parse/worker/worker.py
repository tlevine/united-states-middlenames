#!/usr/bin/env python3
import zmq
import psycopg2

from ssn_locations import ssn_to_state
from dates import process_date
from initial import parseline

context = zmq.Context()
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://desk:5557")

connection = psycopg2.connect('dbname=middlenames user=tlevine host=desk')
cursor = connection.cursor()

def process(rawline):
    doc = {}
    doc.update(parseline(rawline))

    for datetype in ['born', 'died']:
        doc.update(process_date(doc[datetype], datetype))

    doc['state'] = ssn_to_state(doc['ssn'])
    doc['middles_count'] = len(doc['middles'])

    return doc

while True:
    print('Receiveng')
    rawline = str(receiver.recv(), 'utf-8')
    print('Processing')
    doc = process(rawline)

    print('Saving')
    cursor.execute('''
INSERT INTO person VALUES (
  %(ssn)s,

  %(forename)s,
  %(surname)s,
  %(middles)s,

  %(born_year)s,
  %(died_year)s,
  %(born_month)s,
  %(died_month)s,
  %(born_day)s,
  %(died_day)s,

  %(born_date)s,
  %(died_date)s,

  %(born_dow)s,
  %(died_dow)s,

  %(born_doy)s,
  %(died_doy)s,

  %(state)s,
  %(middles_count)s
)''', doc)
    cursor.execute('UPDATE person_raw SET (parsed) = (TRUE)')
    connection.commit()
