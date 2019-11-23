from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:harvest091@localhost/OnlineGroceryStore'
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

db = SQLAlchemy(app)

from webstore import routes