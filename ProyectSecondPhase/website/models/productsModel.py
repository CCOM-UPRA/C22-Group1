from .. import dataBase

class Telescopes(dataBase.Model):
    id = dataBase.Column(dataBase.Integer, primary_key = True, autoincrement = True)
    name = dataBase.Column(dataBase.String(255), nullable = False)
    brand = dataBase.Column(dataBase.String(255), nullable = False)
    description = dataBase.Column(dataBase.String(255), nullable = True)
    lens = dataBase.Column(dataBase.String(255), nullable = False)
    mount = dataBase.Column(dataBase.String(255), nullable = False)
    aperture = dataBase.Column(dataBase.Integer, nullable = False)
    focal_distance = dataBase.Column(dataBase.Integer, nullable = False)
    image_name = dataBase.Column(dataBase.String(255), nullable = True)
    stock = dataBase.Column(dataBase.Integer, nullable = False)
    state = dataBase.Column(dataBase.Boolean)
    price = dataBase.Column(dataBase.Numeric, nullable = False)
    cost = dataBase.Column(dataBase.Numeric, nullable = False)