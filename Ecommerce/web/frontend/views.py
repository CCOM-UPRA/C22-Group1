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


@views.route('/shop')
def shop():
    cartProducts = []
    if 'customer' in session:
        if 'cart' not in session:
            Cart()
        getCartTotal()
        cartProducts = getCartItems()
    
    telescopes = []
    if 'filters' in session:
        telescopes = FilteredTelescopes()
    else:
        telescopes = Telescopes()
    brands = Brands()
    mounts = Mounts()
    lenses = Lenses()
    focalDistance = FocalDistance()
    aperture = Aperture()
    return render_template('shop.html',
                           products=telescopes,
                           brands=brands,
                           mounts=mounts,
                           Lenses=lenses,
                           aperture=aperture,
                           focal_distance=focalDistance,
                           CartItems = cartProducts)
    

@views.route('/filter', methods = ['GET', 'POST'])
def filter():
    if request.method == 'POST':
        checkedBrands = request.form.getlist('brand')
        checkedFocalDistance = request.form.getlist('focal_distance')
        checkedAperture = request.form.getlist('aperture')
        checkedLens = request.form.getlist('lens')
        checkedMount = request.form.getlist('mount')
        print(checkedBrands)
        session['filters'] = [checkedBrands, checkedFocalDistance, checkedAperture, checkedLens, checkedMount]
    return redirect(url_for('views.shop'))

@views.route('clearFilters', methods = ['GET', 'POST'])
def clearFilters():
    if request.method == 'POST':
        if 'filters' in session:
            session.pop('filters')
    return redirect(url_for('views.shop'))


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


@views.route('/addcart', methods = ['GET', 'POST'])
@login_required
def addcart():
    if request.method == 'POST':
        productQuantity = request.form['quantity']
        productID = request.form['p_id']
        
        addToCart(productID, productQuantity)
    return redirect(url_for('views.shop'))

@views.route('/addcartModal', methods = ['GET', 'POST'])
@login_required
def addcartModal():
    if request.method == 'POST':
        productQuantity = request.form['quantity']
        productID = request.form['p_idModal']
        
        addToCart(productID, productQuantity)
    return redirect(url_for('views.shop'))


@views.route('/deletecart', methods = ['GET', 'POST'])
@login_required
def deletecart():
    if request.method == 'POST':
        productID = request.form['itemId']
        deleteFromCart(productID)
    return redirect(url_for('views.shop'))


@views.route('/editcart', methods = ['GET', 'POST'])
@login_required
def editcart():
    if request.method == 'POST':
        productId = request.form['id']
        newQuantity = int(request.form['cartQuantity'])
        updateCart(productId, newQuantity)
    return redirect(url_for('views.shop'))


@views.route('/checkout')
@login_required
def checkout():
    return render_template('checkout.html', user1=[])


@views.route('/invoice')
@login_required
def invoice():
    return render_template('invoice.html', order=[], products=[])
