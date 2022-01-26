from rest import app,db
from model.schema import Product as pd
from flask import jsonify,request

@app.route('/get-with-filter',methods=['POST'])
def get_with_filter():
    body = request.get_json()
    gender = body.get('gender')
    category = body.get('category')
    size = body.get('size')
    index = body.get('index') if body.get('index') else 1
    slice = body.get('slice') if body.get('slice') else 10
    start = (index-1)*slice
    stop = start + slice
    data = pd.query.with_entities(pd.id,pd.name,pd.price,pd.category,pd.size,pd.gender).filter(
        (pd.category.contains(category)) &\
        (pd.gender.contains(gender)) &\
        (pd.size == size.upper())
    ).all()
    result = [] 
    for value in data[start:stop]:
        obj = {}
        obj['id'] = value[0]
        obj['name'] = value[1]
        obj['price'] = value[2]
        obj['category'] = value[3]
        obj['size'] = value[4]
        obj['gender'] = value[5]
        result.append(obj)
    return jsonify(result)