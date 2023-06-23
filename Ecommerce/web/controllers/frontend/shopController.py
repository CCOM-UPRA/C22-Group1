from ...models.frontend.shopModel import *
from flask import session


def Telescopes():
    products = getProducts()
    productsList = []
    for x in products:
        product = {
            'id': x[0],
            'name': x[1],
            'price': x[2],
            'cost': x[3],
            'brand': x[4],
            'description': x[5],
            'image': x[6],
            'stock': x[7],
            'status': x[8],
            'type': x[9],
            'mount': x[10],
            'focal_distance': x[11],
            'aperture': x[12],
        }
        productsList.append(product)

    return productsList


def Brands():
    brands = getBrands()
    brandsList = []
    for brand in brands:
        brandsList.append(brand[0])
    return brandsList


def Mounts():
    mounts = getMounts()
    mountsList = []
    for mount in mounts:
        mountsList.append(mount[0])
    return mountsList


def Lenses():
    lenses = getLenses()
    lensesList = []
    for lense in lenses:
        lensesList.append(lense[0])
    return lensesList


def FocalDistance():
    focalDistance = getFocal_Distance()
    focalDistanceList = []
    for focal_Distance in focalDistance:
        focalDistanceList.append(focal_Distance[0])
    return focalDistanceList


def Aperture():
    aperture = getAperture()
    apertureList = []
    for Aperture in aperture:
        apertureList.append(Aperture[0])
    return apertureList

def Cart():
    userId = session['customer']
    data = getCart(userId)
    if len(data) == 0:
        CreateCart(userId)
        data = getCart(userId)
        cart = data[0]
    
    session['cart'] = cart
