import sqlite3

conn = sqlite3.connect('Herbarium.sqlite3')
c = conn.cursor()
#creates database and connects file to it

val = input("what name?")
print(val)

c.execute('''
 CREATE TABLE IF NOT EXISTS project(
 id integer PRIMARY KEY,
 name text NOT NULL,
 locality text,
 date text 
 );
''')
#creates a table called project

q = ''' INSERT INTO project(name, locality, date) VALUES ("flowers", "wwc", "2018-04-15") '''
q = ''' SELECT * FROM project '''
#puts information into project

c.execute(q)
c.fetchall()
#gets info from table

c.close()

