import sqlite3
try:
    conn=sqlite3.connect("database.db")
    print("Database connection is successfull.")

    conn.execute('''CREATE TABLE IF NOT EXISTS dates
     (ID INT PRIMARY KEY NOT NULL,
     OWNER TEXT NOT NULL,
     HOWMANYPEOPLE INT NOT NULL,
     DATEOF DATE NOT NULL,
     TIMEOF DATETIME NOT NULL);''')

    print("Table checking is ok.")
except:
    print("Hata")
    raise
