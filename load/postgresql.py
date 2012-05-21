#!/usr/bin/env python2
import psycopg2
import sys, os
from readfiles import readfiles

connection = psycopg2.connect('dbname=middlenames user=tlevine')
cursor = connection.cursor()

def store_in_db(rawline):
    'Save a particular line to the database.'
    ssn = rawline[1:10]
    try:
        cursor.execute('INSERT INTO person_raw (ssn,rawline) VALUES (%s, %s, FALSE)', (ssn, rawline))
    except psycopg2.IntegrityError:
        connection.rollback()
    else:
        connection.commit()

if __name__ == '__main__':
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        raise IOError('You must pass a directory containing the death files as the only argument.')
    readfiles(directory, store_in_db)
