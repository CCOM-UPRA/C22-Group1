from .. import dataBase


class Cart(dataBase.Model):
    __tablename = 'Cart'
    id = dataBase.Column(dataBase.Integer, primary_key=True, nullable=False)
    items = dataBase.Column(dataBase.String(255))
    total_price = dataBase.Column(dataBase.String(255))
    total_items = dataBase.Column(dataBase.Integer)
    user_id = dataBase.Column(dataBase.Integer, dataBase.ForeignKey("user.id"))
