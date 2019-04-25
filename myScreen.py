# info from this webiste: http://effbot.org/tkinterbook/button.htm
# and dis one: https://yagisanatode.com/2018/02/26/how-to-display-and-entry-in-a-label-tkinter-python-3/

#set up screen
from tkinter import *
screen = Tk()



#defines the size, position, and color
screen.geometry('600x400')
screen.geometry('+425+125')
screen.configure(background = 'orchid')
screen.title("Herbarium")



#is my welcome to thee herbarium text. Doesn't do anything, looks nice.
welcomeLabel = Label(screen, text =  "Welcome to the Herbarium!", bg = 'orchid')
welcomeLabel.config(font = ("georgia", 20, "italic bold"))
welcomeLabel.pack()



#function that controls what search button does
def searchAction():
    itWorked = 'heello! this worked!'
    return itWorked



#function that control what enter button does
def enterAction():
    newEntry = 'cool find'
    return newEntry



#function that activates entry bar when enter button is pressed
def pressedEntry():
    return none



#function that activates search bar when when search button is pressed
def pressedSearch():
    if searchButton is True:
        textEntry = Entry(screen, width = 20, bg = 'white')
        textEntry.pack()
    return none



#working on my search button
searchButton = Button(screen, text = "Search", command = searchAction())
searchButton.pack()



#working on my enter button
enterButton = Button(screen, text = "New Entry", command = enterAction())
enterButton.pack()


#entry bar
entryBar = Entry(screen, width = 20)
entryBar.pack()


#i don't exactly know what this does
screen.mainloop()
