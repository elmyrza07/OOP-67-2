import sqlite3

connect = sqlite3.connect('store.db')

cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (30) NOT NULL,
    price INTEGER NOT NULL,
    quantity  TEXT
    )
''')
connect.commit()

#CRUD - Create - Read - Update - Delete

def add_product(name, price, quantity):
    cursor.execute(
        'INSERT INTO products(name, price, quantity) VALUES (?, ?, ?)',
        (name, price, quantity)
    )
    connect.commit()
    print("Proccess created successfully")

# add_product("milka", 130, 10)
# add_product("snikers", 150, 30)
# add_product("kurut", 1, 200)

def read_products():
    cursor.execute('SELECT * FROM products')
    data = cursor.fetchall()
    print(data)

read_products()

def update_product(price, id):
    cursor.execute(
        'UPDATE products SET price = ? WHERE id = ?',
        (price, id)
    )
    connect.commit()
    print("Product updated successfully")

update_product(100, 1)

def delete_product(id):
    cursor.execute(
        'DELETE FROM products WHERE id = ?',
        (id,)
    )
    connect.commit()
    print("Product deleted successfully")

delete_product(4)