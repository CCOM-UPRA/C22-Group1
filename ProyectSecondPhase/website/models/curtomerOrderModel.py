from .. import dataBase
from sqlalchemy.sql import func
from .usermodel import User
from sqlalchemy import text
from datetime import datetime
import json

class JsonEcodedDict(dataBase.TypeDecorator):
    impl = dataBase.Text
        
    def set_value(info, dialect):
        if info is None:
            return '{}'
        else:
            return json.dumps(info)
        
    """""    
    def get_value(info, dialect):
        if info is None:
            return {}
        else:
            return json.loads(info)
    """""
    
    
     

class customerOrder(dataBase.Model):
    order_id = dataBase.Column(dataBase.Integer, primary_key=True, autoincrement=True, nullable=False)
    invoice = dataBase.Column(dataBase.String(20), unique=True, nullable=False)
    user_id = dataBase.Column(dataBase.Integer, dataBase.ForeignKey('user.id'), nullable=True)
    status = dataBase.Column(dataBase.String(20),default='Pending',nullable=False)
    order_date = dataBase.Column(dataBase.DateTime, default=datetime.utcnow, nullable=False)
    orders = dataBase.Column(JsonEcodedDict)
    payment_method = dataBase.Column(dataBase.String(150), nullable=False)
    arrival_date = dataBase.Column(dataBase.DateTime(timezone=True), default=func.now(), nullable=False)
    address1 = dataBase.Column(dataBase.String(150), nullable=True)
    address2 = dataBase.Column(dataBase.String(150), nullable=True)
    total = dataBase.Column(dataBase.Integer, nullable=False)



    
    """"
    def _repr_(self) -> str:
        return '<customerOrder %r>' % self.invoice
        
        INVOICE
        tracking number --
        order date--
        total amount
        payment method--
        
        ORDEN
        order date
        arrival date--
        delivery address---
        
        AMOUNT DETAILS
        total items
        total
        
        TABLA
        product--
        brand--
        name--
        price--
        quantity--
        total price
        
    """