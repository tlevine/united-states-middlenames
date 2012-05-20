#!/usr/bin/env python2
from pymongo import Connection
import zmq

connection = Connection()
db = connection.middlenames

context = zmq.Context()
sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5557")

# Send out all of the document _ids
for doc in db.deathfile.find():
    sender.send(doc['_id'])
