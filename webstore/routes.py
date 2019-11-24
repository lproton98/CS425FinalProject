from flask import render_template, url_for, flash, redirect
from webstore import app, db
from webstore.forms import RegistrationForm, CustomerLoginForm
from webstore.models import Customer
from flask_login import login_user, current_user, logout_user


@app.route('/')
@app.route('/home')  #now we have 2 routes to get to the hello_world page --> /home and just /
def home():
    return render_template('home.html')

@app.route('/shop')  #new route, new function -> Allows us to have multiple pages easily.
def shop():
    return render_template('shop.html')

@app.route('/login', methods=['GET', 'POST'])
def customer_login(): #Customer Login page
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = CustomerLoginForm()
    if form.validate_on_submit(): #checking validation of data
        user = Customer.query.filter_by(c_username=form.username.data).first()
        if user and (user.password == form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccesful, No account exists!', 'danger')
        return redirect(url_for('home'))

    return render_template('customerlogin.html', title='Customer Login',form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit(): #checking validation of data
        customer = Customer(c_username=form.username.data, password=form.password.data,balance=0,
                            first_name=form.first_name.data, last_name=form.last_name.data)
        db.session.add(customer)
        db.session.commit()
        flash(f'Account Created!', 'success')
        return redirect(url_for('customer_login'))
    return render_template('register.html', title = 'Register',form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
def account():
    return render_template('account.html', title='Account')
    
