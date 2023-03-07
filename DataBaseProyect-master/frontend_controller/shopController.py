from frontend_model.shopModel import *


def getProducts():
    products = getProductsModel()
    return products


def getBrands():
    return getBrandsModel()


def getMount():
    return getMountModel()


def getFocalDistance():
    return getFocalDistanceModel()


def getAperture():
    return getApertureModel()

def getTipe():
    return getTipeModel()