"""
************************************************************************************
Provides several common "utility" methods that are used by both the front-end and 
the api code.

This will probably get a little messy and unorganized, but fuck it. I was duplicating
these functions in both applications, so why not make a central respository for them.
***************************************************************************************
"""

from __future__ import annotations
import json
import flask.json as fjson
import uuid
from datetime import datetime
import flask
from . import constants


#------------------------------------------------------
# return the data from the specified json file
#------------------------------------------------------
def readJsonFile(file_name_path: str) -> dict:
    with open(file_name_path) as configFile:
        configData = json.loads(configFile.read())
        return configData

# ------------------------------------------------------
# Returns a UUID
#-------------------------------------------------------
def getUUID(as_string: bool=True) -> str | uuid.UUID:
    new_uuid = uuid.uuid4()
    
    if as_string == True:
        return str(new_uuid)
    else:
        return new_uuid

# ------------------------------------------------------
# Prints an object to the console between the specified number of line breaks
#-------------------------------------------------------
def printWithSpaces(output='', num_spaces: int = 20):
    lineBreak(num_spaces)
    print(output)
    lineBreak(num_spaces)

# ------------------------------------------------------
# Prints a specified number of line breaks to the console
#-------------------------------------------------------
def lineBreak(num_lines: int=1):
    print("\n" * num_lines)

# ------------------------------------------------------
# Print to console the json formatted object
# ------------------------------------------------------
def dumpJson(output):
    try:
        serialized_output = fjson.dumps(output, indent=4)
    except Exception as e:
        lineBreak(1)
        print(e)
        lineBreak(1)

        serialized_output = output
    finally:
        print(serialized_output)

# ------------------------------------------------------
# Checks if any of the fields contained in the dict are valid properties of the given object
#
# returns a boolean:
#   true - all dict fields are valid
#   false - the dict contains a field that is not a property of the object
#-------------------------------------------------------
def areAllKeysValidProperties(test_dict: dict, the_object: object) -> bool:
    for key in test_dict:
        if not hasattr(the_object, key):
            return False
    
    return True


#------------------------------------------------------
# Set's the object's properties given a dict
#------------------------------------------------------
def setPropertyValuesFromDict(new_property_values: dict, the_object):
    # set the object properties
    for key in new_property_values:
        if new_property_values[key]:
            setattr(the_object, key, new_property_values.get(key, None))
        else:
            setattr(the_object, key, None)
        
#------------------------------------------------------
# Try to parse an int
#------------------------------------------------------
def intTryParse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False

#------------------------------------------------------
# Get the number of hours between the given start/end times.
#------------------------------------------------------
def getDurationHours(date_start: datetime, date_end: datetime) -> int:
    then = date_start        
    now  = date_end                                 # Now
    duration = now - then                           # For build-in functions
    duration_in_s = duration.total_seconds()        # Total number of seconds between dates

    return divmod(duration_in_s, constants.SECONDS_PER.HOUR)[0] 

#------------------------------------------------------
# Get the number of minutes between the given start/end times.
#------------------------------------------------------
def getDurationMinutes(date_start: datetime, date_end: datetime) -> int:
    then = date_start        
    now  = date_end                                 # Now
    duration = now - then                           # For build-in functions
    duration_in_s = duration.total_seconds()        # Total number of seconds between dates

    return abs(round(divmod(duration_in_s, constants.SECONDS_PER.MINUTE)[0]))

#------------------------------------------------------
# Checks whether or not this is production enviornment.
#
# Returns a bool:
#   true: this is running on the VPS
#   false: not running on the vps
#------------------------------------------------------
def isProductionEnv() -> bool:
    server_ip, server_port = flask.request.server

    if server_ip == constants.VPS_IP_ADDRESS:
        return True
    else:
        return False


#------------------------------------------------------
# Convert the given dollar amount to cents.
#
# Returns an int: the number of cents in the dollar amount.
#------------------------------------------------------
def dollarsToCents(dollars: float) -> int:
    return round(dollars * 100)    

#------------------------------------------------------
# Checks if the specified number is in the range
#------------------------------------------------------
def inRange(number, minimum, maximum) -> bool:
    if minimum <= number <= maximum:
        return True
    else:
        return False