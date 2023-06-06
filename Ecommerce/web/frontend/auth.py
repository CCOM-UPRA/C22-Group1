from flask import Blueprint, render_template, request, redirect, url_for, session

auth = Blueprint('auth', __name__, template_folder='/templates')


@auth.route('/login')
def login():
    session['customer'] = []
    return redirect('/')


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
