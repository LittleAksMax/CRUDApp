import crypt
import mysql.connector

def setup():
    db = mysql.connector.connect(
        host="192.168.0.95",
        user="littleaksmax",
        passwd="KurvaNagyVeres05",
        database="CRUDApp"
    )
    cursor = db.cursor()

    return db, cursor

def close(db, cursor):
    cursor.close()
    db.close()

# --- Users --- #

def check_username_already_used(usrname):
    db, cursor = setup()

    cursor.execute(f"SELECT EXISTS(SELECT * FROM Users WHERE username='{usrname}');")
    
    for x in cursor:
        value = x[0] # returns tuple, need first (and only) element, which is result

    close(db, cursor)
    return True if value == 1 else False

def insert_user(usrname: str, passwd: str) -> bool:
    if check_username_already_used(usrname):
        return False # unsuccessful insertion, username already present in Users

    db, cursor = setup()

    # I need to get the salt and the pepper of the password first
    salt = crypt.get_salt_pepper()
    pepper = crypt.get_salt_pepper()
    passwd = crypt.encrypt(salt, pepper, passwd)

    cursor.execute(f"INSERT INTO Users (username, salt, pepper, password) VALUES \
        ('{usrname}','{salt}', '{pepper}', '{passwd}');")    
    db.commit()

    close(db, cursor)

    return True # successful insertion

def delete_user(usr_id: str) -> None:
    # don't need to verify the user already being in Users, as this option can
    # only come up if they are logged in

    db, cursor = setup()

    cursor.execute(f"DELETE FROM Users WHERE uID='{usr_id}'")

    cursor.execute(f"DELETE FROM Data WHERE uID='{usr_id}'")

    db.commit()

    close(db, cursor)
    
# --- Data --- #

def insert_employee(fname: str, sname: str, email: str, birthdate: str) -> bool:
    pass

def update_employee(fname: str, sname: str, email: str, birthdate: str) -> bool:
    pass

def delete_employee(fname: str, sname: str, email: str, birthdate: str) -> bool:
    pass