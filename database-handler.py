import crypt
import mysql.connector

def setup():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="KurvaNagyVeres05",
        database="CRUDApp"
    )
    cursor = db.cursor()

    return db, cursor

def close(db, cursor):
    cursor.close()
    db.close()

# TODO: create a check_username_already_used() function that checks whether a user is in the Users table

# --- Users --- #

def check_username_already_used(usrname):
    db, cursor = setup()

    cursor.execute(f"SELECT EXISTS(SELECT * FROM Users WHERE username='{usrname}')")
    print(cursor)

    close(db, cursor)

# --- Data --- #