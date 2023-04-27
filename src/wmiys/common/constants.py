"""
************************************************************************************
This module contains shared symbolic constants used throughout the codebase.
None of the values of these constants should EVER be modified in the code.
***************************************************************************************
"""

import enum

VPS_IP_ADDRESS = '104.225.208.116'


class SECONDS_PER(enum.IntEnum):
    HOUR = 3600
    MINUTE = 60
