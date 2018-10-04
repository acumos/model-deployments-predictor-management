"""Utility methods for loading configuration values"""

import logging
from datetime import datetime


def generate_predictor_key(username):
    delimiter = '_'
    name = ""
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    if '@' in username:
        name = username.split('@')[0] + delimiter + str(now)
    else:
        name = username + delimiter + str(now)

    logging.info("generate_predictor_key %s", name)
    return name

