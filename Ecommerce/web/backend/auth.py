from flask import Blueprint, render_template, redirect, url_for, request,Flask,session
from ..controllers.backend.accountController import *

auth = Blueprint('back_auth', __name__, template_folder='/templates')

app = Flask(__name__)

@auth.route('/backlogout')
def backlogout():
    session.pop('admin')
    return redirect(url_for('auth.login'))

@auth.route('encript', methods=['GET', 'POST'])
def encript():
    if request.method == 'POST':
        users = UsersList()
        for i in users:
            user_id = i['id']
            user_pass = i['pass']
            pass_hash = hashlib.sha256(user_pass.encode()).hexdigest()
            #update_password(user_id, pass_hash) 
    return redirect(url_for('back_views.accounts'))