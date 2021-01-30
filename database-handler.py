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

