from datetime import datetime
from rest import db

    
class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(250))
    price = db.Column(db.Integer)
    category = db.Column(db.String(500))
    size = db.Column(db.String(10))
    gender = db.Column(db.String(10))

class Transaction(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    transactionid= db.Column(db.String(250),unique=True)
    productid = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    owner = db.Column(db.String(250))
    payment_status = db.Column(db.String(1),default='0')
    payment_date = db.Column(db.DateTime)
    bank_name = db.Column(db.String(250))
    payment_slip = db.Column(db.String(250))
    address = db.Column(db.String(500))
    
    
    