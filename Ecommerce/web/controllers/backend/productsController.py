from ...models.backend.productModel import *
from ...models.frontend.shopModel import *

def edit_Telescope(prodID):
    products = getProdID(prodID)
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

def back_Telescope():
    products = backgetProducts()
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