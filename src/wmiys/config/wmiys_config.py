from dataclasses import dataclass

@dataclass
class WmiysConfig:
    JSON_SORT_KEYS: bool
    JSONIFY_PRETTYPRINT_REGULAR: bool
    SECRET_KEY_API: str
    SECRET_KEY_GUI: str
    URL_API: str
    URL_GUI: str
    DB_NAME: str
    DB_HOST: str
    DB_PASSWORD: str
    DB_USER: str
    DB_HOST_IP: str


