from flask import Flask, jsonify, request, abort
import pyodbc

conString = 'Driver={SQL Server};Server=DESKTOP-CKLRF1B\SQLEXPRESS;Database=PhoneBook;Truseted_Connection=yes;'

phoneBook = []

app = Flask(__name__)

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
   

@app.route('/contacts', methods=['GET'])
def contacts():
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
    return jsonify({'phoneBook':phoneBook})

@app.route('/contacts/<int:id>', methods=['GET'])
def getContact(id):
    conn = pyodbc.connect(conString)
    myCursor = conn.cursor()
    myCursor.execute('SELECT * FROM Contacts WHERE id = ?', id)
    row = myCursor.fetchone()
    if row is None:
        return jsonify({'result':False})
    contact = {
        'id': row[0],
        'name': row[1],
        'number': row[2]
    }
    return jsonify({'contact':contact})

@app.route('/contacts', methods=['POST'])
def addContact():
    if not request.json:
        abort(400)
    conn = pyodbc.connect(conString)
    myCursor = conn.cursor()
    myCursor.execute('INSERT INTO Contacts (Name, Number) VALUES (?, ?)', request.json['name'], request.json['number'])
    conn.commit()
    return jsonify({'result':True})

@app.route('/contacts/<int:id>', methods=['PUT'])
def updateContact(id):
    conn = pyodbc.connect(conString)
    myCursor = conn.cursor()
    myCursor.execute('SELECT * FROM Contacts WHERE id = ?', id)
    row = myCursor.fetchone()
    if row is None:
        return jsonify({'result':False})
    myCursor.execute('UPDATE Contacts SET Name = ?, Number = ? WHERE id = ?', request.json['name'], request.json['number'], id)
    conn.commit()
    return jsonify({'result':True})

@app.route('/contacts/<int:id>', methods=['DELETE'])
def deleteContact(id):
    conn = pyodbc.connect(conString)
    myCursor = conn.cursor()
    myCursor.execute('SELECT * FROM Contacts WHERE id = ?', id)
    row = myCursor.fetchone()
    if row is None:
        return jsonify({'result':False})
    myCursor.execute('DELETE FROM Contacts WHERE id = ?', id)
    conn.commit()
    return jsonify({'result':True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

