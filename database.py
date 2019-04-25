#my herbarium database!


#creates database and connects file to it
import sqlite3
conn = sqlite3.connect('Herbarium.sqlite3')
c = conn.cursor()


#asks user for info, will later store it in database
nameVal = input("what name?")
localVal = input("where did you find it?")
dateVal = input("when did you find it?")


#creates a table called project
c.execute('''
 CREATE TABLE IF NOT EXISTS project(
 id integer PRIMARY KEY,
 name text NOT NULL,
 locality text,
 date text 
 );
''')


#puts information into project
q =  f" INSERT INTO project(name, locality, date) VALUES ('{nameVal}', '{localVal}', '{dateVal}') "
c.execute(q)
q = ''' SELECT * FROM project '''
c.execute(q)


#prints all info in data
results = c.fetchall()
for eachrow in results:
    print(eachrow)


#closes the connection
c.close()

