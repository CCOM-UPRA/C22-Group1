from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from ..models.frontend.loginModel import *
from ..models.frontend.authModel import *
import hashlib

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'customer' not in session:
            return redirect('/')
        return func(*args, **kwargs)
    return wrapper


auth = Blueprint('auth', __name__, template_folder='/templates')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['C_Email']
        password = request.form['C_Password']
        if email_exists(email):
            customer = customerlog(email)
            customerS = customer[2]
            db_password = customer[0]
            customerID = customer[1]
            customer_status = customer[2]
            if password == db_password:
                
                if customer_status == 'ACTIVE':
                    session['customer'] = customerID
                    return redirect(url_for('views.shop'))
                
                elif customer_status == 'INACTIVE':
                    flash('ACCOUNT IS INACTIVE. CONTACT AN ADMINISTRATOR', 'ERROR')
                    return redirect(url_for('auth.login'))
                
                elif customer_status == 'ADMIN':
                    session['customer'] = customerID
                    return redirect(url_for('back_views.products'))
                
            else:
                flash('PASSWORD IS INCORRRECT', 'ERROR')
                return redirect(url_for('auth.login'))
            
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
            flash('fill all the blanks', 'ERROR')
            return redirect(url_for('auth.register'))
        
        if pass1 != pass2:
            flash('Password dont match!', 'ERROR')
            return redirect(url_for('auth.register'))
        
        if email_exists(email):
            flash('Email already exists', 'ERROR')
            return redirect(url_for('auth.register'))
        pass1_hash = hashlib.sha256(pass1.encode()).hexdigest()
        insert_user(fname, lname, email, pass1)
        session['customer'] = ID_Email(email)[0]
        
        return render_template('shop.html')
    return render_template('register.html')


@auth.route('/password')
def change_password():
    pass