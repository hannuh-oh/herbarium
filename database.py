#my herbarium database!
#database stuff ONLY


#creates database and connects file to it
import sqlite3
conn = sqlite3.connect('Herbarium.sqlite3')
c = conn.cursor()


def nameVal():
    name = input("what name?")
    return name


def localVal():
    locality = input("where did you find it?")
    return locality


def dateVal():
    date = input("when did you find it?")
    return date



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
q =  f" INSERT INTO project(name, locality, date) VALUES ('{nameVal()}', '{localVal()}', '{dateVal()}') "
c.execute(q)
q = ''' SELECT * FROM project '''
c.execute(q)

results = c.fetchall()
for eachrow in results:
    print(eachrow)

#closes the connection
c.close()



if __name__ == '__main__':
    main()
else:
    print( "Hey I am in database.py and __name__ is ", __name__)



