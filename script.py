
import queries
import mysql
import os






print("Welcome to the CLI contact list\n.1 Add contact\n.2 Get contact\n")
optioninput = input("\nPlease enter the number of the function you want to execute and press enter: ")
  
if optioninput.find('1') != -1:
    os.system('clear')
    FirstName = input("Fill in an first name: ")
    LastName = input("Fill in a last name: ")
    EmailAdress = input("Fill in a email adress: ")    
    val = (FirstName, LastName, EmailAdress)
    mysql.query.execute(queries.addcontact, val)

    mysql.connection.commit()
    
    
else:
    exit()
  
  








