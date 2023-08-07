from flask import Blueprint, render_template, redirect, url_for, request,Flask,session
from ..controllers.backend.accountController import *

auth = Blueprint('back_auth', __name__, template_folder='/templates')

app = Flask(__name__)

@auth.route('/backlogout')
def backlogout():
    session.pop('admin')
    return redirect(url_for('auth.login'))