import calendar
from datetime import datetime, timedelta
import datetime
from flask import Blueprint, render_template, redirect, url_for, request, Flask
from ..models.backend.reportmodel import *

views = Blueprint('back_views', __name__, template_folder='templates/')


@views.route('/')
@views.route('/clear')
def clear():
    return redirect(url_for('back_views.products'))


@views.route('/products')
def products():
    return render_template('products.html')


@views.route('/addproduct')
def addproduct():
    return render_template('add_product.html')


@views.route('/accounts')
def accounts():
    return render_template('accounts.html')


    
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
            
    return render_template('reports.html',products=products)


        

@views.route('/profile')
def profile():
    
    
    
    return render_template('profile.html')
