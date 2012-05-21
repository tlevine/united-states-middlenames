#!/usr/bin/env python2
import psycopg2
import sys, os

connection = psycopg2.connect('dbname=middlenames user=tlevine')
cursor = connection.cursor()

def store_in_db(rawline):
    'Save a particular line to the database.'
    ssn = rawline[1:10]
    try:
        cursor.execute('INSERT INTO person_raw (ssn,rawline,parsed) VALUES (%s, %s, FALSE)', (ssn, rawline))
    except psycopg2.IntegrityError:
        connection.rollback()
    else:
        connection.commit()
