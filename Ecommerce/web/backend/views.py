from flask import Blueprint, redirect, url_for, render_template, request

views = Blueprint('back_views', __name__, template_folder='templates/')


@views.route('/')
@views.route('/clear')
def clear():
    return redirect(url_for('back_views.products'))


@views.route('/products')
def products():
    return render_template('products.html')


@views.route('/addproduct')
def addproduct():
    return render_template('add_product.html')


@views.route('/accounts')
def accounts():
    return render_template('accounts.html')


@views.route('/reports')
def reports():
    return render_template('reports.html')


@views.route('/profile')
def profile():
    return render_template('profile2.html', user1 = [])
