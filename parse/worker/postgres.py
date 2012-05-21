import psycopg2

connection = psycopg2.connect('dbname=middlenames user=tlevine host=desk')
cursor = connection.cursor()

def savedoc(doc):
    cursor.execute('''
INSERT INTO person VALUES (
  %(ssn)s,

  %(forename)s,
  %(surname)s,
  %(middles)s,

  %(born_year)s,
  %(died_year)s,
  %(born_month)s,
  %(died_month)s,
  %(born_day)s,
  %(died_day)s,

  %(born_date)s,
  %(died_date)s,

  %(born_dow)s,
  %(died_dow)s,

  %(born_doy)s,
  %(died_doy)s,

  %(state)s,
  %(middles_count)s
)''', doc)
    cursor.execute('UPDATE person_raw SET (parsed) = (TRUE)')
    connection.commit()

