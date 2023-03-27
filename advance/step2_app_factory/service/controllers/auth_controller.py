from flask import render_template, request, url_for
from service.controllers import bp_auth as auth

@auth.route('/')
def home():
    # url_for("별칭.함수명") => url이 리턴된다
    print(url_for('auth_bp.login'))
    return "auth 홈"

@auth.route('/login')
def home():
    return "auth login"

@auth.route('/logout')
def home():
    return "auth logout"

@auth.route('/signup')
def home():
    return "auth signup"

@auth.route('/delete')
def home():
    return "auth delete"

