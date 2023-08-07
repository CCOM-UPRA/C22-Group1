from flask import Blueprint, redirect, url_for, render_template, request, flash
from ..controllers.backend.accountController import *
from ..models.backend.reportmodel import *
from ..controllers.frontend.shopController import *
from ..models.backend.productModel import *
from ..controllers.backend.productsController import *
from ..models.backend.reportmodel import *
from ..controllers.backend.orderController import *
import datetime
import hashlib


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
    products = back_Telescope()
    print(products)
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
        old = request.form['oldPassword']
        email = request.form['Email']
        phone = request.form['Phone']
        status = request.form['selected_status']
        id = request.form['A_id']
        if(fname != '' and lname != '' and email != '' and status != '' and id != ''):
            if(pass1 != ''):
                password_hash = hashlib.sha256(pass1.encode()).hexdigest()
                update_account(fname, lname, password_hash, email, phone, status, id)
                flash('The account have been edited new ', 'succes')
            else:
                update_account(fname, lname, old, email, phone, status, id)
                flash('The account have been edited old ', 'succes')
        
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
            if pass1 != pass2:
                flash('Password dont match', 'error')
            elif email_exists(email):
                flash('Email already exists!', 'error')
            else:
                flash('The New Account Have Been Added', 'succes')
                password_hash = hashlib.sha256(pass2.data.encode()).hexdigest()
                insert_user(fname, lname, email, password_hash)
        else:
            flash('Fill all the blanks', 'error')
    return redirect(url_for('back_views.accounts'))

    
@views.route('/reports', methods =['GET', 'POST'])
def reports():
    products = prod_name()
    if request.method == 'POST':
        
        form_name = request.form.get('form_name')
        
        if form_name == 'form1': #form1 para reporte diario de ordenes
            report_day = request.form['report_day']
            # Check if report_day are provided
            if not report_day:
                return render_template('reports.html', message="Please select a date.")
            
            result = get_sales_report_by_day(report_day)
            if not result:
                # No data available
                return render_template('report.html', message="No sales report available for the selected day.")
            return render_template('report.html', report=result)
        elif form_name == 'form2': #form2 para reporte semanal de ordenes
            report_week = request.form['report_week']
            # Check if report_week are provided
            if not report_week:
                return render_template('reports.html', message="Please select a week.")
            
            year, week_number = datetime.datetime.strptime(report_week + '-1', "%Y-W%W-%w").isocalendar()[0:2]

            # Calculate start date
            start_date = datetime.datetime.strptime(f'{year}-W{week_number}-1', "%Y-W%W-%w").date()

            # Calculate end date
            end_date = start_date + datetime.timedelta(days=6)
            result = get_sales_report_by_week(start_date,end_date)
            
            if not result:
                # No data available
                return render_template('report.html', message="No sales report available for the selected week.")
            return render_template('report.html', report=result)
        elif form_name == 'form3': #form para reporte mensual de ordenes
            report_month = request.form['report_month']
             # Check if report_month are provided
            if not report_month:
                return render_template('reports.html', message="Please select a week.")
             # Convert report_month to a datetime object
            report_date = datetime.datetime.strptime(report_month, "%Y-%m")

    # Calculate the start and end dates of the report month
    
            report_month_start = report_date.replace(day=1)
            next_month = report_month_start.replace(day=28) + datetime.timedelta(days=4)
            report_month_end = next_month - datetime.timedelta(days=next_month.day)
            result = get_sales_report_by_month(report_month_start,report_month_end)

            if not result:               
                # No data available
                return render_template('report.html', message="No sales report available for the selected month.")
            return render_template('report.html', report=result)
        
        elif form_name == 'form5':
            # inventory report
            result = get_inventory_report()
            
            if not result:
                return render_template('report.html',message="No Inventory report")
            return render_template('inventory_report.html', inventory_data=result)  
                
            # Render the template with the processed data
            #product = request.form.get('products')
        elif form_name == 'form6': 
            product = request.form.get('products')
            selected_date = request.form.get('day_report')
            
            # Check if both product and report_week are provided
            if not product or not selected_date:
                return render_template('reports.html', products=products, message="Please select both a telescope and a date.")
                      
        # Llama a la función get_prodid con la fecha seleccionada y el producto
            result = get_prodid(product, selected_date) 
            
            if not result:
                    return render_template('report.html',message="No products available")
            
            return render_template('report.html',report = result)
        
        elif form_name == 'form7': #reporte semanal producto especifico 
            
            product = request.form.get('products') 
            report_week = request.form.get('week_report')
            # Check if both product and report_week are provided
            if not product or not report_week:
                return render_template('reports.html', products=products, message="Please select both a telescope and a date.")
            
              # Extract the year and week number separately
            year, week_number = report_week.split('-')
            year, week_number = int(year), int(week_number[1:])  # Remove the 'W' prefix from week_number

            # Calculate start date based on the year and week number
            start_date = datetime.datetime.strptime(f'{year}-W{week_number}-1', "%Y-W%W-%w").date()

            # Calculate end date
            end_date = start_date + datetime.timedelta(days=6)
            
            result = sales_report_by_week(product, start_date, end_date)
            if not result:
                    return render_template('report.html',message="No products available")
        
            return render_template('report.html',report = result)
    
        elif form_name == 'form8':
            
            product = request.form.get('products') 
            report_month = request.form.get('month_report')
            
            
            # Check if both product and report_month are provided
            if not product or not report_month:
                return render_template('reports.html', products=products, message="Please select both a telescope and a date.")
            
            
            # Extract the year and month separately
            year, month = report_month.split('-')
            year, month = int(year), int(month)

            # Calculate start date and end date for the month
            start_date = datetime.date(year, month, 1)
            last_day = 31 if month != 2 else 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28
            end_date = datetime.date(year, month, last_day)
            
            result = sales_report_by_month(product, year, month)
            
            if not result:
                return render_template('report.html', message="No products available")
        
            return render_template('report.html', report=result)
        
        
        elif form_name == 'form9':
            result = earningreport()    
            earning = totalearningreport()
            return render_template('earningsreport.html', result=result,earning = earning)  
            
    return render_template('reports.html',products=products)


@views.route('/profile')
def profile():
    return render_template('profile2.html', user1 = [])

@views.route('/viewOrders')
def viewOrders():
    orders = getAllOrdersItems()
    orderType = ['all', 'received', 'processed', 'shipped', 'delivered']
    orderType2 = ['Received', 'Processed', 'Shipped', 'Delivered']
    
    if 'BacklastSelectOrderType' in session:
        lastType = session['BacklastSelectOrderType']
        index = orderType.index(lastType)
        orderType.pop(index)
        orderType.insert(0, lastType)
    
    order_count = getOrderCount()
    return render_template("ordersviews.html", 
                           orders = orders, 
                           totalOrders = order_count, 
                           orderType = orderType,
                           orderType2 = orderType2)

@views.route('editOrder', methods = ['GET', 'POST'])
def editOrder():
    if request.method == 'POST':
        date = request.form['Arrival-date']
        prevDate = request.form['PrevArrival']
        status = request.form['Order-status']
        prevStatus = request.form['PrevStatus']
        tracking = request.form['TrackingNumber']
        id = request.form['OrderId']
        
        orderUpdate(id, date, prevDate, status, prevStatus, tracking)
    return redirect(url_for('back_views.viewOrders'))

@views.route('/filterOrders', methods = ['GET','POST'])
def filterOrders():
    if request.method == 'POST':
        selected = request.form['status']

        if selected == 'all':
            if 'BackfilterStatus' in session:
                session.pop('BackfilterStatus')
        else:
            session['BackfilterStatus'] = selected
        
        session['BacklastSelectOrderType'] = selected
        
    return redirect(url_for('back_views.viewOrders'))
