import sqlite3

connect = sqlite3.connect('user.db')

cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (30) NOT NULL,
    age INTEGER NOT NULL,
    hobby TEXT
    )
''')
connect.commit()

#CRUD - Create - Read - Update - Delete

def create_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)',
        (name, age, hobby)
    )
    connect.commit()
    print("User created successfully")

# create_user("person", 30, "voleyball")
# create_user("name", 20, "snowball")
# create_user("akike", 15, "reading")

def get_users():
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()
    print(data)

# get_users()

def update_user(name, id):
    cursor.execute(
        'UPDATE users SET name = ? WHERE id = ?',
        (name, id)
    )
    connect.commit()
    print("User updated successfully")

update_user("Вася", 5)

def delete_user(id):
    cursor.execute(
        'DELETE FROM users WHERE id = ?',
        (id,)
    )
    connect.commit()
    print("User deleted successfully")

# delete_user(4)