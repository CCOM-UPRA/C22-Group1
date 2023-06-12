from ..dbConnection import *
from flask import Flask, request, redirect, render_template
import mysql.connector
from functools import wraps
import bcrypt

# app = Flask(__name__)

@DBConnection
def customerlog(email,database):
    
     cursor = database.cursor()
     cursor.execute("SELECT C_Password,CustomerID FROM customers WHERE C_Email = %s", (email,))
         
     customer = cursor.fetchone()
     return customer
    
    