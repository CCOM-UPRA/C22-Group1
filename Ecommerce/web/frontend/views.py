from flask import Blueprint, render_template, request, redirect, url_for, session, Flask
from functools import wraps
from ..dbConnection import *
from ..models.frontend.loginModel import *


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'customer' not in session:
            return redirect('/')
        return func(*args, **kwargs)
    return wrapper


views = Blueprint('views', __name__, template_folder='templates/')


@views.route('/')
@views.route('/clear', methods=['GET', 'POST'])
def clear():
    return redirect(url_for('views.shop'))


@views.route('/shop', methods=['GET', 'POST'])
def shop():
    return render_template('shop.html')


@views.route('/profile')
@login_required
def profile():
    id = session.get('customer')
    user = user_info(id)
    return render_template('profile.html', user1=user)


@views.route('/editinfo', methods=['GET', 'POST'])
@login_required
def editinfo():
    if request.method == 'POST':
        form_name = request.form.get('form_name')
        id = session.get('customer')
        if form_name == 'form1':
            fname = request.form['C_fname']
            lname = request.form['C_lname']
            email = request.form['C_email']
            edit_prof(id, fname ,lname ,email)
        elif form_name == 'form2':
            Street_name = request.form['aline2']
            Street_number = request.form['aline1']
            city = request.form['city']
            state = request.form['state']
            zipcode = request.form['zipcode']
            edit_address(id, Street_number, Street_name, zipcode, city, state)
        elif form_name == 'form3':
            number = request.form['number']
            edit_phone(id,number)
    return redirect(url_for('views.profile'))


@views.route('/orders')
@login_required
def orders():
    return render_template('orderlist.html', order1=[], order2=[], products1=[], products2=[])


@views.route('/addcart')
@login_required
def addcart():
    pass


@views.route('/deletecart')
@login_required
def deletecart():
    pass


@views.route('/editcart')
@login_required
def editcart():
    pass


@views.route('/checkout')
@login_required
def checkout():
    return render_template('checkout.html', user1=[])


@views.route('/invoice')
@login_required
def invoice():
    return render_template('invoice.html', order=[], products=[])
