from ..dbConnection import *


@DBConnection
def getProducts(database):
    cursor = database.cursor()
    cursor.execute('select * from telescopes')
    return cursor


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


 