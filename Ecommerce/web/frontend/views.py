from flask import Blueprint, render_template, request, redirect, url_for, session, Flask
from functools import wraps
from ..models.frontend.loginModel import *
from ..controllers.frontend.shopController import *


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
    return render_template('profile.html', user1=user)


@views.route('/editinfo', methods=['GET', 'POST'])
@login_required
def editinfo():
    if request.method == 'POST':
        id = session.get('customer')
        fname = request.form['C_fname']
        lname = request.form['C_lname']
        email = request.form['C_email']
        edit_prof(id, fname ,lname ,email)
        user = user_info(id)
    return render_template('profile.html', user1=user)


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
