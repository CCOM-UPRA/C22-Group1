# Dictionary uniter
def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False


# Simulated database of orders and their products
# order1 contains productsOrder1...
order1 = {"tracking_num": "71287249",
    "order_date": "01/17/23",
    "arrival_date": "01/20/23",
    "address_line_1": "Vista Azulin Calle 11 L13",
    "address_line_2": "Arecibor Puerto Ricor, 00614",
    "total": 1197.00,
    "amount": 3,
    "payment_method": "Mastercard",
    "status": 'shipped'}

order2 = {"tracking_num": "92391290",
    "order_date": "01/20/23",
    "arrival_date": "01/23/23",
    "address_line_1": "Vista Azulin Calle 11 L13",
    "address_line_2": "Arecibor Puerto Ricor, 00614",
    "total": 629.00,
    "amount": 3,
    "payment_method": "Mastercard",
    "status": 'delivered'}

productDict1 = {"1": {
    "image": 'TravelScope.png',
    "name": 'Travel Scope',
    "brand": 'Celestron',
    "price": 86.00,
    "quantity": 1,
    "total_price": 86.00
}}

productDict2 = {"2": {
    "image": 'AstroMaster.png',
    "name": 'Astromaster',
    "brand": 'Celestron',
    "price": 300.00,
    "quantity": 2,
    "total_price": 600.00
}}

productsOrder1 = productDict1
productsOrder1 = MagerDicts(productsOrder1, productDict2)

productDict3 = {"3": {
    "image": 'AdvancedVX.jpg',
    "name": 'Advanced VX',
    "brand": 'Celestron',
    "price": 3699.00,
    "quantity": 2,
    "total_price": 7398.00
}}

productDict4 = {"4": {
    "image": 'Skyscanner.jpg',
    "name": 'Skyscanner 10012',
    "brand": 'Orion',
    "price": 130.00,
    "quantity": 1,
    "total_price": 130.00
}}

productsOrder2 = productDict3
productsOrder2 = MagerDicts(productsOrder2, productDict4)


def getorder1M():
    return order1


def getorder2M():
    return order2


def getorder1prodM():
    return productsOrder1


def getorder2prodM():
    return productsOrder2




