from ...dbConnection import *

@DBConnection
def delete_card(number, database):  #update el password
    cursor = database.cursor()
    cursor.execute('UPDATE payment SET Card_Status = %s WHERE Card_number = %s', ('INACTIVE', number))
    database.commit()