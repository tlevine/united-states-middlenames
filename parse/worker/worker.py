#!/usr/bin/env python
import zmq

from ssn_locations import ssn_to_state
from dates import process_date
from parseline import parseline

context = zmq.Context()
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://desk:5557")

connection = psycopg2.connect('dbname=tlevine user=tlevine')
cursor = connection.cursor()

def schema():
    cursor.execute('''
CREATE TABLE IF NOT EXISTS person (
  ssn character(9),   -- Social security number

  forename varchar(55),
  surname varchar(55),
  middles varchar(55),

  -- Date components
  born_year smallint,
  died_year smallint,
  born_month smallint,
  died_month smallint,
  born_day smallint,
  died_day smallint,

  -- The above date as a proper date
  born_date date,
  died_date date,

  -- Day of the week (0, 1, 2, 3, 4, 5 or 6)
  born_dow smallint,
  died_dow smallint,

  -- Date in the year 2000, in case the year is not known
  born_doy date,
  died_doy date,

  state character(2), -- Geographical state of registration
  middles_initials_count smallint, -- How many middle initials

  UNIQUE(ssn)
);''')

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
    
