import hashlib
from flask import Blueprint, render_template, redirect, url_for, request,Flask,session

auth = Blueprint('back_auth', __name__, template_folder='/templates')

app = Flask(__name__)
