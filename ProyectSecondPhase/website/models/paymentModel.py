from .. import dataBase
from sqlalchemy.sql import func

class payment(dataBase.Model):
    __tablename = 'payment'
    id = dataBase.Column(dataBase.Integer, primary_key=True)
    name = dataBase.Column(dataBase.String(20), nullable=True)
    type = dataBase.Column(dataBase.String(20), nullable=True)
    number = dataBase.Column(dataBase.Integer, nullable=True)
    month = dataBase.Column(dataBase.Integer, nullable=True)
    year = dataBase.Column(dataBase.Integer, nullable=True)
    user_id = dataBase.Column(dataBase.Integer, dataBase.ForeignKey("user.id"))    





    
