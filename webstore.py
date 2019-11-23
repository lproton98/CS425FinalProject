from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, CustomerLoginForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:harvest091@localhost/OnlineGroceryStore'
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

db = SQLAlchemy(app)

class Customer(db.Model):
    c_id = db.Column(db.Integer, primary_key=True)
    c_username = db.Column(db.String(20), unique=True, nullable = False)
    password = db.Column(db.String(20), nullable = False)
    balance = db.Column(db.Integer, nullable = False)

    def __init__(self, c_username, password):
        self.c_username = c_username
        self.password = password
    
    def __repr__(self):
        return f"User('{self.c_username}','{self.c_id}', '{self.balance}')"  


@app.route('/')
@app.route('/home')  #now we have 2 routes to get to the hello_world page --> /home and just /
def home():
    return render_template('home.html')
@app.route('/shop')  #new route, new function -> Allows us to have multiple pages easily.
def shop():
    return render_template('shop.html')
@app.route('/login', methods=['GET', 'POST'])
def customer_login(): #Customer Login page
    form = CustomerLoginForm()
    if form.validate_on_submit(): #checking validation of data
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('customerlogin.html', title='Customer Login',form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): #checking validation of data
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register',form=form)
    

if __name__ == "__main__":
    app.run(debug=True)
