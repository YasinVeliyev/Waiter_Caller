from waitercaller import app, login_manager
from flask import render_template, redirect, url_for, request
from flask_login import login_required, login_user, logout_user, current_user
from waitercaller.user import User
from waitercaller.forms import RegistrationForm, LoginForm
from waitercaller import config
from datetime import datetime
import time
from werkzeug.security import check_password_hash, generate_password_hash
# from waitercaller import utils as db





@login_manager.user_loader
def load_user(user_id):
   return User.get_user_by_id(user_id)

@app.route("/", methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route("/dashboard")
@login_required
def dashboard():
    db = User(current_user.email)
    now = datetime.now()
    requests = db.get_request(current_user.id)
    for req in requests:
        deltaseconds = (now - req['time']).seconds
        req['wait_minutes'] = f"{deltaseconds//60}.{deltaseconds%60}"
    return render_template('dashboard.html', requests = requests)

@app.route("/account")
@login_required
def account():
    db = User(current_user.email)
    tables = db.get_tables(current_user.id)
    return render_template('account.html', tables=tables)

@app.route("/register", methods=['GET', "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.get_user_by_email(form.email.data):
            return render_template("register.html", form=form)
        User.set_id()
        User.add_user({'email':form.email.data, 'password':generate_password_hash(form.password.data)})
        print(User.MOCK_USERS)
        return redirect(url_for('login'))
    return render_template("register.html", form=form)


@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.get_user_by_email(email)
        if user and check_password_hash(user['password'], password):
            user = User(email)
            print(user.id)
            login_user(user)
            return redirect(url_for('account'))
        form.email.errors.append("Email or password invalid")
        form.password.errors.append("Email or password invalid")
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/account/createtable", methods = ['POST'])
@login_required
def create_table():
    # db = User(current_user.email)
    table_name = request.form.get('tablenumber')
    table_id = User.add_table(table_name, current_user.get_id())
    new_url = config.base_url + "newrequest/" + table_id
    current_user.update_table(table_id, new_url)
    return redirect(url_for('account'))

@app.route("/account/deletetable")
@login_required
def delete_table():
    table_id = request.args.get("tableid")
    current_user.delete_table(table_id)
    return redirect(url_for('account'))

@app.route("/newrequest/<tid>")
def newrequest(tid):
    db = User(current_user.email)
    db.add_request(tid, datetime.now())
    return 'Your request has been logged and a waiter will be with you shortly'

@app.route("/dashboard/resolve")
@login_required
def dashboard_resolve():
    request_id = request.args.get("request_id")
    User.delete_request(request_id)
    return redirect(url_for('dashboard'))

#218