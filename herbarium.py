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
        connection.commit()


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
    return


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
    if command == 'e':
        userEnterNewPlant(cursor)
    elif command == 's':
        userSearchDatabase(cursor)
    elif command == 'd':
        userDeleteEntry(cursor)
    elif command == 'x':
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
    search_result = searchDatabase(name, cursor)
    print(search_result)
    return


def userSearchDatabase(cursor):
    """
    ask user to enter search word
    get result using searchDatabase
    no entry returns all
    print result
    :return:
    """
    search_term = input("What are you searching for?")
    if search_term == "":
        all_entries = cursor.fetchall()
        for eachRow in all_entries:
            print(eachRow)
    result = searchDatabase(search_term, cursor)
    print(result)
    return


def searchDatabase(search_term, cursor):
    """
    create query to select from database
    execute query
    :return: result
    """
    query = f" SELECT name, locality, date, id FROM project WHERE name='{search_term}'"
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
    delete_term = input("What do you want to delete?")
    result = searchDatabase(delete_term, cursor)
    print(result)
    if result is None:
        return
    confirmation = input("Do you wish to proceed? Y/N").lower()
    if confirmation == 'y':
        delete_query = f" DELETE FROM project WHERE id = '{result[-1]}'"
        cursor.execute(delete_query)

    return


def saveVariablesToDatabase(name, locality, date, cursor):
    """
    1. creating query
    2. execute query
    """

    query = f" INSERT INTO project(name, locality, date) VALUES ('{name}', '{locality}', '{date}') "
    cursor.execute(query)

    return 0


def userExitProgram(cursor):
    """
    close connection
    exits the program
    :return:
    """

    cursor.close()
    sys.exit()

main()

"""
herbarium database interactive window

1.set up screen
    - set up background in pink.
    - make it a nice lil box
    - display "welcome to the herbarium!" 

2. userinput
    -
    1. search
        - prompt user to type search word in box
        - store that info to a variable?
        - press search
            -equivalent to pressing 's'
        - access that info in database
        - print that info to display area
    2. enter
        - prompt user to enter 
            - name
            - locality
            - date
        store that info in database 
    3. delete
        -
6. display 

7. exit


"""



