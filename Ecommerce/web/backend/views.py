from flask import Blueprint, redirect, url_for, render_template, request, flash
from ..controllers.backend.accountController import *
from ..models.backend.reportmodel import *
from ..controllers.frontend.shopController import *
from ..models.backend.productModel import *
from ..controllers.backend.productsController import *
import calendar
from datetime import datetime, timedelta

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'admin' not in session:
            return redirect('/')
        return func(*args, **kwargs)
    return wrapper

views = Blueprint('back_views', __name__, template_folder='templates/')


@views.route('/')
@views.route('/clear')
def clear():
    return redirect(url_for('back_views.products'))


@views.route('/products')
@login_required
def products():
    products = Telescopes()
    return render_template('products.html', products = products)


@views.route('/addproduct', methods=['GET', 'POST'])
@login_required
def addproduct():
    if request.method == 'POST':
        tname = request.form['t_Name']
        tbrand = request.form['t_Brand']
        ttype = request.form['t_Lens']
        tmount = request.form['t_Mount']
        tfocal = request.form['t_Focal']
        tprice = request.form['t_Price']
        tstock = request.form['t_Stock']
        tdesc = request.form['t_Description']
        timage = request.form['myfile']
        tstatus = request.form['status']
        tcost = request.form['t_cost']
        taperture = request.form['t_aperture']
        if(tname !='' and tbrand !='' and ttype !='' and tmount !='' and tfocal !='' and tprice!='' and tstock!='' and tdesc!='' and timage!='' and tstatus!='' and tcost!='' and taperture!=''):
            new_product(tname,tprice,tcost,tbrand,tdesc,timage,tstock,tstatus,ttype,tmount,tfocal,taperture)
            flash('Product added to the database ', 'succes')
            return redirect(url_for('back_views.products'))
    return render_template('add_product.html')


@views.route('/edit_prod', methods=['GET', 'POST'])
@login_required
def edit_prod():
    if request.method == 'POST':
        edit = request.form['edit']
        prodID = request.form['prodId']
        if edit == 'noedit':
            products = edit_Telescope(prodID)
            return render_template('edit_prod.html', prod = products, pid = prodID)
        elif edit == 'edit':
            tname = request.form['t_Name']
            tbrand = request.form['t_Brand']
            ttype = request.form['t_Lens']
            tmount = request.form['t_Mount']
            tfocal = request.form['t_Focal']
            tprice = request.form['t_Price']
            tstock = request.form['t_Stock']
            tdesc = request.form['t_Description']
            timage = request.form['myfile']
            oldimg = request.form['oldimg']
            tstatus = request.form['status']
            tcost = request.form['t_cost']
            taperture = request.form['t_aperture']
            if(timage != ''):
                if(prodID != '' and tname !='' and tbrand !='' and ttype !='' and tmount !='' and tfocal !='' and tprice!='' and tstock!='' and tdesc!='' and tstatus!='' and tcost!='' and taperture!=''):
                    edit_product(prodID,tname,tprice,tcost,tbrand,tdesc,timage,tstock,tstatus,ttype,tmount,tfocal,taperture)
                    flash('Product has been edited ', 'succes')
            elif(oldimg != ''):
                if(prodID != '' and tname !='' and tbrand !='' and ttype !='' and tmount !='' and tfocal !='' and tprice!='' and tstock!='' and tdesc!='' and tstatus!='' and tcost!='' and taperture!=''):
                    edit_product(prodID,tname,tprice,tcost,tbrand,tdesc,oldimg,tstock,tstatus,ttype,tmount,tfocal,taperture)
                    flash('Product has been edited ', 'succes')
    return redirect(url_for('back_views.products'))
    


@views.route('/accounts', methods=['GET', 'POST'])
@login_required
def accounts():
    users = UsersList()
    return render_template('accounts.html', user = users)

@views.route('/edit_accounts', methods=['GET', 'POST'])
@login_required
def edit_accounts():
    if request.method == 'POST':
        fname = request.form['F_Name']
        lname = request.form['L_Name']
        pass1 = request.form['Password']
        email = request.form['Email']
        phone = request.form['Phone']
        status = request.form['selected_status']
        id = request.form['A_id']
        if(fname != '' and lname != '' and pass1 != '' and email != '' and status != '' and id != ''):
            update_account(fname, lname, pass1, email, phone, status, id)
            flash('The account have been edited ', 'succes')
    return redirect(url_for('back_views.accounts'))

@views.route('/add_accounts', methods=['GET', 'POST'])
@login_required
def add_accounts():
    if request.method == 'POST':
        fname = request.form['F_Name']
        lname = request.form['L_Name']
        email = request.form['Email']
        pass1 = request.form['Password']
        pass2 = request.form['Password2']
        if(fname != '' and lname != '' and pass1 != '' and pass2 !='' and email != ''):
            addaccount(fname,lname,email,pass1,pass2)
            flash('The new account have been added', 'succes')
    return redirect(url_for('back_views.accounts'))

    
@views.route('/reports', methods=['GET', 'POST'])
@login_required
def reports():
    return render_template('reports.html')