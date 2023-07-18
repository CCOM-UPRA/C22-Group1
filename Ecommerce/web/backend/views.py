from flask import Blueprint, redirect, url_for, render_template, request, flash
from ..controllers.backend.accountController import *

views = Blueprint('back_views', __name__, template_folder='templates/')


@views.route('/')
@views.route('/clear')
def clear():
    return redirect(url_for('back_views.products'))


@views.route('/products')
def products():
    return render_template('products.html')


@views.route('/addproduct')
def addproduct():
    return render_template('add_product.html')


@views.route('/accounts')
def accounts():
    users = UsersList()
    return render_template('accounts.html' , user = users)

@views.route('/edit_accounts', methods=['GET', 'POST'])
def edit_accounts():
    if request.method == 'POST':
       fname = request.form['F_Name']
       lname = request.form['L_Name'] 
       pass1 = request.form['Password']
       email = request.form['Email']
       phone = request.form['Phone']
       status = request.form['selected_status']
       id = request.form['A_id']
       update_account(fname, lname, pass1, email, phone, status, id)
       flash('The account have been edited ', 'succes')
    return redirect(url_for('back_views.accounts'))

@views.route('/add_accounts', methods=['GET', 'POST'])
def add_accounts():
    if request.method == 'POST':
        fname = request.form['F_Name']
        lname = request.form['L_Name']
        email = request.form['Email']
        pass1 = request.form['Password']
        pass2 = request.form['Password2']
        addaccount(fname,lname,email,pass1,pass2)
        flash('The new account have been added', 'succes')
    return redirect(url_for('back_views.accounts'))


@views.route('/reports')
def reports():
    return render_template('reports.html')


@views.route('/profile')
def profile():
    return render_template('profile.html')
