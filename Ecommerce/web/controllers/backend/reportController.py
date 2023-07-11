from ...models.backend.reportmodel import *
def Reports(report_month,report_day,report_week,report_week_start,product,database):
    sales_reports = get_sales_report_by_product(product,database)
    inventory_rep = get_inventory_report()
    report_day = get_sales_report_by_day(report_day,database)
    report_month = get_sales_report_by_month(report_month,database)
    report_week = get_sales_report_by_week(report_week,report_week_start,database)
    
    
    reportList = []
    for x in sales_reports:
      s_report = {
       'Order_Date': x[0],
        'Telescope_Name': x[1],
        'Product_Quantity': x[2],
        'Product_Price': x[3],
    }
    reportList.append(s_report)

    inventory = []
    for x in inventory_rep:
        r_inventory = {
        'Order_Date': x[0],
        'Telescope_Name': x[1],
        'Product_Quantity': x[2],
        'Product_Price': x[3],
        }
        inventory.append(r_inventory)

    day_rep = []
    for x in report_day:
        d_report = {
        'Order_Date': x[0],
        'Telescope_Name': x[1],
        'Product_Quantity': x[2],
        'Product_Price': x[3],
    }
        day_rep.append(d_report)



    return reportList,inventory,day_rep