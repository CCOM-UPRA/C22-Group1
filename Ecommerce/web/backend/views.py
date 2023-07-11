
import calendar
from datetime import datetime, timedelta
#from ..controllers.backend.reportController import *

from flask import Blueprint, render_template, redirect, url_for, request,Flask
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


    
@views.route('/reports', methods=['GET', 'POST'])
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

@views.route('/profile')
def profile():
    
    
    
    return render_template('profile.html')
