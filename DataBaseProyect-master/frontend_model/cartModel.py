from flask import session

# Dictionary uniter
def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False


# Cart items simulated
dictitems1 = {'1': {'name': "Travel Scope", 'price': 86.00, 'quantity': 2, 'total_price': 172.00,
                  'stock': 15, 'brand': "Celestron", 'Mount': 'Altazimutal', 'Lens': 'Refractor', 'desc': " ",
                  'image': 'static/images/product-images/TravelScope.png', 'cost': 86.00}}

dictitems2 = {'3': {'name': "Advanced VX", 'price': 3699.00, 'quantity': 1, 'total_price': 3699.00,
                  'stock': 10, 'brand': "Celestron", 'Mount': 'Ecuatorial', 'Lens': 'Catadioptrico', 'desc': " ",
                  'image': "static/images/product-images/AdvancedVX.jpg", 'cost': 3699.00}}

def getCartModel():
    # Checking if cart is in session or not and adding the dictionaries to it
    if 'cart' in session:
        session['cart'] = MagerDicts(session['cart'], dictitems1)
    else:
        session['cart'] = dictitems1

    if 'cart' in session:
        session['cart'] = MagerDicts(session['cart'], dictitems2)
    else:
        session['cart'] = dictitems2

    return


def addCartModel():
    # make changes to cart here
    # not in use at the moment
    return


def deleteCartItemModel():
    # delete item from cart
    # not in use at the moment
    return



