# Orders simulation for the reports that specify date

dictProd1 = {'1': {'name': "Travel Scope", 'price': 86.00, 'quantity': 2, 'total_price': 172.00,
                  'stock': 15, 'brand': "Celestron", 'Mount': 'Altazimutal', 'Lens': 'Refractor', 'desc': " ",
                  'image': 'static/images/product-images/TravelScope.png', 'cost': 86.00}}

dictProd2 = {'2': {'name': "Astromaster", 'price': 86, 'quantity': 3, 'total_price': 258.00,
                  'stock': 4, 'brand': "Celestron", 'Mount': 'Ecuatorial', 'Lens': 'Reflector', 'desc': " ",
                  'image': "static/images/product-images/AstroMaster.png", 'cost': 86.00}}

dictProd3 = {'3': {'name': "Advanced VX", 'price': 3699.00, 'quantity': 1, 'total_price': 3699.00,
                  'stock': 13, 'brand': "Celestron", 'Mount': 'Ecuatorial', 'Lens': 'Catadioptrico', 'desc': " ",
                  'image': "static/images/product-images/AdvancedVX.jpg", 'cost': 3699.00}}

dictProd4 = {'4': {'name': "Skyscanner 10012", 'price': 130.00, 'quantity': 2, 'total_price': 260.00,
                  'stock': 25, 'brand': "Orion", 'Mount': 'Altazimutal', 'Lens': 'Reflector', 'desc': " ",
                  'image': "static/images/product-images/Skyscanner.jpg", 'cost': 130.00}}

dictProd5 = {'5': {'name': "Maksutov-Cassegrain Starmax", 'price': 180.00, 'quantity': 4, 'total_price': 720.00,
                  'stock': 2, 'brand': "Orion", 'Mount': 'Altazimutal', 'Lens': 'Catadioptrico', 'desc': " ",
                  'image': "static/images/product-images/Starmax.jpg", 'cost': 180.00}}

dictProd6 = {'5': {'name': "Astroview  9024", 'price': 250.00, 'quantity': 4, 'total_price': 1000.00,
                  'stock': 65, 'brand': "Orion", 'Mount': 'Ecuatorial', 'Lens': 'Refractor', 'desc': " ",
                  'image': "static/images/product-images/AstroView.jpg", 'cost': 250.00}}




# Orders simulation for the inventory/stock report
product1 = {1: {'name': "Travel Scope", 'brand': 'Celestron', 'quantity': 15}}
product2 = {2: {'name': "Astromaster", 'brand': 'Celestron', 'quantity': 4}}
product3 = {3: {'name': "Advanced VX", 'brand': 'Celestron', 'quantity': 13}}
product4 = {4: {'name': "Skyscanner 10012", 'brand': 'Orion', 'quantity': 25}}
product5 = {5: {'name': "Maksutov-Cassegrain Starmax", 'brand': 'Orion', 'quantity': 2}}
product6 = {6: {'name': "Astroview  9024", 'brand': 'Orion', 'quantity': 65}}


def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False


ordersList = dictProd1
ordersList = MagerDicts(ordersList, dictProd2)
ordersList = MagerDicts(ordersList, dictProd3)
ordersList = MagerDicts(ordersList, dictProd4)
ordersList = MagerDicts(ordersList, dictProd5)


productsList = product1
productsList = MagerDicts(productsList, product2)
productsList = MagerDicts(productsList, product3)
productsList = MagerDicts(productsList, product4)
productsList = MagerDicts(productsList, product5)
productsList = MagerDicts(productsList, product6)


def getDatedReportModel():
    return ordersList


def getStockReportModel():
    return productsList
