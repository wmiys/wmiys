"""
**********************************************************************************************

Development and production configuration classes

**********************************************************************************************
"""

from .base_configuration import Base

#------------------------------------------------------
# The production config is the default, 
# It inherits all the values from the base
#------------------------------------------------------
class Production(Base):
    pass


#------------------------------------------------------
# Provide any overrides needed for development
#------------------------------------------------------
class Dev(Base):
    SECRET_KEY_API                  = b'UH5vjJaP3wCG9v9sfAgQ6nXrN5xQ5DxgBZQvaMLJa8SzpswmUhYQsVqQ+ItummAdeT37k85JOP0jmW5jqO7Zxw=='
    SECRET_KEY_GUI                  = b'SEXn773P7GF7I4kbaD/RUNNh86jg7R6SoB/WJCjxjfIvVuzsIOJMAmU4CNXKe6qRbRIajG2iGzBZYZ/hQHQmAA=='

    URL_API = 'http://10.0.0.82:5000'
    URL_GUI = 'http://10.0.0.82:8000'
    DB_NAME = 'wmiys_dev'
    DB_HOST = Base.DB_HOST_IP
 

