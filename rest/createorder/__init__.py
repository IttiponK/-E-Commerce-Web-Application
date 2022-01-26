from rest import app,db
from model.schema import (
    Product as pd,
    Transaction as ts
)
from flask import request,jsonify
import random

@app.route('/create-order',methods=['POST'])
def create_order():
    body = request.get_json()
    owner = body.get('owner')
    address = body.get('address')
    quantity = body.get('quantity')
    productid = body.get('productid')
    
    product = pd.query.filter_by(id=productid).first()
    if product :
        transactionid = str(random.randint(0,99999)).zfill(5)
        new_transaction = ts(
            productid = productid,
            quantity = quantity,
            amount = quantity * product.price,
            owner = owner,
            address = address,
            transactionid = transactionid
        )
        db.session.add(new_transaction)
        db.session.commit()
        return jsonify({'message':f'Your order already add transaction id is {transactionid}'})
    return jsonify({'message':'Product id is invalid.'})

@app.route('/check-your-order/<owner>')
def check_order(owner):
    your_order = ts.query.filter_by(owner=owner).all()
    if your_order:
        res = []
        for order in your_order:
            obj = {}
            obj['transactionid'] = order.transactionid
            obj['productid'] = order.productid
            obj['quantity'] = order.quantity
            obj['amount'] = order.amount
            obj['payment_status'] = order.payment_status 
            res.append(obj)
    return jsonify(res)
    