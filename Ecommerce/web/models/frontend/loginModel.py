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
    cursor.execute('SELECT C_Password,CustomerID FROM customers WHERE C_Email = %s', (email,))
    customer = cursor.fetchone()
    return customer

#profile

@DBConnection
def user_info(id, database): #selecciona informacion deacuerdo al id del usuario
    cursor = database.cursor()
    cursor.execute('SELECT C_Fname, C_Lname, C_Email, C_Password, C_Phone, Street_number, Street_name, zipCode, C_City, C_State FROM customers WHERE CustomerID = %s', (id,))
    result = cursor.fetchone()
    return result

@DBConnection
def edit_prof(id, fname, lname, email, database): #edit profile info
    cursor = database.cursor()
    cursor.execute('UPDATE customers SET C_Fname = %s, C_Lname = %s, C_Email = %s WHERE CustomerID = %s ', (fname, lname, email, id)) 
    database.commit()

@DBConnection
def edit_address(id, street_number, street_name, zipcode, c_city, c_state, database): #edit billing addres info
    cursor = database.cursor()
    cursor.execute('UPDATE customers SET Street_number = %s, Street_name = %s, zipCode = %s, C_City = %s, C_State = %s WHERE CustomerID = %s ', (street_number, street_name, zipcode, c_city, c_state, id)) 
    database.commit()   

@DBConnection
def edit_phone(id, C_Phone, database): #edit number 
    cursor = database.cursor()
    cursor.execute('UPDATE customers SET C_Phone = %s WHERE CustomerID = %s ', (C_Phone, id)) 
    database.commit() 
    


@DBConnection
def update_password(id , C_Password, database):
    cursor = database.cursor()
    cursor.execute('UPDATE customers SET C_Password = %s WHERE CustomerID = %s', (C_Password, id))
    database.commit()
    


   