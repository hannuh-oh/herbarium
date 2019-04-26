import database

"""
This is my herbarium database!!
what does it do?

prompt:
    ask for the command
    if the command is "search" jump to search:
    if the command is "enter" jump to enter:
    print the results
    jump to prompt:

search:
    ask user for query
    create the query
    execute the query
    return the results

enter:
    ask the user for information
    store information in database
    jump to search:
    
     
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



