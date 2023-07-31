from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from ..models.frontend.loginModel import *
from ..models.frontend.authModel import *
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


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['C_Email']
        password = request.form['C_Password']
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        if email_exists(email):
            customer = customerlog(email)
            db_password = customer[0]
            customerID = customer[1]
            customer_status = customer[2]
            if password_hash == db_password:
                
                if customer_status == 'ACTIVE':
                    session['customer'] = customerID
                    return redirect(url_for('views.shop'))
                
                elif customer_status == 'INACTIVE':
                    flash('ACCOUNT IS INACTIVE. CONTACT AN ADMINISTRATOR', 'ERROR')
                    return redirect(url_for('auth.login'))
                
                elif customer_status == 'ADMIN':
                    session['admin'] = customerID
                    return redirect(url_for('back_views.products'))
                
            else:
                flash('PASSWORD IS INCORRRECT', 'ERROR')
                return redirect(url_for('auth.login'))
            
        else:
            flash('CREATE AN ACCOUNT IF YOU WANT TO USE THE STORE', 'ERROR')
            return render_template('register.html')
            
    return render_template('login.html')


@auth.route('/home')
def home():
    return render_template('shop.html')


@auth.route('/logout')
def logout():
    session.pop('customer')
    session.pop('cart')
    session.pop('cartTotalItems')
    session.pop('cartTotalPrice')
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
        insert_user(fname, lname, email, pass1_hash)
        session['customer'] = ID_Email(email)[0]
        
        return redirect(url_for('views.shop'))
    return render_template('register.html')


@auth.route('/Cpassword', methods=['GET', 'POST'])
def Cpassword(): 
    if request.method == 'POST':
        email = request.form['C_email']
        pass1 = request.form['pass_n']
        pass2 = request.form['pass_n1']
        if email_exists(email):
            if pass1 != pass2:
                flash('Password dont match!', 'ERROR')
                return redirect(url_for('auth.Cpassword'))
            reset_password(email, pass2) 
            flash('Password successfully changed', 'error')
            return render_template('login.html')
        return redirect(url_for('auth.Cpassword'))
    return render_template('change_password.html')