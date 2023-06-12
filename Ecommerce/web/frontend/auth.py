from flask import Blueprint,Flask , flash, render_template, request, redirect, url_for, session
from flask_mysqldb  import MySQL
auth = Blueprint('auth', __name__, template_folder='/templates')
from ..models.authmodel import customerlog
from flask import session
from ..dbConnection import *
#import mysql.connector
from functools import wraps






@auth.route('/logout')
def logout():
   # logout_user()
    return redirect(url_for('login'))


@auth.route('/home')
def home():
    return render_template('shop.html')

@auth.route('/logout')
def logout():
    session.pop('customer')
    return redirect('/')


@auth.route('/register')
def register():
    return render_template('register.html')


@auth.route('/password')
def password():
    pass




app = Flask(__name__)




# def hash_password(password):
#     salt = bcrypt.gensalt()
#     hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
#     return hashed_password

@auth.route('/login', methods=['GET', 'POST'])
@DBConnection
def login(*args, **kwargs):
    
    if request.method == 'POST':
        email = request.form['C_Email']
        password = request.form['C_Password']
        customer = customerlog(email=email)

        # Obtener el hash de la contraseña almacenada en la base de datos
      

        if customer:
            hashed_password = customer[0]
            CustomerID = customer[1]
            if password == hashed_password:
                # Guardar la información de la cuenta del usuario en la sesión
                session['email'] = email
                session['password'] = hashed_password
                session['customer'] = CustomerID 
                
                # Redireccionar al usuario a la página deseada después del inicio de sesión exitoso
                return redirect(url_for('views.shop'))
            
        # La contraseña es incorrecta o el email no se encontró, volver a cargar la página de inicio de sesión con un mensaje de error
        return render_template('login.html', error=True)
    else:
        # Mostrar la página de inicio de sesión
        return render_template('login.html', error=False)



if __name__ == '__main__':
    app.run()
