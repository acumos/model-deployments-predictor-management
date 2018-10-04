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

from .config_util import get_config_value

from enum import Enum
from flask_restplus import abort, Resource
from http import HTTPStatus

from werkzeug.exceptions import BadRequest


PREFIX_NAME = 'error_prefix'
SECTION_NAME = 'RESPONSES'


class ErrorId(Enum):
    GENERIC_ERROR = '0001'
    INVALID_INPUT = '0002'
    INVALID_INPUT_ENUMS = '0003'
    MISSING_MANDATORY_PARAMETER = '0004'

    FORBIDDEN = '0103'
    UNAUTHORIZED = '0101'
    NOT_FOUND = '0104'
    METHOD_NOT_ALLOWED = '0105'
    REQUEST_ENTITY_TOO_LARGE = '0113'

    INTERNAL_SERVER_ERROR = '0200'


def get_error_prefix():
    return get_config_value(PREFIX_NAME, section=SECTION_NAME)


def generate_error_id_string(code):
    return get_error_prefix() + '-' + code.value


class ACUMOSResource(Resource):
    def _handle_bad_request(self, br):
        data = br.data

        message = data.get('message', br.description)
        variables = []

        # TODO (pk9069): validate
        if 'errors' in data:
            errors = data.get('errors')
            message += '. Expected values:'
            for i, name in enumerate(errors):
                if name == '':
                    message = errors[name]
                    break
                else:
                    message += (f' %{i + 1}')
                    variables.append(name)

        response_data = {
            'errorId': generate_error_id_string(ErrorId.INVALID_INPUT),
            'message': message
        }
        if variables:
            response_data['variables'] = variables
        abort(HTTPStatus.BAD_REQUEST.value, **response_data)

    def validate_payload(self, func):
        try:
            super().validate_payload(func)
        except BadRequest as br:
            if not hasattr(br, 'data'):
                error_id = generate_error_id_string(ErrorId.GENERIC_ERROR)
                abort(HTTPStatus.BAD_REQUEST.value, br.description, errorId=error_id)
            self._handle_bad_request(br)


def error_response(status_code, message, error_id=ErrorId.GENERIC_ERROR, variables=None, error_url=None):
    response = {
        'errorId': generate_error_id_string(error_id)
    }
    if variables is not None:
        response['variables'] = variables

    if error_url is not None:
        response['errorUrl'] = error_url

    abort(status_code, message, **response)


def forbidden(message, error_id=ErrorId.FORBIDDEN, variables=None, error_url=None):
    status_code = HTTPStatus.FORBIDDEN.value
    error_response(status_code, message, error_id=error_id, variables=variables, error_url=error_url)


def unauthorized(message=None, error_id=ErrorId.UNAUTHORIZED, variables=None, error_url=None):
    if message is None:
        message = HTTPStatus.UNAUTHORIZED.phrase
    status_code = HTTPStatus.UNAUTHORIZED.value
    error_response(status_code, message, error_id=error_id, variables=variables, error_url=error_url)


def bad_request(message, error_id=ErrorId.GENERIC_ERROR, variables=None, error_url=None):
    status_code = HTTPStatus.BAD_REQUEST.value
    error_response(status_code, message, error_id=error_id, variables=variables, error_url=error_url)


def not_found(message=None, error_id=ErrorId.NOT_FOUND, variables=None, error_url=None):
    if message is None:
        message = HTTPStatus.NOT_FOUND.phrase
    status_code = HTTPStatus.NOT_FOUND.value
    error_response(status_code, message, error_id=error_id, variables=variables, error_url=error_url)


def request_entity_too_large(message=None, error_id=ErrorId.REQUEST_ENTITY_TOO_LARGE, variables=None, error_url=None):
    if message is None:
        message = HTTPStatus.REQUEST_ENTITY_TOO_LARGE.phrase
    status_code = HTTPStatus.REQUEST_ENTITY_TOO_LARGE.value
    error_response(status_code, message, error_id=error_id, variables=variables, error_url=error_url)


def method_not_allowed(message=None, error_id=ErrorId.METHOD_NOT_ALLOWED, variables=None, error_url=None):
    if message is None:
        message = HTTPStatus.METHOD_NOT_ALLOWED.phrase
    status_code = HTTPStatus.METHOD_NOT_ALLOWED.value
    error_response(status_code, message, error_id=error_id, variables=variables, error_url=error_url)


def ok_response(message):
    response = message
    if isinstance(message, str):
        response = {'message': message}
    return response


def accepted_response(message, status_path, additional_values=None):
    link = get_config_value('microservice_url', section='SERVICES') + status_path
    response = {
        'message': message,
        'link': link
    }
    if additional_values is not None:
        response.update(additional_values)
    return response, HTTPStatus.ACCEPTED.value


def created_response(body, resource_path, additional_headers=None):
    """
    Generates a CREATED HTTP response conforming to AT&T REST standards.

    The location header is set by concatinating the microservice_url and resource_path.
    """
    location = get_config_value('microservice_url', section='SERVICES') + resource_path
    headers = {'location': location}
    if additional_headers is not None:
        headers.update(additional_headers)
    return body, HTTPStatus.CREATED.value, headers


def no_content_response():
    return '', HTTPStatus.NO_CONTENT.value
