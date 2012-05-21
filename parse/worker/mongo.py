import pymongo

connection = pymongo.Connection('desk')
db = connection.middlenames

def savedoc(doc):
    doc['_id'] = doc['ssn']
    db.person.save(doc)
    db.person_raw.update({'_id': doc['_id']}, {'$set': {'parsed': True}})
