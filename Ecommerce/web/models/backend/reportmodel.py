
from ...dbConnection import *
import sqlite3


@DBConnection
def get_sales_report_by_month(report_month_start, report_month_end, database):
    cursor = database.cursor()
    cursor.execute('''
        SELECT
            Order_Date,
            Telescope_Name,
            Product_Quantity,
            Product_Price,
            (Product_Price - Telescope_Cost) AS Earnings
        FROM
            orders
        JOIN
            contains ON orders.Order_ID = contains.OrderID
        JOIN
            telescopes ON telescopes.TelescopeID = contains.TelescopeID
        WHERE
            Order_Date >= %s AND Order_Date <= %s
    ''', (report_month_start, report_month_end))
    result = cursor.fetchall()
    return result


@DBConnection
def get_sales_report_by_week(report_week_start, report_week_end, database):
    cursor = database.cursor()
    cursor.execute('''
        SELECT
            Order_Date,
            Telescope_Name,
            Product_Quantity,
            Product_Price,
            (Product_Price - Telescope_Cost) AS Earnings
        FROM
            orders
        JOIN
            contains ON orders.Order_ID = contains.OrderID
        JOIN
            telescopes ON telescopes.TelescopeID = contains.TelescopeID
        WHERE
            Order_Date >= %s AND Order_Date <= %s
    ''', (report_week_start, report_week_end))
    result = cursor.fetchall()
    return result



@DBConnection
def get_sales_report_by_day(report_day,database):
    cursor = database.cursor()
    cursor.execute('''
         SELECT
            Order_Date,
            Telescope_Name,
            Product_Quantity,
            Product_Price,
            (Product_Price - Telescope_Cost) AS Earnings
        FROM
            orders
        JOIN
            contains ON orders.Order_ID = contains.OrderID
        JOIN
            telescopes ON telescopes.TelescopeID = contains.TelescopeID
        WHERE
            Order_Date = %s
    ''', (report_day,))
    result = cursor.fetchall()
    return result



@DBConnection
def get_inventory_report(database):
    cursor = database.cursor()
    cursor.execute('''
        SELECT Telescope_Name,TelescopeID, Telescope_Stock 
        FROM telescopes
        
    ''')
    result = cursor.fetchall()
    return result

@DBConnection
def get_products(database):
    cursor=database.cursor()
    cursor.execute('SELECT TelescopeID, Telescope_Name FROM telescopes')
    result = cursor.fetchall()
    return result

@DBConnection
def prod_name(database):
    cursor=database.cursor()
    cursor.execute('SELECT Telescope_Name FROM telescopes')
    result = cursor.fetchall()
    return result



@DBConnection
def get_prodid(product,date, database):
    cursor = database.cursor()
    cursor.execute('''
        SELECT
            Order_Date,
            Telescope_Name,
            Product_Quantity,
            Product_Price,
            (Product_Price - Telescope_Cost) AS Earnings
        FROM
            orders
        JOIN
            contains ON orders.Order_ID = contains.OrderID
        JOIN
            telescopes ON telescopes.TelescopeID = contains.TelescopeID
        WHERE
            Telescope_Name = %s AND Order_Date = %s
    ''', (product,date,))
    result = cursor.fetchall()
    return result

@DBConnection
def sales_report_by_week(product,report_week_start, report_week_end, database):
    cursor = database.cursor()
    cursor.execute('''
         SELECT
            Order_Date,
            Telescope_Name,
            Product_Quantity,
            Product_Price,
            (Product_Price - Telescope_Cost) AS Earnings
        FROM
            orders
        JOIN
            contains ON orders.Order_ID = contains.OrderID
        JOIN
            telescopes ON telescopes.TelescopeID = contains.TelescopeID
        WHERE
            Telescope_Name = %s AND Order_Date >= %s AND Order_Date <= %s
    ''', (product,report_week_start, report_week_end,))
    result = cursor.fetchall()
    return result

@DBConnection
def sales_report_by_month(product, year, month, database):
    cursor = database.cursor()
    cursor.execute('''
        SELECT
            Order_Date,
            Telescope_Name,
            Product_Quantity,
            Product_Price,
            (Product_Price - Telescope_Cost) AS Earnings
        FROM
            orders
        JOIN
            contains ON orders.Order_ID = contains.OrderID
        JOIN
            telescopes ON telescopes.TelescopeID = contains.TelescopeID
        WHERE
            Telescope_Name = %s AND YEAR(Order_Date) = %s AND MONTH(Order_Date) = %s
    ''', (product,year, month,))
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
def earningreport(database):
    cursor = database.cursor()
    cursor.execute('''
    SELECT
        t.Telescope_Name,
        c.Product_Price,
         t.Telescope_Cost,
        (c.Product_Price - t.Telescope_Cost) AS Earnings
        
    FROM
        telescopes t
    JOIN
        contains c ON t.TelescopeID = c.TelescopeID
                   ''')
    result = cursor.fetchall()
    return result

@DBConnection 
def totalearningreport(database):
    cursor = database.cursor()
    cursor.execute('''
    SELECT SUM((c.Product_Price - t.Telescope_Cost)) AS Earnings FROM telescopes t JOIN contains c ON t.TelescopeID = c.TelescopeID
                   ''')
    result = cursor.fetchone()
    return result[0]
