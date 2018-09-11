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

from flask_restplus import fields
from api.namespaces import predictors_namespace_v2 as api

error_response_body = api.model('Error Response - General', {
    'errorId': fields.String(description='Identifier for the error.',
                             required=True,
                             example="PRED-0003"),
    'message': fields.String(description='Brief description about the error.',
                             required=True,
                             example="Invalid Value for parameter(s), %1, %2"),
    'variable': fields.List(fields.String, description='Values for the parameters in the error message field.',
                            required=False,
                            example="['modelKey', 'modelVersion']"),
    'errorUrl': fields.String(description='Url to a web page where there is detailed information \
    about the cause and resolution for the given error.',
                              required=False,
                              example="https://acumos.org/error/pred-0001"),
})


error_response_body_500 = api.model('Error Response - 500', {
    'errorId': fields.String(description='Identifier for the error.',
                             required=True,
                             example="PRED-0001"),
    'message': fields.String(description='Brief description about the error.',
                             required=True,
                             example="Please provide the reference id ( %1 ) to the support team"),
    'variable': fields.List(fields.String,
                            description='The unique error reference id to be provided to the support team.',
                            required=False,
                            example="['24234234234234']"),
    'errorUrl': fields.String(description='Url to a web page where there is detailed information \
    about the cause and resolution for the given error.',
                              required=False,
                              example="https://acumos.org/error/pred-0001"),
})
