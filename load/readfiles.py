#!/usr/bin/env python2
import sys, os

def readfiles(directory, loadfunc):
    'Go throug all of the files and import everything.'
    for filepart in range(1, 4):
        f = open(os.path.join(directory, 'ssdm%d' % filepart), 'r')
        for line in f:
            loadfunc(line[:-1]) # The last character is a \n

directory = sys.argv[1]
db = sys.argv[2]

if not os.path.isdir(directory):
    raise IOError('You must pass a directory containing the death files as the only argument.')

if db == 'postgres':
    from postgresql import store_in_db as store_postgres
    store_in_db = store_postgres
elif db == 'mongo':
    from mongodb import store_in_db as store_mongo
    store_in_db = store_mongo
else:
    raise ValueError('The second argument, database, must be "postgres" or "mongo".')

readfiles(directory, store_in_db)
