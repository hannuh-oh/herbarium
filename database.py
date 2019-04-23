import sqlite3

conn = sqlite3.connect('Herbarium.sqlite3')
c = conn.cursor()
#creates database and connects file to it

nameVal = input("what is the name of this plant?")
localityVal = input("where did you find this plant?")
dateVal = input("when did you find it? EX (YYYY-MM-DD)")


c.execute('''
 CREATE TABLE IF NOT EXISTS project(
 id integer PRIMARY KEY,
 name text NOT NULL,
 locality text,
 date text 
 );
''')
#creates a table called project


q =  f" INSERT INTO project(name, locality, date) VALUES ('{nameVal}', '{localityVal}', '{dateVal}') "
c.execute(q)
#puts information into project

q = ''' SELECT * FROM project '''
c.execute(q)
#selects all info

results = c.fetchall()
for eachrow in results:
    print(eachrow)
#prints all info in data

c.close()

