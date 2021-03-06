#*******************************************************************************************
# Module:       products
#
# Url Prefix:   /products
#
# Description:  Handles pages dealing with lender products
#*******************************************************************************************
from __future__ import annotations
import flask
from datetime import datetime

from wmiys.common import security, product_requests
from wmiys.payments import payout_accounts
from wmiys.api_wrapper import ApiWrapperUsers, ApiWrapperProducts, ApiWrapperProductAvailability

# module blueprint
bpProducts = flask.Blueprint('products', __name__)




#------------------------------------------------------
# Overview page
#------------------------------------------------------
@bpProducts.get('')
@security.login_required
@payout_accounts.payout_account_required
def overviewGet():
    api = ApiWrapperUsers(flask.g)
    response = api.get()

    return flask.render_template('pages/products/overview.html', data=response.json())

#------------------------------------------------------
# Inventory page
#------------------------------------------------------
@bpProducts.get('inventory')
@security.login_required
@payout_accounts.payout_account_required
def productsGet():
    api = ApiWrapperProducts(flask.g)
    api_response = api.get()

    if not api_response.ok:
        flask.abort(api_response.status_code)

    products: list[dict] = api_response.json()

    # use the placeholder image if the product does not have an image
    for product in products:
        product['image'] = product['image'] or '/static/img/placeholder.jpg'

    return flask.render_template('pages/products/inventory.html', products=products)


#------------------------------------------------------
# All received product requests (as a lender)
#------------------------------------------------------
@bpProducts.get('requests')
@bpProducts.get('requests/pending')
@security.login_required
@payout_accounts.payout_account_required
def requestsGet():
    # status_filter = flask.request.args.get('status', 'pending')
    status_filter = 'pending'
    requests = product_requests.getRequests(status_filter)
    return flask.render_template('pages/products/requests/pending.html', data=requests)


#------------------------------------------------------
# All received product requests (as a lender)
#------------------------------------------------------
@bpProducts.get('requests/resolved')
@security.login_required
@payout_accounts.payout_account_required
def requestsGetResolved():
    # status_filter = flask.request.args.get('status', 'all')
    status_filter = 'all'
    requests = product_requests.getRequests(status_filter)
    return flask.render_template('pages/products/requests/resolved.html', data=requests)


#------------------------------------------------------
# Create new product
#------------------------------------------------------
@bpProducts.get('new')
@security.login_required
@payout_accounts.payout_account_required
def productsNew():
    api = ApiWrapperProducts(flask.g)
    
    # post an empty product
    api_response = api.post(None, None)

    if not api_response.ok:
        flask.abort(400)
        # return flask.jsonify(api_response.text, api_response.status_code)

    # get the id from the response
    emptyProduct = api_response.json()

    # load the edit product page
    return flask.redirect(flask.url_for('products.productPageEdit', product_id=emptyProduct['id']))

#------------------------------------------------------
# Single product page
#------------------------------------------------------
@bpProducts.route('<int:product_id>', methods=['GET', 'DELETE'])
@security.login_required
@payout_accounts.payout_account_required
def productPageEdit(product_id):
    product_api_response = _getProductApiResponse(product_id)
    return flask.render_template('pages/products/product/overview.html', product=product_api_response)


#------------------------------------------------------
# Product availability
#------------------------------------------------------
@bpProducts.get('<int:product_id>/availability')
@security.login_required
@payout_accounts.payout_account_required
def productPageAvailability(product_id):
    # get the product's availability records from the api
    availabilities = _getProductAvailabilityApiResponse(product_id)
    product_api_response = _getProductApiResponse(product_id)

    return flask.render_template('pages/products/product/availability.html', product=product_api_response, availabilities=availabilities)
    
#------------------------------------------------------
# Product insights
#------------------------------------------------------
@bpProducts.get('<int:product_id>/insights')
@security.login_required
@payout_accounts.payout_account_required
def productPageInsights(product_id):
    product_api_response = _getProductApiResponse(product_id)

    return flask.render_template('pages/products/product/insights.html', product=product_api_response)

#------------------------------------------------------
# Product settings
#------------------------------------------------------
@bpProducts.get('<int:product_id>/settings')
@security.login_required
def productPageSettings(product_id):
    product_api_response = _getProductApiResponse(product_id)
    
    return flask.render_template('pages/products/product/settings.html', product=product_api_response)



#------------------------------------------------------
# Retrieve the api response for a product
#------------------------------------------------------
def _getProductApiResponse(product_id: int) -> dict:
    # get the product's info from the api
    api = ApiWrapperProducts(flask.g)
    api_response = api.get(product_id)

    if not api_response.ok:
        flask.abort(api_response.status_code, api_response.text)
        return

    product_api_response = api_response.json()

    return product_api_response

#------------------------------------------------------
# Get the product's availability records from the api
#------------------------------------------------------
def _getProductAvailabilityApiResponse(product_id: int) -> list[dict]:
    api = ApiWrapperProductAvailability(flask.g)
    api_response = api.get(product_id)
    
    if not api_response.ok:
        flask.abort(api_response.status_code, api_response.text)
        return

    availabilities = api_response.json()
    _formatAvailabilityDates(availabilities)

    return availabilities

#------------------------------------------------------
# Format the date fields
#------------------------------------------------------
def _formatAvailabilityDates(product_availabilities: list[dict]):
    for row in product_availabilities:
        formatToken = '%m/%d/%Y'
        keys = ['created_on', 'ends_on', 'starts_on']

        for key in keys:
            row[key] = datetime.fromisoformat(row[key]).strftime(formatToken)