"""
**********************************************************************************************

Location services

**********************************************************************************************
"""


from __future__ import annotations

import flask

from wmiys.repository import locations as locations_repo
from wmiys.domain import models
from wmiys.api import other

#------------------------------------------------------
# Respond to a GET request
#------------------------------------------------------
def response_GET(location_id: int) -> flask.Response:
    location_model = models.Location(
        id = location_id
    )

    result = locations_repo.select(location_model)
    
    # make sure sql command was successful and the location exists
    if not result.successful:
        return other.responses.badRequest(str(result.error))
    elif not result.data:
        return other.responses.notFound()

    # all good - return the location
    return other.responses.get(result.data)



