import sqlite3  # import the module which knows how to interact with SQLite3 databases


def create_table():
    # let's connect & create the database
    connection = sqlite3.connect("first.db")
    cursor = connection.cursor()
    #       CREATE TABLE is the command, crypto is the name of the table, name & price are the columns' names
    cursor.execute("CREATE TABLE crypto ('name' TEXT, 'price' INTEGER)")
    # to save the changes to the database
    connection.commit()
    # we have to close the connection
    connection.close()


def add_coin(name: str, price: int):
    connection = sqlite3.connect("first.db")
    cursor = connection.cursor()
    # INSERT to add a new row, INTO <table_name>
    cursor.execute("INSERT INTO crypto (name, price) VALUES ('" + name + "', " + str(price) + ")")
    connection.commit()
    connection.close()

# create_table()
add_coin("bitcoin", 38000)
