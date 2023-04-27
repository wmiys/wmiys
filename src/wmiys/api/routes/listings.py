"""
Package:        product_listings
Url Prefix:     /listings/<int:product_id>
Description:    Handles all the product listings routing.
"""

import flask
from wmiys.api.other import security
from wmiys.api.services import listings as listing_services
from wmiys.api.services import listing_availability as listing_availability_services

bp_listings = flask.Blueprint('productListings', __name__)


#----------------------------------------------------------
# Get a product's listing information for a single product
#----------------------------------------------------------
@bp_listings.get('')
@security.login_required
def getProductListings(product_id: int):
    return listing_services.responses_GET(product_id)

#----------------------------------------------------------
# Check if a product is available for rent
#----------------------------------------------------------
@bp_listings.get('availability')
@security.login_required
def getProductListingAvailability(product_id: int):
    return listing_availability_services.responses_GET(product_id)

