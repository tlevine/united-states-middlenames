#!/usr/bin/env python2
import pymongo

connection = pymongo.Connection('desk')
db = connection.middlenames

def store_in_db(rawline):
    'Save a particular line to the database.'
    ssn = rawline[1:10]
    db.person_raw.save({'_id': ssn, 'rawline': rawline, 'parsed': False})
