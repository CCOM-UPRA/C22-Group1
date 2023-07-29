from ...dbConnection import *

#register
@DBConnection
def insert_user(C_Fname, C_Lname, C_Email, C_password, database): #insertar el user en la base de datos
    cursor = database.cursor()
    cursor.execute('INSERT INTO customers (C_Fname, C_Lname, C_Email, C_Password) VALUES (%s, %s, %s, %s)', (C_Fname, C_Lname, C_Email, C_password, ))
    database.commit()

@DBConnection
def email_exists(C_Email, database): #verificar si el email ya existe en la base de datos
    cursor = database.cursor()
    cursor.execute('SELECT CustomerID FROM customers WHERE C_Email = %s', (C_Email,))
    result = cursor.fetchone()
    return bool(result)

@DBConnection
def ID_Email(C_Email, database): #obtener el id dependiendo del email
    cursor = database.cursor()
    cursor.execute('SELECT CustomerID FROM customers WHERE C_Email = %s', (C_Email,))
    result = cursor.fetchone()
    return result


#login
@DBConnection
def customerlog(email,database): #Obtiene el password y el customer id del email (gabriel)
    cursor = database.cursor()
    cursor.execute('SELECT C_Password, CustomerID, C_status FROM customers WHERE C_Email = %s', (email,))
    customer = cursor.fetchone()
    return customer