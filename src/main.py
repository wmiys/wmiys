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
from Utilities import Utilities
from functools import wraps, update_wrapper
from Constants import Constants
import json

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
CORS(app)


apiWrapper = ApiWrapper()



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

        # set the wrapper authentication members
        global apiWrapper
        apiWrapper.userID = session.get('userID')
        apiWrapper.email = session.get('email')
        apiWrapper.password = session.get('password')

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
    return flask.render_template('pages/home.html', email=flask.session.get('email'), password=flask.session.get('password'))


@app.route('/login')
def login():
    # clear the session data
    flask.session.pop('email', None)
    flask.session.pop('password', None)

    return flask.render_template('pages/login.html')


@app.route('/create-account')
def createAccount():
    # clear the session data
    session.pop('email', None)
    session.pop('password', None)

    return flask.render_template('pages/create-account.html')


@app.route('/products', methods=['GET'])
@login_required
def productsGet():
    apiResponse = apiWrapper.getUserProducts()

    if apiResponse.status_code != 200:
        pass    # error

    products = apiResponse.json()

    # format the product images
    for product in products:
        if product['image'] != None:
            product['image'] = '{}/{}'.format(Constants.PRODUCT_IMAGES_PATH, product['image'])
        else:
            product['image'] = '/static/img/placeholder.jpg'

    return flask.render_template('pages/products/products.html', products=products)


@app.route('/products/new')
@login_required
def productsNew():
    # create an empty product
    apiResponse = apiWrapper.postUserProduct(None, None)

    if apiResponse.status_code != 200:
        pass    # error

    # get the id from the response
    emptyProduct = apiResponse.json()

    # load the edit product page
    return redirect(url_for('productPageEdit', product_id=emptyProduct['id']))

@app.route('/products/<int:product_id>')
@login_required
def productPageEdit(product_id):
    apiResponse = apiWrapper.getUserProduct(product_id)

    if apiResponse.status_code != 200:
        pass    # error

    product = apiResponse.json()

    # return jsonify(product)

    if product['image'] != None:
        product['image'] = '{}/{}'.format(Constants.PRODUCT_IMAGES_PATH, product['image'])
    # else:
    #     product['image'] = '/static/img/placeholder.jpg'

    return flask.render_template('pages/products/product-edit.html', product=product)


@app.route('/products/<int:product_id>/availability')
@login_required
def productPageAvailability(product_id):
    apiResponse = apiWrapper.getProductAvailabilities(product_id)

    if apiResponse.status_code != 200:
        pass    # error

    availabilities = apiResponse.json()
    return flask.render_template('pages/products/product-availability.html', availabilities=availabilities)



@app.route('/account-settings')
@login_required
def accountSettings():
    response = apiWrapper.getUser()
    return flask.render_template('pages/account-settings/account-settings.html', userInfo=response.json())



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
    responseData = result.json()
    
    flask.session['userID'] = responseData['id']
    flask.session['email'] = userEmail
    flask.session['password'] = userPassword

    return ('', 200)


@app.route('/api/create-account', methods=['POST'])
def apiCreateAccount():
    user_email      = request.form.get('email')
    user_password   = request.form.get('password')
    user_name_first = request.form.get('name_first')
    user_name_last  = request.form.get('name_last')
    user_birth_date = request.form.get('birth_date')

    result = ApiWrapper.createAccount(email=user_email, password=user_password, name_first=user_name_first, name_last=user_name_last, birth_date=user_birth_date)

    if result.status_code != 200:
        flask.abort(result.status_code)

    # set the session variables
    responseData = result.json()
    flask.session['userID'] = responseData['id']
    flask.session['email'] = user_email
    flask.session['password'] = user_password

    return ('', 200)


@app.route('/api/products', methods=['POST'])
@login_required
def apiProductsPost():
    apiResponse = apiWrapper.postUserProduct(request.form, request.files.get('image'))

    if apiResponse.status_code != 200:
        flask.abort(apiResponse.status_code)
    
    return ('', 200)

@app.route('/api/products/<int:product_id>', methods=['PUT'])
@login_required
def apiProductPut(product_id):
    apiResponse = apiWrapper.putUserProduct(product_id, request.form, request.files.get('image'))

    if apiResponse.status_code != 200:
        flask.abort(apiResponse.status_code)
    
    return ('', 200)



#------------------------------------------------------
# Handle any requests related a single product availability:
#  - GET:    Retrieve a single product availability record
#  - PUT:    Update a single product availability record
#  - DELETE: Delete a single product availability record
#------------------------------------------------------
@app.route('/api/products/<int:product_id>/availability/<int:product_availability_id>', methods=['GET', 'PUT','DELETE'])
@login_required
def apiProductAvailabilityModify(product_id, product_availability_id):
    if request.method == 'GET':
        apiResponse = apiWrapper.getProductAvailability(product_id, product_availability_id)

        if apiResponse.status_code != 200:          # error
            flask.abort(apiResponse.status_code)

        return (jsonify(apiResponse.json()), 200)

    apiResponse = None

    if request.method == 'PUT':
        apiResponse = apiWrapper.putProductAvailability(product_id, product_availability_id, request.form)
    elif request.method == 'DELETE':
        apiResponse = apiWrapper.deleteProductAvailability(product_id, product_availability_id)

    return ('', apiResponse.status_code)


#------------------------------------------------------
# Create a new product
#------------------------------------------------------
@app.route('/api/products/<int:product_id>/availability', methods=['POST'])
@login_required
def apiProductAvailability(product_id):
    
    apiResponse = apiWrapper.insertProductAvailability(product_id, request.form)

    if apiResponse.status_code != 200:          # error
        flask.abort(apiResponse.status_code)

    return (jsonify(apiResponse.json()), 200)



#************************************************************************************
#
#                                   Main function
#
#************************************************************************************
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)







