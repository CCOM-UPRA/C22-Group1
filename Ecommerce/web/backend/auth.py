from flask import Blueprint, render_template, redirect, url_for, request

auth = Blueprint('back_auth', __name__, template_folder='/templates')
