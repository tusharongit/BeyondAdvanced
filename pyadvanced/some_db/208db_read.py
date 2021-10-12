import sqlite3 # open-source sql built into python

# make a connection to a db
conn = sqlite3.connect('my_db') # conect to this db or create a db if doesnt exist and then connect to it

# create a cursor to access members of the db
curs = conn.cursor() # curs is a db access object

# some SQL statements to read data

# we will have a zoo table containing animals with name, count, cost, exhibit
#stmt_read = "SELECT * FROM zoo"
stmt_read = '''
SELECT exhibit, animal, count, cost
FROM zoo
'''
#WHERE exhibit like '%jungle%'
#ORDER BY exhibit, count
#'''

# execute the statement
curs.execute(stmt_read)
rows = curs.fetchall()
print(rows) # a list of tuples
for anim in rows:
    print('There are {1} {0}s in the {2} exhibit.  It costs €{3:.2f} to maintain each {0}.'.format(anim[1], anim[2], anim[0], anim[3]))


# tidy up
conn.close()
