from tkinter import *
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
    command = input("Press 'E' to enter 'S' to search 'D' to delete 'X' to exit 'W' for window").lower()
    if command == 'e':
        userEnterNewPlant(cursor)
    elif command == 's':
        userSearchDatabase(cursor)
    elif command == 'd':
        userDeleteEntry(cursor)
    elif command == 'x':
        userExitProgram(cursor)
    elif command == 'w':
        userDisplayWindow(cursor)
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
        result = returnAllEntries(cursor)
        for each_entry in result:
            print(each_entry)
    else:
        result = searchDatabase(search_term, cursor)
        print(result)
    return


def searchDatabase(search_term, cursor):
    """
    create query to select from database
    execute query
    :return: result
    """
    query = f"SELECT name, locality, date, id FROM project WHERE name='{search_term}'"
    cursor.execute(query)
    result = cursor.fetchone()
    return result

def returnAllEntries(cursor):
    """
    query to search everything in database
    execute query
    returns all entries
    :param cursor:
    :return:
    """
    query = "SELECT * FROM project"
    cursor.execute(query)
    result = cursor.fetchall()
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

def userDisplayWindow(cursor):
    """
    call set up screen
    call user interface elements
    call display screen
    """
    screen = setUpScreen()
    configureInterfaceElements(screen, cursor)
    displayScreen(screen)

    return

def setUpScreen():
    """
    setup screen
    create window
    define size
    define color
    create title
    """
    screen = Tk()
    screen.geometry('600x400')
    screen.geometry('+425+125')
    screen.configure(background = 'orchid')
    screen.title("Herbarium")
    return screen

def configureInterfaceElements(screen, cursor):
    """
    configure welcome label
    configure text entry box
    configure new entry button
    configure search text entry box
    configure search button
    configure display area
    :return:
    """
    configureWelcomeLabel(screen)
    newEntry = configureTextEntry(screen)
    newButton = configureButton(screen, "New Entry", handleEnterAction(newEntry, cursor))
    searchEntry = configureTextEntry(screen)
    searchButton = configureButton(screen, "Search", handleSearchAction(searchEntry, cursor))

    return

def configureWelcomeLabel(screen):
    """
    configure welcome label
    create label
    display in top center of screen
    pack it
    """
    welcome_label = Label(screen, text =  "Welcome to the Herbarium!", bg = 'orchid')
    welcome_label.config(font = ("georgia", 20, "italic bold"))
    welcome_label.pack()
    return welcome_label

def configureTextEntry(screen):
    """
    configure new entry text entry box
    create entry box
    pack it
    """
    entry = Entry(screen, width = 20, bg = 'white')
    entry.pack()
    return entry

def configureButton(screen, text, command):
    """
    create button
    pack
    :return:
    """
    button = Button(screen, text = text, command = command)
    button.pack()
    return button


def configureDisplayArea():
    """
    create text display box
    pack
    :return:
    """
    return


def handleEnterAction(entry, cursor):
    """
    access text from enter bar
    assume user isn't an idiot: types in plant, locality, date
    separate values with ", "
    assign those values to name, locality, and date
    call saveVariablesToDatabase
    call searchDatabase with name
    print that list in display screen
    :return:
    """


    return

def handleSearchAction(search, cursor):
    """
    wait until button is pressed
    access text from search bar
    use text to call searchDatabase
    display result in display screen
    :return:
    """
    name = search.get()
    searchDatabase(name, cursor)
    print(name)
    print(searchDatabase(name, cursor))

def displayScreen(screen):
    """
    display screen
    """
    screen.mainloop()
    return

main()







