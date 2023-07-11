
from ...dbConnection import *
import sqlite3

#login for admins
@DBConnection
def adminlog(email, database):
    cursor = database.cursor()
    cursor.execute('SELECT C_Password, CustomerID FROM customers WHERE C_Email = %s AND C_Status = %s', (email, 'ADMIN'))
    customer = cursor.fetchone()
    return customer

@DBConnection
def email_exists(C_Email, database): #verificar si el email ya existe en la base de datos
    cursor = database.cursor()
    cursor.execute('SELECT CustomerID FROM customers WHERE C_Email = %s', (C_Email,))
    result = cursor.fetchone()
    return bool(result)