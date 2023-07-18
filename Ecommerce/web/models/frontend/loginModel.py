from ...dbConnection import *

#profile
@DBConnection
def user_info(id, database): #selecciona informacion del usuario deacuerdo al id
    cursor = database.cursor()
    cursor.execute('SELECT C_Fname, C_Lname, C_Email, C_Password, C_Phone, Street_number, Street_name, zipCode, C_City, C_State FROM customers WHERE CustomerID = %s', (id,))
    result = cursor.fetchone()
    return result


#edit
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
    
    
#password 
@DBConnection
def old_password(id, database): #obtener el password viejo antes de cambiarlo
    cursor = database.cursor()
    cursor.execute('SELECT C_Password FROM customers WHERE CustomerID = %s', (id,))
    result = cursor.fetchone()
    return result

@DBConnection
def update_password(id, C_Password, database):  #update el password
    cursor = database.cursor()
    cursor.execute('UPDATE customers SET C_Password = %s WHERE CustomerID = %s', (C_Password, id))
    database.commit()
    
    
#paymenth
@DBConnection
def insert_card(CustomerID,Card_Name, Card_type, Card_Number, Card_Month, Card_Year, Card_CVV, Card_zipcode, database): #insertar el payment info en la base de datos
    cursor = database.cursor()
    cursor.execute('INSERT INTO payment (CustomerID, Card_Name, Card_type, Card_Number, Card_Month, Card_Year, Card_CVV, Card_zipcode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (CustomerID,Card_Name, Card_type, Card_Number, Card_Month, Card_Year, Card_CVV, Card_zipcode))
    database.commit()
    
@DBConnection
def card_info(CustomerID, database): #seleccionar todas las tarjetas del usuario
    cursor = database.cursor()
    cursor.execute('SELECT Payment_ID, Card_Name, Card_type, Card_Number, Card_Month, Card_Year, Card_CVV, Card_zipcode FROM payment WHERE CustomerID = %s', (CustomerID,))
    result = cursor.fetchall()
    return result

@DBConnection
def update_payment(c_number, c_name, c_type, year, month, c_id, database): #update the card info
    cursor = database.cursor()
    cursor.execute('UPDATE payment SET Card_Name = %s, Card_Type = %s, Card_Month = %s, Card_Year = %s WHERE Card_number = %s AND Payment_ID = %s' , (c_name, c_type, month, year, c_number, c_id))
    database.commit()