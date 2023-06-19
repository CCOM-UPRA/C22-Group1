from flask import Blueprint, render_template, request, redirect, url_for, session
from ..models.frontend.loginModel import *
import hashlib

auth = Blueprint('auth', __name__, template_folder='/templates')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['C_Email']
        password = request.form['C_Password']
        if email_exists(email):
            customer = customerlog(email=email)
            db_password = customer[0]
            customerID = customer[1]
            if password == db_password:
                session['customer'] = customerID
                return redirect(url_for('views.shop'))
            else:
                return 'Password dont match!'
        else:
            return render_template('register.html')
    return render_template('login.html')


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
        session['customer'] = ID_Email(email)
        return render_template('shop.html')
    return render_template('register.html')


@auth.route('/password')
def password():
    pass
