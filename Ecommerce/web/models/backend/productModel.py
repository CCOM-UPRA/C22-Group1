from ...dbConnection import *

#addproducts
@DBConnection
def new_product(tname,tprice,tcost,tbrand,tdesc,timage,tstock,tstatus,ttype,tmount,tfocal,taperture, database): #insertar el user en la base de datos
    cursor = database.cursor()
    cursor.execute('''INSERT INTO telescopes (Telescope_Name, Telescope_Price, Telescope_Cost, Telescope_Brand, 
                   Telescope_Description, Telescope_Img, Telescope_Stock, Telescope_Status, Telescope_Type, Telescope_Mount, 
                   Telescope_FD, Telescope_Aperture) VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s)''',
                    (tname,tprice,tcost,tbrand,tdesc,timage,tstock,tstatus,ttype,tmount,tfocal,taperture))
    database.commit()
    
@DBConnection
def edit_product(id,tname,tprice,tcost,tbrand,tdesc,timage,tstock,tstatus,ttype,tmount,tfocal,taperture, database): #insertar el user en la base de datos
    cursor = database.cursor()
    cursor.execute('''UPDATE telescopes SET Telescope_Name = %s, Telescope_Price = %s, Telescope_Cost = %s, Telescope_Brand = %s, 
                    Telescope_Description = %s, Telescope_Img = %s, Telescope_Stock = %s, Telescope_Status = %s, Telescope_Type = %s, 
                    Telescope_Mount = %s, Telescope_FD = %s, Telescope_Aperture = %s WHERE TelescopeID = %s''',
                    (tname,tprice,tcost,tbrand,tdesc,timage,tstock,tstatus,ttype,tmount,tfocal,taperture,id))
    database.commit()
    
@DBConnection
def getProdID(id, database):
    cursor = database.cursor()
    cursor.execute('select * FROM telescopes WHERE TelescopeID = %s',(id,))
    data = cursor.fetchall()
    return data

@DBConnection
def backgetProducts(database):
    cursor = database.cursor()
    cursor.execute('select * from telescopes')
    return cursor

