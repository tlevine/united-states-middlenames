import pymongo

connection = psycopg2.Connection('desk')
db = connection.middlenames

def savedoc(doc):
    doc['_id'] = doc['ssn']
    db.person.save(doc)
    db.person_raw.update(doc['_id'], {'$set': {'parsed': True})
