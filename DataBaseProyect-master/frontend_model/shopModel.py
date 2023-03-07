from backend_model.productsModel import productList
# This is our simulation of the database
# We have two products here.
# The students must create their own productList when working on their eCommerce site
# Product images are loaded into static/images/product-images/
# Done in array instead of dictionaries to portray the differences


def getProductsModel():
    return productList


def getBrandsModel():
    # Simulating grabbing these filters via SQL from the database
    brands = ["Celestron", "Orion"]
    return brands

def getMountModel():
    Mount = ['Altazimutual', 'Ecuatorial']
    return Mount


def getFocalDistanceModel():
    FocalDistance = ['400', '650', '2350', '1250', '910']
    return FocalDistance


def getApertureModel():
    Aperture = ['70', '90', '100', '130', '235']
    return Aperture

def getTipeModel():
    Model = ['Reflector', 'Refractor', 'catadioptric']
    return Model
