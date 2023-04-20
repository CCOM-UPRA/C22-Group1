from .. import dataBase
from flask_login import UserMixin
from .cartmodel import Cart
from .paymentModel import payment
from .ordersModel import Orders


class User(dataBase.Model, UserMixin):
    __tablename__ = 'user'
    id = dataBase.Column(
        dataBase.Integer, primary_key=True, autoincrement=True)
    Fname = dataBase.Column(dataBase.String(100), nullable=False)
    Lname = dataBase.Column(dataBase.String(100), nullable=False)
    Email = dataBase.Column(dataBase.String(150), nullable=False, unique=True)
    Password = dataBase.Column(dataBase.String(255), nullable=False)
    Img = dataBase.Column(dataBase.String(255), default='default.png')
    Address = dataBase.Column(dataBase.String(255), default='')
    ZipCode = dataBase.Column(dataBase.String(255), default='')
    Street = dataBase.Column(dataBase.String(255), default='')
    City = dataBase.Column(dataBase.String(255), default='')
    State = dataBase.Column(dataBase.String(255), default='')
    Phone = dataBase.Column(dataBase.Numeric(precision=10), default=0)
    Status = dataBase.Column(dataBase.Integer, default=1)
    cart = dataBase.relationship('Cart')
    orders = dataBase.relationship('Orders')
    payment = dataBase.relationship('payment')
