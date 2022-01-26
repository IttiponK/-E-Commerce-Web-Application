from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = 'alksdfjlkjasldkfjlksadf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'
db = SQLAlchemy(app)

import rest.productlist
import rest.createorder
import rest.payment
import rest.admin