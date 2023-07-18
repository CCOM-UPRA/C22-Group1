import hashlib
from flask import Blueprint, render_template, redirect, url_for, request,Flask,session
from ..models.backend.loginA import *


auth = Blueprint('back_auth', __name__, template_folder='/templates')

app = Flask(__name__)




# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form['C_Email']
#         password = request.form['C_Password']
#         if email_exists(email):
#             customer = adminlog(email)
#             db_password = customer[0]
#             customerID = customer[1]
#             if password == db_password:
#                 session['customer'] = customerID
#                 return redirect(url_for('back_views.admin_products'))
#             else:
#                 return 'Password dont match!'
#         else:
#             return render_template('admin_login.html')
#     return render_template('admin_login.html')

# @auth.route('/logout')
# def logout():
#     session.pop('customer')
#     return render_template('/admin_login.html')


# if __name__ == '__main__':
#     app.run()