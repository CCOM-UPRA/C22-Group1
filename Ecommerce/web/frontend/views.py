from flask import Blueprint, render_template, request, redirect, url_for, session, Flask, flash
from functools import wraps
from ..models.frontend.loginModel import *
from ..controllers.frontend.shopController import *
from ..models.frontend.profileModel import *


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
    telescopes = Telescopes()
    brands = Brands()
    mounts = Mounts()
    lenses = Lenses()
    focalDistance = FocalDistance()
    aperture = Aperture()
    print(telescopes)
    return render_template('shop.html',
                           products=telescopes,
                           brands=brands,
                           mounts=mounts,
                           Lenses=lenses,
                           aperture=aperture,
                           focal_distance=focalDistance)


@views.route('/profile')
@login_required
def profile():
    id = session.get('customer')
    user = user_info(id)
    cards = card_info(id)
    return render_template('profile.html', 
                           user1=user,
                           card = cards)


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
            flash('ACCOUNT INFO EDITED', 'EDITED')
        elif form_name == 'form2':
            Street_name = request.form['aline2']
            Street_number = request.form['aline1']
            city = request.form['city']
            state = request.form['state']
            zipcode = request.form['zipcode']
            edit_address(id, Street_number, Street_name, zipcode, city, state)
            flash('ADDRESS INFO EDITED', 'EDITED')
        elif form_name == 'form3':
            number = request.form['number']
            edit_phone(id,number)
            flash('PHONE NUMBER EDITED', 'EDITED')
        elif form_name == 'form4':
            c_number = request.form['selected_card']
            c_name = request.form['card_name']
            c_type = request.form['card_type']
            c_date = request.form['date']
            year,month = c_date.split('-')
            c_id = request.form['card_id']
            update_payment(c_number, c_name, c_type, year, month,c_id) 
            flash('PAYMENT INFO EDITED', 'EDITED')
    return redirect(url_for('views.profile'))


@views.route('/deletecard', methods=['GET', 'POST'])
@login_required
def deletecard():
    c_number = request.form['selected_card']
    delete_card(c_number)
    flash('PAYMENT CARD DELETED', 'EDITED')
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


@views.route('/payment', methods=['GET', 'POST'])
@login_required
def payment():
    if request.method == 'POST':
        id = session.get('customer')
        Cname = request.form['Card_Name']
        Cnumber = request.form['Card_Number']
        Ctype = request.form['card_type']
        Cdate = request.form['Card_date']
        year,month = Cdate.split('-')
        Ccvv = request.form['Card_cvv']
        Czipcode = request.form['Card_zipcode']
        insert_card(id, Cname, Ctype, Cnumber, month, year, Ccvv, Czipcode)
        flash('NEW PAYMENTH INFO ADDED', 'ADDED')
    return redirect(url_for('views.profile'))


@views.route('/change_password', methods=['POST'])
@login_required
def change_password():
    id = session.get('customer')
    old = old_password(id)[0]
    password = request.form['C_Password']
    password2 = request.form['pass_n']
    password3 = request.form['pass_n1']
    
    
    if old != password:
        flash('The password you entered is not the old one you had', 'error')
        return redirect(url_for('views.profile'))
    
    if old == password2:
        flash('Your new password is the same as the old one.', 'error')
        return redirect(url_for('views.profile'))
    
    if password2 != password3:
        flash('Your new password and the confirmation dont match', 'error')
        return redirect(url_for('views.profile'))
    
    update_password(id, password2) 
    flash('Password updates', 'ADDED')
    return redirect(url_for('views.profile'))