from tkinter import *
import sqlite3
import sys

class Herbarium:

    screen = Tk()
    cursor = None
    newEntryName = None
    newEntryLocality = None
    newEntryDate = None
    newButton = None
    searchEntry = None
    searchButton = None
    displayArea = None
    deleteButton = None

    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.createTable(connection)
        while True:
            self.promptUserForCommand()
            connection.commit()

    def createTable(self, connection):
        """
        creates table in sqlite3
        takes in name, locality, date
        :return:
        """
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS project(
        id integer PRIMARY KEY,
        name text NOT NULL,
        locality text,
        date text 
        );
        ''')
        connection.commit()
        return


    def promptUserForCommand(self):
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
            self.userEnterNewPlant()
        elif command == 's':
            self.userSearchDatabase()
        elif command == 'd':
            self.userDeleteEntry()
        elif command == 'x':
            self.userExitProgram()
        elif command == 'w':
            self.userDisplayWindow()
        return


    def userEnterNewPlant(self):
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
        self.saveVariablesToDatabase(name, locality, date)
        search_result = self.searchDatabase(name)
        print(search_result)
        return


    def userSearchDatabase(self):
        """
        ask user to enter search word
        get result using searchDatabase
        no entry returns all
        print result
        :return:
        """
        search_term = input("What are you searching for?")
        result = self.searchDatabase(search_term)
        if isinstance(result, list):
            for each in result:
                print(each)
        else:
            print(result)
        return


    def searchDatabase(self, search_term):
        """
        create query to select from database
        execute query
        :return: result
        """
        if search_term == "":
            return self.returnAllEntries()
        else:
            query = f"SELECT name, locality, date, id FROM project WHERE name='{search_term}'"
            self.cursor.execute(query)
            return self.cursor.fetchone()

    def returnAllEntries(self):
        """
        query to search everything in database
        execute query
        returns all entries
        :param cursor:
        :return:
        """
        query = "SELECT * FROM project"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def userDeleteEntry(self):
        """
        ask user for name
        call searchDatabase using name
        get result
        confirm?
        delete result

        :return:
        """
        delete_term = input("What do you want to delete?")
        result = self.searchDatabase(delete_term)
        print(result)
        if result is None:
            return
        confirmation = input("Do you wish to proceed? Y/N").lower()
        if confirmation == 'y':
            delete_query = f" DELETE FROM project WHERE id = '{result[-1]}'"
            self.cursor.execute(delete_query)

        return


    def saveVariablesToDatabase(self, name, locality, date):
        """
        1. creating query
        2. execute query
        """

        query = f" INSERT INTO project(name, locality, date) VALUES ('{name}', '{locality}', '{date}') "
        self.cursor.execute(query)

        return 0


    def userExitProgram(self):
        """
        close connection
        exits the program
        :return:
        """

        self.cursor.close()
        sys.exit()

    def userDisplayWindow(self):
        """
        call set up screen
        call user interface elements
        call display screen
        """
        self.setUpScreen()
        self.configureInterfaceElements()
        self.displayScreen()

        return

    def setUpScreen(self):
        """
        setup screen
        create window
        define size
        define color
        create title
        """

        self.screen.geometry('600x400')
        self.screen.geometry('+425+125')
        self.screen.configure(background = 'orchid')
        self.screen.title("Herbarium")

    def configureInterfaceElements(self):
        """
        configure welcome label
        configure text entry box
        configure new entry button
        configure search text entry box
        configure search button
        configure display area
        :return:
        """
        self.configureWelcomeLabel()
        self.newEntryName = self.configureTextEntry()
        self.newEntryLocality = self.configureTextEntry()
        self.newEntryDate = self.configureTextEntry()
        self.newButton = self.configureButton( "New Entry", self.handleEnterAction)
        self.searchEntry = self.configureTextEntry()
        self.searchButton = self.configureButton("Search", self.handleSearchAction)
        self.configureDisplayArea()
        self.deleteButton = self.configureButton("Delete", self.handleDeleteAction)
        return

    def configureWelcomeLabel(self):
        """
        configure welcome label
        create label
        display in top center of screen
        pack it
        """
        welcome_label = Label(self.screen, text =  "Welcome to the Herbarium!", bg = 'orchid')
        welcome_label.config(font = ("georgia", 20, "italic bold"))
        welcome_label.pack()
        return welcome_label

    def configureTextEntry(self):
        """
        configure new entry text entry box
        create entry box
        pack it
        """
        entry = Entry(self.screen, width = 20, bg = 'white')
        entry.pack()
        return entry

    def configureButton(self, text, command):
        """
        create button
        pack
        :return:
        """
        button = Button(self.screen, text = text, command = command)
        button.pack()
        return button


    def configureDisplayArea(self):
        """
        create text display box
        pack
        :return:
        """
        self.displayArea = Listbox(self.screen, width=30, height=10)
        self.displayArea.pack()
        return


    def handleEnterAction(self):
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
        self.displayArea.delete(0, END)
        name = self.newEntryName.get()
        locality = self.newEntryLocality.get()
        date = self.newEntryDate.get()
        self.saveVariablesToDatabase(name, locality, date)
        result = self.searchDatabase(name)
        self.displayArea.insert(END, result)
        return

    def handleSearchAction(self):
        """
        wait until button is pressed
        access text from search bar
        use text to call searchDatabase
        display result in display screen
        :return:
        """
        self.displayArea.delete(0, END)
        name = self.searchEntry.get()
        result = self.searchDatabase(name)
        if isinstance(result, list):
            for each in result:
                self.displayArea.insert(END, each)
        else:
            self.displayArea.insert(END, result)
        return

    def handleDeleteAction(self):
        self.displayArea.delete(ANCHOR)
        result = self.displayArea.get(ANCHOR)
        print("You have deleted this entry:", result)
        delete_query = f" DELETE FROM project WHERE id = '{result[0]}'"
        self.cursor.execute(delete_query)
        return

    def displayScreen(self):
        """
        display screen
        """
        self.screen.mainloop()
        return
