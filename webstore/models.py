from webstore import db

class Customer(db.Model):
    c_id = db.Column(db.Integer, primary_key=True)
    c_username = db.Column(db.String(20), unique=True, nullable = False)
    password = db.Column(db.String(20), nullable = False)
    balance = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"User('{self.c_username}','{self.c_id}', '{self.balance}')"  

