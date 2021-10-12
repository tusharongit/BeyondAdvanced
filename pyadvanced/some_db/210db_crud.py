# Create Read Update Delete CRUD
import sqlite3 # open-source sql built into python
from sqlite3.dbapi2 import IntegrityError # to check for primary key violation

def makeConn():
    # make a connection to a db
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    return (conn, curs)

def cleanConn(conn):
    conn.close()

def update():
    conn, curs = makeConn()
    # some SQL statements to update data
    stmt_update = '''
    UPDATE zoo
    SET count = 9
    WHERE animal = 'meerkat'
    '''
    try:
        # execute the statement
        curs.execute(stmt_update)
        # commit
        conn.commit()
    except IntegrityError as err:
        print('[EXCEPTION] {}'.format(err))
    except Exception as err:
        print('[EXCEPTION] {}'.format(err))
    finally:
    # tidy up
        cleanConn(conn)    

if __name__ == '__main__':
    update()
