#!/usr/bin/env python2
from pymongo import Connection
import zmq

connection = psycopg2.connect('dbname=tlevine user=tlevine')
cursor = connection.cursor()

context = zmq.Context()
sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5557")

# Send out all of the lines.
cursor.execute('select rawline from person_raw limit 100')
for record in cursor:
    sender.send(record[0]))
