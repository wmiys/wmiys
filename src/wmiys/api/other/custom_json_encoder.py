#************************************************************************************
# Name:     CustomJSONEncoder
#
# Purpose:  This class is used to encode date's in the correct format: YYYY-MM-DD. 
#
#           Before creating this, Flask was encoding all dates/datetimes/times as 'Mon, 15 Mar 2021 18:30:42 GMT'.
#           This was done to fields that were only dates.
#
#           The solution was found: https://www.javaer101.com/en/article/1732830.html
#************************************************************************************

from flask.json.provider import DefaultJSONProvider
from datetime import date, datetime, timedelta
from decimal import Decimal

class CustomJSONEncoder(DefaultJSONProvider):

    compact = False
    sort_keys = False

    @staticmethod
    def default(obj):

        try:
            if isinstance(obj, (date, datetime)):
                return obj.isoformat()
            elif isinstance(obj, Decimal):
                return float(obj)
            elif isinstance(obj, timedelta):
                return timedelta.__str__
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        
        return DefaultJSONProvider.default(obj)
        