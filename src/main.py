#************************************************************************************
#
#                                   API URL Routing Page
#
#************************************************************************************
import flask
from flask import Flask, jsonify, request, session, redirect, url_for
from flask_cors import CORS
from markupsafe import escape
import os
from ApiWrapper import ApiWrapper
from functools import wraps, update_wrapper

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
CORS(app)


#************************************************************************************
#
#                                   Decorators
#
#************************************************************************************
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        # if user is not logged in, redirect to login page
        if not session:
            return redirect(url_for('login'))

        return f(*args, **kwargs)

    return wrap




#************************************************************************************
#
#                                   Pages
#
#************************************************************************************
@app.route('/')
@login_required
def home():
    return flask.render_template('home.html', email=flask.session.get('email'), password=flask.session.get('password'))


@app.route('/login')
def login():
    # clear the session data
    flask.session.pop('email', None)
    flask.session.pop('password', None)

    return flask.render_template('login.html')


@app.route('/create-account')
def createAccount():
    # clear the session data
    session.pop('email', None)
    session.pop('password', None)

    return flask.render_template('create-account.html')


@app.route('/products')
@login_required
def products():
    return flask.render_template('products.html')

@app.route('/products/new')
@login_required
def productsNew():
    return flask.render_template('products-new.html')


@app.route('/products/<int:product_id>')
@login_required
def productPage(product_id):
    return flask.render_template('product-page.html')


@app.route('/account-settings')
@login_required
def accountSettings():
    return flask.render_template('account-settings.html')



#************************************************************************************
#
#                                   API Calls
#
#************************************************************************************
@app.route('/api/login')
def apiLogin():
    # get the email and password details
    userEmail = request.args.get('email')
    userPassword = request.args.get('password')

    # call the api
    result = ApiWrapper.login(userEmail, userPassword)

    # verify that the login was successful
    if result.status_code != 200:
        flask.abort(result.status_code)

    # set the session variables
    flask.session['email'] = userEmail
    flask.session['password'] = userPassword

    return ('', 200)



#************************************************************************************
#
#                                   Main function
#
#************************************************************************************
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)






