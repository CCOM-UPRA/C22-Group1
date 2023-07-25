from flask import Blueprint, render_template, request, redirect, url_for, session
from ..models.frontend.loginModel import *
import hashlib
from ..dbConnection import *

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'customer' not in session:
            return redirect('/')
        return func(*args, **kwargs)
    return wrapper


auth = Blueprint('auth', __name__, template_folder='/templates')


#import mysql.connector
from functools import wraps


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['C_Email']
        password = request.form['C_Password']
        if email_exists(email):
            customer = customerlog(email)
            db_password = customer[0]
            customerID = customer[1]
            print(customer)
            customerS = customer[2]
            if password == db_password:
                if customerS == 'ADMIN':
                    session['customer'] = customerID
                    return render_template('products.html')  #redirect(url_for('back_views.admin_products'))
                elif customerS == 'ACTIVE':
                    session['customer'] = customerID
                    return redirect(url_for('views.shop'))
                else:
                   return redirect(url_for('auth.login', message='Cuenta Inactiva..'))
            else:
                return 'Password dont match!'
        else:
            return render_template('register.html')
            
    return render_template('login.html')






@auth.route('/home')
def home():
    return render_template('shop.html')

@auth.route('/logout')
def logout():
    session.pop('customer')
    return render_template('/login.html')


@auth.route('/register' , methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fname = request.form['C_fname']
        lname = request.form['C_lname']
        email = request.form['C_email']
        pass1 = request.form['C_password1']
        pass2 = request.form['C_password2']
        
        if not fname or not lname or not email or not pass1 or not pass2:
            return 'fill all the blanks'
        
        if pass1 != pass2:
            return 'Password dont match!'
        
        if email_exists(email):
            return 'Email already exists!'
        pass1_hash = hashlib.sha256(pass1.encode()).hexdigest()
        insert_user(fname, lname, email, pass1)
        session['customer'] = ID_Email(email)[0]
        
        return render_template('shop.html')
    return render_template('register.html')


@auth.route('/password')
def change_password():
    pass
