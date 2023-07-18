
from ...dbConnection import *
import sqlite3


@DBConnection
def get_sales_report_by_month(report_month_start, report_month_end, database):
    cursor = database.cursor()
    cursor.execute('''
        SELECT Order_Date, Telescope_Name, Product_Quantity, Product_Price
        FROM orders
        JOIN contains ON orders.Order_ID = contains.OrderID
        JOIN telescopes ON telescopes.TelescopeID = contains.TelescopeID
        WHERE Order_Date >= %s AND Order_Date <= %s
    ''', (report_month_start, report_month_end))
    result = cursor.fetchall()
    return result


@DBConnection
def get_sales_report_by_week(report_week_start, report_week_end, database):
    cursor = database.cursor()
    cursor.execute('''
        SELECT Order_Date, Telescope_Name, Product_Quantity, Product_Price
        FROM orders 
        JOIN contains ON orders.Order_ID = contains.OrderID
        JOIN telescopes ON telescopes.TelescopeID = contains.TelescopeID
        WHERE Order_Date >= %s AND Order_Date <= %s
    ''', (report_week_start, report_week_end))
    result = cursor.fetchall()
    return result


@DBConnection
def get_sales_report_by_day(report_day,database):
    cursor = database.cursor()
    cursor.execute('''
        SELECT Order_Date, Telescope_Name, Product_Quantity, Product_Price
        FROM orders 
        JOIN contains ON orders.Order_ID = contains.OrderID
        JOIN telescopes ON telescopes.TelescopeID = contains.TelescopeID
        WHERE Order_Date = %s
    ''', (report_day,))
    result = cursor.fetchall()
    return result


@DBConnection
def get_sales_report_by_product(product, database):
    cursor = database.cursor()
    cursor.execute('''
        SELECT Order_Date, Telescope_Name, Product_Quantity, Product_Price
        FROM orders 
        JOIN contains ON orders.Order_ID = contains.OrderID
        JOIN telescopes ON telescopes.TelescopeID = contains.TelescopeID
        WHERE Telescope_Name = %s
    ''', (product,))
    result = cursor.fetchall()
    return result

@DBConnection
def get_inventory_report(database):
    cursor = database.cursor()
    cursor.execute('''
        SELECT Telescope_Name, SUM(Product_Quantity) AS Total_Quantity
        FROM telescopes
        GROUP BY Telescope_Name
    ''')
    result = cursor.fetchall()
    return result


