import sqlite3
import sys

def main():
    """
    connect to database
    reference cursor
    create table
    prompt user for command
    loop back to prompt
    :return:
    """

    connection = sqlite3.connect('Herbarium.sqlite3')
    cursor = connection.cursor()
    createTable(cursor, connection)
    while True:
        promptUserForCommand(cursor)

def createTable(cursor, connection):
    """
    creates table in sqlite3
    takes in name, locality, date
    :return:
    """

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS project(
    id integer PRIMARY KEY,
    name text NOT NULL,
    locality text,
    date text 
    );
    ''')

    connection.commit()

def promptUserForCommand(cursor):
    """
    asking for user to select search, enter, delete, or exit
    if enter call userEnterNewPlant
    if search call userSearchDatabase
    if delete call userDeleteProgram
    if exit call userExitProgram
    :return:
    """
    command = input("Press 'E' to enter 'S' to search 'D' to delete 'X' to exit").lower()
    if(command == 'e'):
        userEnterNewPlant(cursor)
    elif(command == 's'):
        userSearchDatabase(cursor)
    elif(command == 'd'):
        userDeleteEntry(cursor)
    elif(command == 'x'):
        userExitProgram(cursor)
    return

def userEnterNewPlant(cursor):
    """
    ask user for name
    ask user for locality
    ask user for date
    assign variables to table in database
    call searchDatabase to display information
    :return:
    """
    name = input("What is the plant's name?")
    locality = input("Where did you find this plant?")
    date = input("What is the date?")
    saveVariablesToDatabase(name, locality, date, cursor)
    searchResult = searchDatabase(name, cursor)
    print(searchResult)
    return 


def userSearchDatabase(cursor):
    """
    ask user to enter search word
    get result using searchDatabase
    print result
    :return:
    """
    searchTerm = input("What are you searching for?")
    result = searchDatabase(searchTerm, cursor)
    print(result)
    return

def searchDatabase(searchTerm, cursor):
    """
    create query to select from database
    execute query
    :return: result
    """
    query = f" SELECT '{searchTerm}' FROM project"
    cursor.execute(query)
    result = cursor.fetchone()
    return result


def userDeleteEntry(cursor):
    """
    ask user for name
    call searchDatabase using name
    get result
    confirm?
    delete result

    :return:
    """
    deleteTerm = input("What do you want to delete?")
    result = searchDatabase(deleteTerm, cursor)
    print(result)
    confirmation = input("Do you wish to proceed? Y/N").lower()
    if confirmation == 'y':
        deleteQuery = f" DELETE FROM project WHERE ID = '{result}'"
        cursor.execute(deleteQuery)

    return


def userExitProgram(cursor):
    """
    close connection
    exits the program
    :return:
    """

    cursor.close()
    sys.exit()


def saveVariablesToDatabase(name, locality, date, cursor):
    """
    1. creating query
    2. execute query
    """

    query = f" INSERT INTO project(name, locality, date) VALUES ('{name}', '{locality}', '{date}') "
    cursor.execute(query)

    return 0

main()

