from ...dbConnection import *


@DBConnection
def getProducts(database):
    cursor = database.cursor()
    cursor.execute('select * from telescopes')
    data = cursor.fetchall()
    return data


@DBConnection
def getBrands(database):
    cursor = database.cursor()
    cursor.execute('select DISTINCT Telescope_Brand from telescopes')
    return cursor


@DBConnection
def getMounts(database):
    cursor = database.cursor()
    cursor.execute('select DISTINCT Telescope_Mount from telescopes')
    return cursor


@DBConnection
def getLenses(database):
    cursor = database.cursor()
    cursor.execute('select DISTINCT Telescope_Type from telescopes')
    return cursor


@DBConnection
def getFocal_Distance(database):
    cursor = database.cursor()
    cursor.execute('select DISTINCT Telescope_FD from telescopes')
    return cursor


@DBConnection
def getAperture(database):
    cursor = database.cursor()
    cursor.execute('select DISTINCT Telescope_Aperture from telescopes')
    return cursor


@DBConnection
def getMinPrice(database):
    cursor = database.cursor()
    cursor.execute('select min(price) from telescopes')
    return cursor.fetchone()


@DBConnection
def getMaxPrice(database):
    cursor = database.cursor()
    cursor.execute('select max(price) from telescopes')
    return cursor.fetchone()

@DBConnection
def getCart(id, database):
    cursor = database.cursor()
    cursor.execute('SELECT Order_Id FROM orders WHERE CustomerID = %s and Order_Number = 0 ', (id,))
    return cursor.fetchone()

@DBConnection
def CreateCart(id, database):
    cursor = database.cursor()
    cursor.execute('INSERT INTO orders (CustomerId) VALUES (%s)', (id,))
    database.commit()

@DBConnection
def GetCartData(cartId, database):
    cursor = database.cursor()
    cursor.execute('select * from telescopes join contains on telescopes.TelescopeID = contains.TelescopeID where contains.OrderID = %s', (cartId,))
    return cursor.fetchall()

@DBConnection
def getCartTotalPrice(cartId, database):
    cursor = database.cursor()
    cursor.execute('select sum(total_price) as Total from (SELECT TelescopeID, Product_Quantity * Product_Price as total_price from contains where OrderID = %s) as products_total', (cartId,))
    data = cursor.fetchone()
    
    if data[0] == None:
        return 0
    return data[0]

@DBConnection
def getCartTotalItems(cartId, database):
    cursor = database.cursor()
    cursor.execute('select sum(Product_Quantity) as Total from contains where OrderID = %s', (cartId,))
    data = cursor.fetchone()
    
    if data[0] == None:
        return 0
    return data[0]

@DBConnection
def checkCartProducts(productId, cartId, database):
    cursor = database.cursor()
    cursor.execute('select Product_Quantity from contains where OrderID = %s and TelescopeID = %s', (cartId, productId,))
    data = cursor.fetchone()
    if data == None:
        return 0
    else:
        return data[0]
    
@DBConnection
def checkMaxItemQuantity(productId, database):
    cursor = database.cursor()
    cursor.execute('select Telescope_Stock from telescopes where TelescopeID = %s', (productId,))
    data = cursor.fetchone()
    return data[0]

@DBConnection
def incertToCart(productId, cartId, productCuantity, database):
    cursor = database.cursor()
    cursor.execute('select Telescope_Price from telescopes where TelescopeID = %s', (productId,))
    data = cursor.fetchone()
    price = data[0]
    cursor.execute('insert into contains (OrderID, TelescopeID, Product_Quantity, Product_Price) values (%s, %s, %s, %s)', (cartId, productId, productCuantity, price,))
    database.commit()

@DBConnection
def updateCartItem(productId, cartId, productCuantity, database):
    cursor = database.cursor()
    cursor.execute('update contains set Product_Quantity = %s where OrderID = %s and TelescopeID = %s', (productCuantity, cartId, productId,))
    database.commit()

@DBConnection
def deleteItemFromCart(productId, cartId, database):
    cursor = database.cursor()
    cursor.execute('delete from contains where OrderID = %s and TelescopeID = %s', (cartId, productId,))
    database.commit()