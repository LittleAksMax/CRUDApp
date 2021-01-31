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

def check_username_already_used(usrname: str) -> bool:
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

    cursor.execute(f"DELETE FROM Users WHERE uID={usr_id};")

    cursor.execute(f"DELETE FROM Employees WHERE uID={usr_id};")

    db.commit()

    close(db, cursor)
    
# --- Data --- #

def check_employee_already_present(fname: str, sname: str, uID: int) -> bool:
    db, cursor = setup()

    cursor.execute(f"SELECT EXISTS(SELECT * FROM Employees WHERE fname='{fname}' AND sname='{sname}' AND uID={uID});")
    
    for x in cursor:
        value = x[0] # returns tuple, need first (and only) element, which is result

    close(db, cursor)
    return True if value == 1 else False

def insert_employee(fname: str, sname: str, email: str, uID: int) -> bool:
    # check if already there present
    if check_username_already_used(fname, sname, uID):
        return False

    db, cursor = setup()

    cursor.execute(f"INSERT INTO Employees (fname, sname, email, uID) VALUES ('{fname}', '{sname}', '{email}', {uID});")
    db.commit()

    close(db, cursor)
    return True

def update_employee(emp_id: int, fname: str, sname: str, email: str) -> None:
    # don't need to check if present in table, because it can only show up if the employee is shown

    db, cursor = setup()

    cursor.execute(f"UPDATE Employees SET fname='{fname}', sname='{sname}', email='{email}') WHERE eID={emp_id};")
    db.commit()  

    close(db, cursor)

def delete_employee(emp_id: int) -> None:
    # don't need to check if present in table, because it can only show up if the employee is shown

    db, cursor = setup()

    cursor.execute(f"DELETE FROM Employees WHERE eID={emp_id};")
    db.commit()
    
    close(db, cursor)