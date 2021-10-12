import sqlite3 # open-source sql built into python
from sqlite3.dbapi2 import IntegrityError # to check for primary key violation

# make a connection to a db
conn = sqlite3.connect('my_db') # conect to this db or create a db if doesnt exist and then connect to it

# create a cursor to access members of the db
curs = conn.cursor() # curs is a db access object

# some SQL statements to create tables, populate data, etc.

# we will have a zoo table containing animals with name, count, cost, exhibit
stmt1 = '''
INSERT INTO zoo
VALUES
( "meerkat",
  20,
  7.25,
  "open insert"
)
'''

try:
    # execute the statement
    curs.execute(stmt1)
    # commit
    conn.commit()
except IntegrityError as err:
    print('[EXCEPTION] {}'.format(err))
except Exception as err:
    print('[EXCEPTION] {}'.format(err))
finally:
    # tidy up
    conn.close()
