#!/usr/bin/env python2
'Connect to the MongoDB.'
def connect():
    from pymongo import Connection

    connection = Connection()
    db = connection.middlenames
    return db

db = connect()
del(connect)
