#!/usr/bin/env python2
import pymongo
import zmq

connection = pymongo.Connection('desk')
db = connection.middlenames

context = zmq.Context()
sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5557")

# Send out all of the lines.
records = db.person_raw.find({'parsed': False}) #, limit = 100)
for record in records:
    sender.send(str(record['rawline']))
