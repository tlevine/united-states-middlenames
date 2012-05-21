#!/usr/bin/env python2
import zmq
import psycopg2

connection = psycopg2.connect('dbname=middlenames user=tlevine host=desk')
cursor = connection.cursor()

context = zmq.Context()
sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5557")

# Send out all of the lines.
cursor.execute('select rawline from person_raw where NOT parsed limit 100')
for record in cursor:
    sender.send(record[0])
