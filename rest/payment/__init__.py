from rest import app,db
from flask import request,jsonify
from model.schema import Transaction as ts 
from datetime import datetime

@app.route('/payment',methods=['POST'])
def payment():
    body = request.get_json()
    transactionid = body.get('transactionid')
    bank_name = body.get('bank_name')
    payment_slip = body.get('payment_slip')
    time_stamp = datetime.today()
    own_transaction = ts.query.filter_by(transactionid=transactionid).first()
    if own_transaction:
        own_transaction.bank_name = bank_name
        own_transaction.payment_slip = payment_slip
        own_transaction.payment_status = True 
        own_transaction.payment_date = time_stamp
        db.session.commit()
        return jsonify({'message':f'Transaction id : {transactionid} is success at {time_stamp}'})
    return jsonify({'message':'Invalid transaction id'})

