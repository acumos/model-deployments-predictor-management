#!/usr/bin/env python3
#
# ===============LICENSE_START=======================================================
# Acumos
# ===================================================================================
# Copyright (C) 2018 AT&T Intellectual Property. All rights reserved.
# ===================================================================================
# This Acumos software file is distributed by AT&T
# under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============LICENSE_END=========================================================
import configparser
import logging
import os


class ConfigUtilException(Exception):
    pass


def get_properties_path():
    if 'PROPERTIES_PATH' in os.environ:
        properties_path = 'properties'  # we assume relative
    properties_path = os.environ.get('PROPERTIES_PATH', 'properties')
    if not os.path.exists(properties_path):
        raise ConfigUtilException(f'{properties_path} does not exist. Please set PROPERTIES_PATH environmental value')
    return properties_path


_parser = None  # cache parser to avoid constant file IO


def get_parser():
    global _parser
    if _parser is None:
        parser = configparser.ConfigParser()
        # TODO (pk9069): allow settings.cfg to be specified
        config_path = os.path.join(get_properties_path(), 'settings.cfg')
        logging.info("config_path: %s", config_path)
        parser.read(config_path)
        _parser = parser
    return _parser


def get_config_value(env_name, config=None, config_name=None, section=None):
    if env_name in os.environ:
        return os.environ[env_name]

    if config is None:
        config = get_parser()
    if section is not None:
        if section not in config:
            raise ConfigUtilException(f"Section {section} does not exist")
        config = config[section]
    if config_name is None:
        config_name = env_name
    if config_name in config:
        return config[config_name]
    raise ConfigUtilException(f"Configurable {env_name} not in environment nor configuration")


