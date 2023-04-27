"""
**********************************************************************************************

Development and production configuration classes

**********************************************************************************************
"""

from .private import ConfigPrivate
from copy import deepcopy


ConfigProduction = deepcopy(ConfigPrivate)

ConfigDev = deepcopy(ConfigPrivate)
ConfigDev.SECRET_KEY_API                  = b'UH5vjJaP3wCG9v9sfAgQ6nXrN5xQ5DxgBZQvaMLJa8SzpswmUhYQsVqQ+ItummAdeT37k85JOP0jmW5jqO7Zxw=='
ConfigDev.SECRET_KEY_GUI                  = b'SEXn773P7GF7I4kbaD/RUNNh86jg7R6SoB/WJCjxjfIvVuzsIOJMAmU4CNXKe6qRbRIajG2iGzBZYZ/hQHQmAA=='
ConfigDev.URL_API = 'http://10.0.0.82:5000'
ConfigDev.URL_GUI = 'http://10.0.0.82:8000'
ConfigDev.DB_NAME = 'wmiys_dev'