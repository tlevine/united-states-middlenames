#!/usr/bin/env python2
from parseline import parseline
import psycopg2

connection = psycopg2.connect('dbname=tlevine user=tlevine')
cursor = connection.cursor()

def schema():
    cursor.execute('''
CREATE TABLE IF NOT EXISTS person (
  ssn character(9),   -- Social security number
  raw character(100), -- Raw line of the file

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
--has_middle_initial boolean -- At least one middle initial
);''')

def load():
    'Go throug all of the files and import everything.'
    for filepart in range(1, 4):
        def o(prefix):
            return open('deathfile/ssdm%d' % filepart, 'r')

        try:
            f = o('/tmp/') # From the ramdisk
        except IOError:
            f = o('') #From the hard disk

        for line in f:
            loadline(line)

def loadline(line):
    'Save a particular line to the database.'
    if line[-1] == '\n':
        line = line[:-1]
    doc = parseline(line)
    print doc; 1/0
    db.deathfile.insert(doc)

if __name__ == '__main__':
    load()
