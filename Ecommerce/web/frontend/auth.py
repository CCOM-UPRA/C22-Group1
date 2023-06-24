from flask import Blueprint, render_template, request, redirect, url_for, session
from ..models.frontend.loginModel import *
import hashlib

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'customer' not in session:
            return redirect('/')
        return func(*args, **kwargs)
    return wrapper


auth = Blueprint('auth', __name__, template_folder='/templates')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['C_Email']
        password = request.form['C_Password']
        if email_exists(email):
            customer = customerlog(email=email)
            db_password = customer[0]
            customerID = customer[1]
            if password == db_password:
                session['customer'] = customerID
                return redirect(url_for('views.shop'))
            else:
                return 'Password dont match!'
        else:
            return render_template('register.html')
    return render_template('login.html')


@auth.route('/logout')
def logout():
    session.pop('customer')
    return render_template('/login.html')


@auth.route('/register' , methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fname = request.form['C_fname']
        lname = request.form['C_lname']
        email = request.form['C_email']
        pass1 = request.form['C_password1']
        pass2 = request.form['C_password2']
        
        if not fname or not lname or not email or not pass1 or not pass2:
            return 'fill all the blanks'
        
        if pass1 != pass2:
            return 'Password dont match!'
        
        if email_exists(email):
            return 'Email already exists!'
        pass1_hash = hashlib.sha256(pass1.encode()).hexdigest()
        insert_user(fname, lname, email, pass1)
        session['customer'] = ID_Email(email)[0]
        
        return render_template('shop.html')
    return render_template('register.html')


# @auth.route('/password', methods=['GET', 'POST'])
# def change_password():
#     if request.method == 'POST':
#         # Obtener los datos del formulario
#         username = request.form['C_Email']
#         pass_o = request.form['C_Password']
#         pass_n = request.form['pass_n']
#         pass_n1 = request.form['pass_n1']
        
        
#         if pass_n == pass_n1:
#             # Verificar la existencia de la contraseña actual en la base de datos
#             count = check_password(username, pass_o)

#             if count > 0:
#                 # Actualizar la contraseña en la base de datos
#                 update_password(pass_n, username)

#                 # Almacenar el nombre de usuario en la sesión
#                 #session['username'] = username

#                 # Redirigir a una página de éxito
#                 return render_template('login.html')
#             else:
#                 # Contraseña actual incorrecta
#                 error_message = "La contraseña actual es incorrecta."
#                 return render_template('change_password.html', error_message=error_message)
#         else:
#             # Las contraseñas nuevas no coinciden
#             error_message = "Las contraseñas nuevas no coinciden."
#             return render_template('change_password.html', error_message=error_message)

#     # Si el método de solicitud es GET, simplemente renderiza el formulario de cambio de contraseña
#     return render_template('change_password.html')