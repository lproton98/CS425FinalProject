from flask import render_template, url_for, flash, redirect
from webstore import app
from webstore.forms import RegistrationForm, CustomerLoginForm
from webstore.models import Customer


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