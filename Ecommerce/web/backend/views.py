from flask import Blueprint, redirect, url_for, render_template, request, flash
from ..controllers.backend.accountController import *
from ..models.backend.reportmodel import *
from ..controllers.frontend.shopController import *
from ..models.backend.productModel import *
import calendar
from datetime import datetime, timedelta

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'customer' not in session:
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
        print(tname,tprice,tcost,tbrand,tdesc,timage,tstock,tstatus,ttype,tmount,tfocal,taperture)
        # new_product(tname,tprice,tcost,tbrand,tdesc,timage,tstock,tstatus,ttype,tmount,tfocal,taperture)
    return render_template('add_product.html')


@views.route('/accounts')
@login_required
def accounts():
    users = UsersList()
    return render_template('accounts.html' , user = users)

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
        addaccount(fname,lname,email,pass1,pass2)
        flash('The new account have been added', 'succes')
    return redirect(url_for('back_views.accounts'))

    
@views.route('/reports', methods=['GET', 'POST'])
@login_required
def reports():
    print("HOLA")
    if request.method == 'POST':
        
        report_day = request.form['report_day']
        print("HOLA")
        print(report_day)
        report_week = request.form.get('report_week')
        report_month = request.form.get('report_month')
        product = request.form.get('products')
        stock_report = request.form.get('stock_report')


        if report_day:
            # Convert the report_day string to a datetime object
            report_day = datetime.strptime(report_day, '%Y-%m-%d').date()
            # Execute the SQL query for report by day
            result = get_sales_report_by_day(report_day)
            # Process the result and render the template
            if not result:
                # No data available
                return render_template('reports.html', message="No sales report available for the selected week.")
            return render_template('reports.html', report=result)


        # elif report_week:   
        #     # Convert the report_week string to a datetisme object
        #     report_week_start = datetime.strptime(report_week + '-1', '%Y-W%W-%w')
        #     # Calculate the end of the week by adding 6 days
        #     report_week_end = report_week_start + timedelta(days=6)
        #     # Execute the SQL query for the report by week
        #     result = get_sales_report_by_week(report_week_start, report_week_end)
        #     # Process the result and render the template
        #     return render_template('reports.html', report=result)
        
        elif report_week:
            # Convert the report_week string to a datetime object
            report_week_start = datetime.strptime(report_week + '-1', '%Y-W%W-%w')
            # Calculate the end of the week by adding 6 days
            report_week_end = report_week_start + timedelta(days=6)
            # Execute the SQL query for the report by week
            result = get_sales_report_by_week(report_week_start, report_week_end)
            # Process the result and render the template
            
            if not result:
                # No data available
                return render_template('reports.html', message="No sales report available for the selected week.")
                print(message)
            return render_template('reports.html', report=result)
            
        elif report_month:
            # Convert the report_month string to a datetime object
            report_month_start = datetime.strptime(report_month, '%Y-%m')
            # Calculate the start and end dates for the month
            report_month_start = report_month_start.replace(day=1)
            report_month_end = report_month_start.replace(day=calendar.monthrange(report_month_start.year, report_month_start.month)[1])

            # Execute the SQL query for the report by month
            result = get_sales_report_by_month(report_month_start.strftime('%Y-%m-%d'), report_month_end.strftime('%Y-%m-%d'))
            # Process the result and render the template
            return render_template('reports.html', report=result)
            
        elif product:
            # Execute the SQL query for report by product
            result = get_sales_report_by_product(product)
            # Process the result for rendering
            

                # Perform any additional data processing or formatting as needed
                # Create a dictionary to store the processed data
               
            # Render the template with the processed data
            return render_template('report.html', inventory=result)
        
        elif stock_report:
            # Execute the SQL query for inventory report
            result = get_inventory_report()
            # Process the result for rendering
            inventory_data = []
            for row in result:
                telescope_name = row[0]
                total_quantity = row[1]
                # Perform any additional data processing or formatting as needed
                # Create a dictionary to store the processed data
                inventory_data.append({
                    'telescope_name': telescope_name,
                    'total_quantity': total_quantity
                })
            # Render the template with the processed data
            return render_template('report.html', inventory_data=inventory_data)

    return render_template('reports.html')