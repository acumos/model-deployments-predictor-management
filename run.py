#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ===============LICENSE_START=======================================================
# Acumos Apache-2.0
# ===================================================================================
# Copyright (C) 2017-2018 AT&T Intellectual Property. All rights reserved.
# ===================================================================================
# This Acumos software file is distributed by AT&T
# under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============LICENSE_END=========================================================
"""Utility script to run a local development server."""

from predictormanagerservice.app import initialize_app
from flask import Flask

import argparse
import configparser
import logging
import os

logger = logging.getLogger(__name__)

app = Flask(__name__)

DEFAULT_HOST = '0.0.0.0'
DEFAULT_PORT = 8085


def get_default_properties_path():
    dir_path = os.path.dirname(os.path.join(os.path.realpath(__file__)))
    return os.path.join(dir_path, 'properties', 'settings.cfg')


def load_properties(config_path):
    parser = configparser.ConfigParser()
    parser.read(config_path)
    mongo = parser['MONGO']
    app.config['MONGODB_SETTINGS'] = {
        'host': mongo['mongo_host'],
        'port': mongo.getint('mongo_port'),
        'db': mongo['mongo_dbname'],
        'username': mongo['mongo_username'],
        'password': mongo['mongo_password'],
    }

    files_config = parser['FILES']
    app.config['UPLOAD_FOLDER'] = files_config['upload_dir']


def parse_args():
    default_path = get_default_properties_path()

    parser = argparse.ArgumentParser(description='Run a development server.')

    parser.add_argument('--host', default=DEFAULT_HOST,
                        help='specify the host used to run the development server (default: {})'.format(DEFAULT_HOST))
    parser.add_argument('--settings', default=get_default_properties_path(),
                        help='specify the location of the configuration: (default: {})'.format(default_path))

    parser.add_argument('--port', default=DEFAULT_PORT, type=int,
                        help='specify the port used to run the development server (default: {})'.format(DEFAULT_PORT))

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    load_properties(args.settings)

    initialize_app(app)
    app.run(host=args.host, debug=True, port=args.port)
