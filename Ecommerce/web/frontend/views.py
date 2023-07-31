from flask import Blueprint, render_template, request, redirect, url_for, session, Flask, flash
from functools import wraps
from ..models.frontend.loginModel import *
from ..models.frontend.orderModel import *
from ..controllers.frontend.shopController import *
from ..controllers.frontend.orderController import *
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

# @views.route('/reports', methods=['GET', 'POST'])
# def inv_rep():
#     inventario = reports()
    
#     return render_template('inventory_report.html',reportes = inventario)


@views.route('/shop')
def shop():
    
    if 'cardId' in session:
        session.pop('cardId')
    
    cartProducts = []
    if 'customer' in session:
        if 'cart' not in session:
            Cart()
        getCartTotal()
        cartProducts = getCartItems()
    
    if 'minPrice' not in session:
        setPriceRange()
    
    telescopes = []
    if 'filters' in session:
        telescopes = FilteredTelescopes()
    elif 'searchString' in session:
        telescopes = SearchBar()
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

@views.route('/filterOrders', methods = ['GET','POST'])
def filterOrders():
    if request.method == 'POST':
        selected = request.form['status']

        if selected == 'all':
            if 'filterStatus' in session:
                session.pop('filterStatus')
        else:
            session['filterStatus'] = selected
        
        session['lastSelectOrderType'] = selected
        
    return redirect(url_for('views.orders'))

@views.route('/clearError/<Origin>')
def clearError(Origin):
    if 'CartMaxError' in session:
        session.pop('CartMaxError')
    if 'cardError' in session:
        session.pop('cardError')
    
    if Origin == 'shop':
        return redirect(url_for('views.shop'))
    elif Origin == 'profile':
        return redirect(url_for('views.profile'))
    elif Origin == 'orders':
        return redirect(url_for('views.orders'))
    elif Origin == 'checkout':
        return redirect(url_for('views.checkout'))


@views.route('/filter', methods = ['GET', 'POST'])
def filter():
    if request.method == 'POST':
        checkedBrands = request.form.getlist('brand')
        checkedFocalDistance = request.form.getlist('focal_distance')
        checkedAperture = request.form.getlist('aperture')
        checkedLens = request.form.getlist('lens')
        checkedMount = request.form.getlist('mount')
        session['filters'] = [checkedBrands, checkedFocalDistance, checkedAperture, checkedLens, checkedMount]
    return redirect(url_for('views.shop'))

@views.route('filterBySearch', methods = ['GET', 'POST'])
def filterBySearch():
    if request.method == 'POST':
        searchString = request.form['searchBar']
        if len(searchString) > 0:
            session['searchString'] = searchString
        else:
            if 'searchString' in session:
                session.pop('searchString')
    return redirect(url_for('views.shop'))

@views.route('clearFilters', methods = ['GET', 'POST'])
def clearFilters():
    if request.method == 'POST':
        if 'filters' in session:
            session.pop('filters')
    return redirect(url_for('views.shop'))

@views.route('UpdatePriceRange', methods = ['GET', 'POST'])
def UpdatePriceRange():
    if request.method == 'POST':
        newMinPrice = request.form['minPrice']
        newMaxPrice = request.form['maxPrice']
        
        if newMinPrice.isalpha() or len(newMinPrice) == 0:
            newMinPrice = session['minPrice']
        else:
            newMinPrice = int(newMinPrice)
        
        if newMaxPrice.isalpha() or len(newMaxPrice) == 0:
            newMaxPrice = session['maxPrice']
        else:
            newMaxPrice = int(newMaxPrice)
            
        updatePriceRange(newMinPrice, newMaxPrice)
    return redirect(url_for('views.shop'))

@views.route('ResetPriceRange', methods = ['GET', 'POST'])
def ResetPriceRange():
    if request.method == 'POST':
        setPriceRange()
    return redirect(url_for('views.shop'))


@views.route('/profile')
@login_required
def profile():
    
    if 'cart' not in session:
        Cart()
    getCartTotal()
    cartProducts = getCartItems()
    
    id = session.get('customer')
    user = user_info(id)
    cards = card_info(id)
    return render_template('profile.html', 
                           user1=user,
                           card = cards,
                           CartItems = cartProducts)


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

@views.route('/editinfoCheckout', methods=['GET', 'POST'])
@login_required
def editinfoCheckout():
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
        elif form_name == 'form4':
            c_number = request.form['selected_card']
            c_name = request.form['card_name']
            c_type = request.form['card_type']
            c_date = request.form['date']
            year,month = c_date.split('-')
            update_payment(c_number, c_name, c_type, year, month) 
    return redirect(url_for('views.checkout'))

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
    cartProducts = []
    if 'customer' in session:
        if 'cart' not in session:
            Cart()
        getCartTotal()
        cartProducts = getCartItems()
        telescopes = Telescopes()
        
    orderType = ['all', 'recived', 'processed', 'shipped', 'delivered']
    
    if 'lastSelectOrderType' in session:
        lastType = session['lastSelectOrderType']
        index = orderType.index(lastType)
        orderType.pop(index)
        orderType.insert(0, lastType)
        
    id = session.get('customer')
    user = user_info(id)

    allOrders = getAllOrdersItems()
    totalOrders = order_count(id)
   

    
    
    return render_template('orderlist.html', 
                           user = user, 
                           products=telescopes,
                           CartItems = cartProducts,
                           totalOrders = totalOrders,
                           Orders = allOrders,
                           orderType = orderType
                           )


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
        Origin = request.form['Origin']
        deleteFromCart(productID)
        
        if Origin == 'shop':
            return redirect(url_for('views.shop'))
        elif Origin == 'profile':
            return redirect(url_for('views.profile'))
        elif Origin == 'orders':
            return redirect(url_for('views.orders'))

@views.route('/deleteCheckout', methods = ['GET', 'POST'])
@login_required
def deleteCheckout():
    if request.method == 'POST':
        productID = request.form['itemId']
        deleteFromCart(productID)
    return redirect(url_for('views.checkout'))


@views.route('/editcart', methods = ['GET', 'POST'])
@login_required
def editcart():
    if request.method == 'POST':
        productId = request.form['id']
        Origin = request.form['Origin']
        newQuantity = int(request.form['cartQuantity'])
        updateCart(productId, newQuantity)
        
        if Origin == 'shop':
            return redirect(url_for('views.shop'))
        elif Origin == 'profile':
            return redirect(url_for('views.profile'))
        elif Origin == 'orders':
            return redirect(url_for('views.orders'))

@views.route('editCheckout', methods = ['GET', 'POST'])
@login_required
def editCheckout():
    if request.method == 'POST':
        productId = request.form['p_idModal']
        newQuantity = int(request.form['quantity'])
        updateCart(productId, newQuantity)
        
    return redirect(url_for('views.checkout'))


@views.route('/checkout', methods=['GET','POST'])
@login_required
def checkout():
    if int(session['cartTotalItems']) <= 0:
        return redirect(url_for('views.shop'))
    
    id = session.get('customer')
    user = user_info(id)
    cards = card_info(id)
    
    if '' in user:
        session['UserIncomplete'] = True
    else:
        if 'UserIncomplete' in session:
            session.pop('UserIncomplete')
    
    if len(cards) == 0:
        session['NoCards'] = True
    else:
        if 'NoCards' in session:
            session.pop('NoCards')
    
    print(user)

    getCartTotal()
    cartProducts = getCartItems()
    telescopes = Telescopes()
    
    cardId = 'card'
    if 'cardId' in session:
        cardId = session['cardId']
       
    
    return render_template('checkout.html', 
                           user1=user,
                           card = cards,
                           products=telescopes,
                           CartItems = cartProducts,
                           cardId = cardId)

@views.route('saveSelectedCard', methods = ['GET', 'POST'])
def saveSelectedCard():
    if request.method == 'POST':
        cardId = request.form['cardId']
        if cardId != 'card':
            session['cardId'] = int(cardId)
            
        if 'cardError' in session:
            session.pop('cardError')
    return redirect(url_for('views.checkout'))

@views.route('procesOrder')
def procesOrder():
    if 'cardId' not in session:
        session['cardError'] = True
        return redirect(url_for('views.checkout'))
    
    customer = user_info(session['customer'])
    order_update(session['customer'], customer, order_number(), session['cardId'], session['cart'])
    session['orderTotalItems'] = session['cartTotalItems']
    session['orderTotalPrice'] = session['cartTotalPrice']
    session['lastOrder'] = session['cart']
    session['lastCardUsed'] = session['cardId']
    updateDataBaseProducts()
    return redirect(url_for('views.clearCart'))
    


@views.route('/invoice', methods=['GET','POST'])
@login_required
def invoice():
    id = session.get('customer')
    user = user_info(id)
    cardType = getCardType()
    orders = order_info(id, session['lastOrder'])
    orderProducts = getOrderItems()
    
    
    
    return render_template('invoice.html', 
                           user1=user,
                           card = cardType,
                           order = orders,
                           OrderItems = orderProducts
                          )


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
        Origin = request.form['Origin']
        insert_card(id, Cname, Ctype, Cnumber, month, year, Ccvv, Czipcode)
        flash('NEW PAYMENTH INFO ADDED', 'ADDED')
        
        if Origin == 'shop':
            return redirect(url_for('views.shop'))
        elif Origin == 'profile':
            return redirect(url_for('views.profile'))
        elif Origin == 'orders':
            return redirect(url_for('views.orders'))
        elif Origin == 'checkout':
            return redirect(url_for('views.checkout'))

@views.route('/paymentCheckout', methods=['GET', 'POST'])
@login_required
def paymentCheckout():
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
    success_message = "Contraseña actualizada con éxito."
    flash('Password updates', 'ADDED')
    return redirect(url_for('views.profile'))

@views.route('clearCart')
def clearCart():
    if 'cart' in session:
        session.pop('cart')
        session.pop('cartTotalItems')
        session.pop('cartTotalPrice')
        session.pop('cardId')
    return redirect(url_for('views.invoice'))
