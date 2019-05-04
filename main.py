import sqlite3
import herbarium

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
    newHerbs = herbarium.Herbarium(cursor, connection)

main()