#!/usr/bin/env python2
from pymongo import Connection
from parseline import parseline

connection = Connection()
db = connection.middlenames

def load():
    'Go throug all of the files and import everything.'
    for filepart in range(1, 4):
        f = open('deathfile/ssdm%d' % filepart, 'r')
        for line in f:
            loadline(line)

def loadline(line):
    'Save a particular line to the database.'
    if line[-1] == '\n':
        line = line[:-1]
    doc = parseline(line)
    doc['_id'] = doc['ssn']
    db.deathfile.insert(doc)

if __name__ == '__main__':
    load()
