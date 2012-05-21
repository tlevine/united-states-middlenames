#!/usr/bin/env python3
import zmq
import psycopg2

from ssn_locations import ssn_to_state
from dates import process_date
from parseline import parseline

context = zmq.Context()
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://desk:5557")

connection = psycopg2.connect('dbname=middlenames user=tlevine host=desk')
cursor = connection.cursor()

def process(rawline):
    doc = {}
    doc.update(parseline)

    for datetype in ['born', 'died']:
        doc.update(process_date(deathfile_doc[datetype], datetype))

    doc['state'] = ssn_to_state(deathfile_doc['ssn'])
    doc['middles_count'] = len(deathfile_doc['middles'])

    return doc

while True:
    rawline = str(receiver.recv(), 'utf-8')
    doc = process(rawline)
    cursor.execute('''
INSERT INTO person VALUES (
  %(ssn),

  %(forename),
  %(surname),
  %(middles),

  %(born_year),
  %(died_year),
  %(born_month),
  %(died_month),
  %(born_day),
  %(died_day),

  %(born_date),
  %(died_date),

  %(born_dow),
  %(died_dow),

  %(born_doy),
  %(died_doy),

  %(state),
  %(middles_count)
)''')
    cursor.commit()
