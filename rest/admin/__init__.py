from rest import app
from model.schema import Transaction as ts 
from flask import jsonify,request
from datetime import datetime

@app.route('/admin/filter-transaction',methods=['POST'])
def filter_transaction():
    body = request.get_json()
    start = datetime.strptime(body.get('start'),'%Y-%m-%d')
    end = datetime.strptime(body.get('end'),'%Y-%m-%d')
    payment_status = body.get('payment_status') 
    index = body.get('index') if body.get('index') else 1
    slice = body.get('slice') if body.get('slice') else 10
    start_slice = (index-1)*slice
    stop_slice = start_slice + slice
    print(start,flush=True)
    print(end,flush=True)
    print(payment_status,flush=True)
    if payment_status in [True,False]:
        data = ts.query.filter(
            (ts.payment_status == payment_status) &\
            (ts.payment_date >= start) &\
            (ts.payment_date <= end) 
        ).all()
    else:
        data = ts.query.filter(
            (ts.payment_date >= start) &\
            (ts.payment_date <= end) 
        ).all()
    result = []
    for value in data[start_slice:stop_slice]:
        obj = {}
        obj['id'] = value.id
        obj['transaction'] = value.transactionid
        obj['productid'] = value.productid
        obj['quantity'] = value.quantity
        obj['amount'] = value.amount
        obj['owner'] = value.owner
        obj['payment_status'] = value.payment_status
        obj['payment_date'] = value.payment_date
        obj['bank_name'] = value.bank_name
        obj['payment_slip'] = value.payment_slip
        obj['address'] = value.address
        result.append(obj)
    return jsonify(result)
