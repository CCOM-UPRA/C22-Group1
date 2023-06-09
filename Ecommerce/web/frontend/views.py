from flask import Blueprint, render_template, request, redirect, url_for, session
from functools import wraps
from ..dbConnection import *


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
    user = []
    return render_template('profile.html', user1=user)


@views.route('/editinfo')
@login_required
def editinfo():
    pass


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
