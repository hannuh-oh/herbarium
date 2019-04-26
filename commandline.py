import database

"""
This is my herbarium database!!
what does it do?
1. prompt user for command
2.
3. if command is search jump to 
"""

print('hello!')
# asks user for info, will later store it in database

def main():
   """
   1. connect to database
   2. reference cursor
   3. create table
   4. ask user for info
   5. display info
   6. loop to 4
   7. close connection
   :return:
   """


"""

1. wait to ask user for the name of plant
-store in variable 
2. wait to ask user for locality
-store in variable
3. wait to ask user for date
-store in variable
4. save all variables to database
5. return to one 

--search through database for plant name
1. sqlite query to find matching plant name 
-execute
2. if results length is greater than zero, jump to number 4
3. for all matches, display all of that info in the display box
-return to 1 or jump to five
4.  is 0, or no matches, print "nothing found"



"""

def askUserForInformation(database):
    while True:
        name = askUserForPlantName()
        locality = askUserForLocality()
        date = askUserForDate()
        saveVariablesToDatabase(name, locality, date, database)
    return 0

def askUserForPlantName():
    return input("What is the plant's name?")

def askUserForLocality():
    return input("Where did you find this plant?")

def askUserForDate():
    return input("What is the date?")

def saveVariablesToDatabase(name, locality, date, database):
    """
    1. creating query
    2. execute query
    """

    query = f" INSERT INTO project(name, locality, date) VALUES ('{name}', '{locality}', '{date}') "
    database.execute(query)

    return 0

