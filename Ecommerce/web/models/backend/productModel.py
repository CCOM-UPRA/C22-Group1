from ...dbConnection import *

#addproducts
@DBConnection
def new_product(tname,tprice,tcost,tbrand,tdesc,timage,tstock,tstatus,ttype,tmount,tfocal,taperture, database): #insertar el user en la base de datos
    cursor = database.cursor()
    cursor.execute('''INSERT INTO telescopes (Telescope_Name, Telescope_Price, Telescope_Cost, Telescope_Brand, 
                   Telescope_Description, Telescope_Img, Telescope_Stock, Telescope_Status, Telescope_Type, Telescope_Mount, 
                   Telescope_FD, Telescope_Apeerture) VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s)''',
                    (tname,tprice,tcost,tbrand,tdesc,timage,tstock,tstatus,ttype,tmount,tfocal,taperture))
    database.commit()
