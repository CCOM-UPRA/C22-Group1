from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from .controlers.usercontroler import *
from .controlers.productsControler import *
from .controlers.ordersControler import *
from .controlers.cartcontroler import *
from .controlers.paymentController import *
from .controlers.customerOrderControler import *
import json

views = Blueprint('views', __name__, template_folder='templates/client/')


@views.route('/')
@views.route('/shop', methods=['GET', 'POST'])
def shop():
    telescopes = getAllTelescopes()
    brands = getAllBrands()
    price = [getMinPrice()[0], getMaxPrice()[0]]
    lens = getAllLensType()
    focal_distance = [getMinFocalDistance()[0], getMaxFocalDistance()[0]]
    aperture = [getMinAperture()[0], getMaxAperture()[0]]
    mounts = getAllMounts()
    cart = None
    cart_items = None
    total = 0

    if current_user.is_authenticated:
        cart = getCart()
        cart_items = json.loads(cart.items)
        total = float(cart.total_price)

    if request.method == 'POST':
        price = [request.form.get('minPrice'), request.form.get('maxPrice')]
        focal_distance = \
            [request.form.get('minFocal_distance'),
             request.form.get('maxFocal_distance')]
        aperture = [request.form.get('minAperture'),
                    request.form.get('maxAperture')]
        checkedBrands = request.form.getlist('brand')
        checkedLens = request.form.getlist('lens')
        checkedMount = request.form.getlist('mount')

        if aperture[0] == '':
            aperture[0] = getMinAperture()[0]

        if aperture[1] == '':
            aperture[1] = getMaxAperture()[0]

        if focal_distance[0] == '':
            focal_distance[0] = getMinFocalDistance()[0]

        if focal_distance[1] == '':
            focal_distance[1] = getMaxFocalDistance()[0]

        if price[0] == '':
            price[0] = getMinPrice()[0]

        if price[1] == '':
            price[1] = getMaxPrice()[0]
        telescopes = filterTelesopes(price=price,
                                     focal_distance=focal_distance,
                                     aperture=aperture,
                                     brands=checkedBrands,
                                     lens=checkedLens,
                                     mounts=checkedMount)

    return render_template('shop.html', user=current_user,
                           telescopes=telescopes,
                           brands=brands,
                           price=price,
                           Lens=lens,
                           focal_distance=focal_distance,
                           aperture=aperture,
                           mounts=mounts,
                           cart=cart,
                           items=cart_items,
                           total=total)


@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    cart = None
    cart_items = None
    total_items = None
    name = getCardName()
    number = getCardNumber()
    type = getCardType()
    month = getMonth()
    year = getYear()
    
    cart = getCart()
    cart_items = json.loads(cart.items)
    total = float(cart.total_price)
 
        
    
    if request.method == "POST":    
        fname = request.form.get('fname')
        if fname == None:
            fname = User.Fname
        else:    
            dataBase.session.execute(text(f"UPDATE user SET Fname = '{fname}' WHERE id = {current_user.id}"))
          
        lname = request.form.get('lname')
        if lname == None:
            lname = User.Lname
        else:    
            dataBase.session.execute(text(f"UPDATE user SET Lname = '{fname}' WHERE id = {current_user.id}"))
          
        email = request.form.get('email')
        if email == None:
            email = User.Email
        else:    
            dataBase.session.execute(text(f"UPDATE User SET Email = '{email}' WHERE id = {current_user.id}"))
        
        number = request.form.get('number')
        if number == None:
            number = User.Phone
        else:    
            dataBase.session.execute(text(f"UPDATE user SET Phone = '{number}' WHERE id = {current_user.id}"))
            
        aline1 = request.form.get('aline1')
        if aline1 == None:
            aline1 = User.Address
        else:
            dataBase.session.execute(text(f"UPDATE user SET Address = '{aline1}' WHERE id = {current_user.id}"))
            
        aline2 = request.form.get('aline2')
        if aline2 == None:
            aline2 = User.Street
        else:
            dataBase.session.execute(text(f"UPDATE user SET Street = '{aline2}' WHERE id = {current_user.id}"))
        
        city = request.form.get('city')
        if city == None:
            city = User.City
        else:
            dataBase.session.execute(text(f"UPDATE user SET City = '{city}' WHERE id = {current_user.id}"))
            
        state = request.form.get('state')
        if state == None:
            state = User.State
        else:
            dataBase.session.execute(text(f"UPDATE user SET State = '{state}' WHERE id = {current_user.id}"))
            

        zipcode = request.form.get('zipcode')
        if zipcode == None:
            zipcode = User.ZipCode
        else:
            dataBase.session.execute(text(f"UPDATE user SET ZipCode = '{zipcode}' WHERE id = {current_user.id}"))
            
            
        
        cname = request.form.get('card_name')
        if cname == None:
            cname = getCardName()
        else:
            dataBase.session.execute(text(f"UPDATE payment SET name = '{cname}' WHERE id = {current_user.id}"))

        ctype = request.form.get('card_type')
        if ctype == None:
            ctype = getCardType()
        else:
            dataBase.session.execute(text(f"UPDATE payment SET type = '{ctype}' WHERE id = {current_user.id}"))

        cnumber = request.form.get('card_num')
        if cnumber == None:
            cnumber = getCardNumber
        else:
            dataBase.session.execute(text(f"UPDATE payment SET number = '{cnumber}' WHERE id = {current_user.id}"))

        month = request.form.get('month')
        if month == None:
            month = getMonth()
        else:
            dataBase.session.execute(text(f"UPDATE payment SET month = '{month}' WHERE id = {current_user.id}"))
        
        year = request.form.get('year')
        if year == None:
            year = getYear()
        else:
            dataBase.session.execute(text(f"UPDATE payment SET year = '{year}' WHERE id = {current_user.id}"))


        dataBase.session.commit()        
        return redirect(url_for('views.profile'))


    return render_template('profile.html', user = current_user,
                           cart = cart,
                           items = cart_items,
                           total_items = total_items,
                           name = name, 
                           number = number,
                           type = type,
                           month = month,
                           year = year
                           )


@views.route('/orders', methods=['GET', 'POST'])
@login_required
def orders():
    orders = getAllOrders()
    order_id = getorderid()
    tracking_num = get_trackingnum()
    total = 1
    
    
    
    cart = getCart()
    cart_items = json.loads(cart.items)
    total = float(cart.total_price)
 

    return render_template('orders.html', user=current_user,
                           orders=orders,
                           order_id=order_id,
                           tracking_num=tracking_num,
                           total=total,
                           cart = cart,
                           cart_items = cart_items)


@views.route('/checkout',  methods=['GET', 'POST'])
@login_required
def checkout():
    cart = None
    cart_items = None
    total_items = None
  
    cart = getCart()
    cart_items = json.loads(cart.items)
    total = float(cart.total_price)

        
    name = getCardName()
    number = getCardNumber()
    type = getCardType()
    month = getMonth()
    year = getYear()
    
    
    if request.method == "POST":    
        fname = request.form.get('fname')
        if fname == None:
            fname = User.Fname
        else:    
            dataBase.session.execute(text(f"UPDATE user SET Fname = '{fname}' WHERE id = {current_user.id}"))
            
        lname = request.form.get('lname')
        if lname == None:
            lname = User.Lname
        else:    
            dataBase.session.execute(text(f"UPDATE user SET Lname = '{fname}' WHERE id = {current_user.id}"))
            
        email = request.form.get('email')
        if email == None:
            email = User.Email
        else:    
            dataBase.session.execute(text(f"UPDATE user SET Email = '{email}' WHERE id = {current_user.id}"))
        
        number = request.form.get('number')
        if number == None:
            number = User.Phone
        else:    
            dataBase.session.execute(text(f"UPDATE user SET Phone = '{number}' WHERE id = {current_user.id}"))
            
        aline1 = request.form.get('aline1')
        if aline1 == None:
            aline1 = User.Address
        else:
            dataBase.session.execute(text(f"UPDATE user SET Address = '{aline1}' WHERE id = {current_user.id}"))
            
        aline2 = request.form.get('aline2')
        if aline2 == None:
            aline2 = User.Street
        else:
            dataBase.session.execute(text(f"UPDATE user SET Street = '{aline2}' WHERE id = {current_user.id}"))
        
        city = request.form.get('city')
        if city == None:
            city = User.City
        else:
            dataBase.session.execute(text(f"UPDATE user SET City = '{city}' WHERE id = {current_user.id}"))
            
        state = request.form.get('state')
        if state == None:
            state = User.State
        else:
            dataBase.session.execute(text(f"UPDATE user SET State = '{state}' WHERE id = {current_user.id}"))
            

        zipcode = request.form.get('zipcode')
        if zipcode == None:
            zipcode = User.ZipCode
        else:
            dataBase.session.execute(text(f"UPDATE user SET ZipCode = '{zipcode}' WHERE id = {current_user.id}"))
            
            
        
        cname = request.form.get('card_name')
        if cname == None:
            cname = getCardName()
        else:
            dataBase.session.execute(text(f"UPDATE payment SET name = '{cname}' WHERE id = {current_user.id}"))

        ctype = request.form.get('card_type')
        if ctype == None:
            ctype = getCardType()
        else:
            dataBase.session.execute(text(f"UPDATE payment SET type = '{ctype}' WHERE id = {current_user.id}"))

        cnumber = request.form.get('card_num')
        if cnumber == None:
            cnumber = getCardNumber
        else:
            dataBase.session.execute(text(f"UPDATE payment SET number = '{cnumber}' WHERE id = {current_user.id}"))

        month = request.form.get('month')
        if month == None:
            month = getMonth()
        else:
            dataBase.session.execute(text(f"UPDATE payment SET month = '{month}' WHERE id = {current_user.id}"))
        
        year = request.form.get('year')
        if year == None:
            year = getYear()
        else:
            dataBase.session.execute(text(f"UPDATE payment SET year = '{year}' WHERE id = {current_user.id}"))


        dataBase.session.commit()        
        return redirect(url_for('views.checkout'))


    
    return render_template('checkout.html', user = current_user,
                            cart = cart,
                            items = cart_items,
                            total_items = total_items,
                            name = name,
                            number = number,
                            type = type,
                            month = month,
                            year = year )


@views.route('/invoice', methods=['GET', 'POST'])
@login_required
def invoice():
    cart = getCart()
    cart_items = json.loads(cart.items)
    total = float(cart.total_price)
    tracking_number = get_trackingnum()
    order_date = getOrderDate()
    total_amount = 100
    payment_method = "credit card"
   
    cart = getCart()
    cart_items = json.loads(cart.items)
    total = float(cart.total_price)


    return render_template('invoice.html', user=current_user,
                           orders=orders,
                           cart=cart,
                           items=cart_items,
                           total=total,
                           tracking_number = tracking_number,
                           order_date = order_date,
                           total_amount = total_amount,
                           payment_method = payment_method
                           )


@login_required
@views.route('/addToCart', methods=['GET', 'POST'])
def addToCart():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        id = request.form.get('p_id')
        image = request.form.get('image')
        brand = request.form.get('brand')
        item = {
            'id': int(id),
            'name': name,
            'price': int(price),
            'brand': brand,
            'image': image
        }
        quantity = request.form.get('quantity')
        itemToAdd = {
            'quantity': int(quantity),
            'product': item
        }
        incertToCart(itemToAdd)
        return redirect(url_for('views.shop'))


@login_required
@views.route('/deleteFromCart/<itemid>')
def deleteFromCart(itemid):
    deleteItem(itemid)
    return redirect(url_for('views.shop'))


@login_required
@views.route('/editCart<itemid>', methods=['GET', 'POST'])
def editItemInCart(itemid):
    if request.method == 'POST':
        newValue = request.form.get('quantity')
        print(newValue)
        editCart(itemid, newValue)
    return redirect(url_for('views.shop'))
