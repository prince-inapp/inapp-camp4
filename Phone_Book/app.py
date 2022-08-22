from flask import Flask
import pyodbc

conString = 'Driver={SQL Server};Server=DESKTOP-CKLRF1B\SQLEXPRESS;Database=PhoneBook;Truseted_Connection=yes;'

phoneBook = []

def displayOptions():
    print('''
    1. List all contacts
    2. Add new contact
    3. Delete contact
    4. Search contact by name
    5. Search contact by number
    6. Exit
    ''')

def createTable():
    try:
        conn = pyodbc.connect(conString)
        myCursor = conn.cursor()
        myCursor.execute('''CREATE TABLE Contacts
        (id int identity primary key,
        Name varchar(20),
        Number varchar(20)
        );
        ''')
        conn.commit()
        return True
    except Exception as e:
        #print(type(e).__name__)
        return False


    
if(createTable()):
    print("Table Created")
else:
    print("Table Exists")        
   

try:
    phoneBook = []
    conn = pyodbc.connect(conString)
    myCursor = conn.cursor()
    myCursor.execute('SELECT * FROM Contacts;')
    for row in myCursor:
        #print(row)
        contact = {
            'id': row[0],
            'name': row[1],
            'number': row[2]
        }
        phoneBook.append(contact)
    print(phoneBook)
except Exception as e:
    print(e)
