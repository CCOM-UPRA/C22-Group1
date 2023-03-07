# Done in array instead of dictionaries to portray the differences between dictionaries and arrays
# Database tuples are normally received in an array
productList = [['1', 'Travel Scope', 'Celestron', 'description', 'Refractor', 'Altazimutal', '70', '400', 'TravelScope.png', '5', 'Active', '86', '86'],

            ['2', 'Astromaster', 'Celestron', 'description', 'Reflector', 'Ecuatorial', '130', '650', 'AstroMaster.png', '3', 'Active', '300', '300'],

            ['3', 'Advanced VX', 'Celestron', 'description', 'Catadioptrico', 'Ecuatorial', '235', '2359', 'AdvancedVX.jpg', '1', 'Active', '3,699', '3,699'],

            ['4', 'Skyscanner 10012', 'Orion', 'description', 'Reflector', 'Altazimutal', '100', '400', 'Skyscanner.jpg', '2', 'Active', '130', '130'],

            ['5', 'Maksutov-Cassegrain Starmax', 'Orion', 'description', 'Catadioptrico', 'Altazimutal', '90', '1250', 'Starmax.jpg', '1', 'Active', '180', '180'],

            ['6', 'Astroview  9024', 'Orion', 'description', 'Refractor', 'Ecuatorial', '90', '910', 'AstroView.jpg', '4', 'Active', '250', '250']]


def getProductsModel():
    return productList


# Find the specific product given the ID, found in element 0 of the sub-arrays
def getsingleproductmodel(prodID):
    for product in productList:
        if product[0] == prodID:
            return product
