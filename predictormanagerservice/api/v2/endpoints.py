# ===============LICENSE_START=======================================================
# Acumos Apache-2.0
# ===================================================================================
# Copyright (C) 2018 AT&T Intellectual Property. All rights reserved.
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

from flask_restplus import Resource, abort

from predictormanagerservice.api.v2.business import create_predictor, get_predictor, get_predictors, \
update_predictor_attributes, delete_predictor
from predictormanagerservice.api.namespaces import predictors_namespace as api
from predictormanagerservice.api.v2.serializers import create_fields, update_fields
from predictormanagerservice.api.v2.parsers import error_response_body, error_response_body_500, PredictorParser


@api.route('/predictors')
class PredictorCollection(Resource):
    @api.response(202, 'Accepted')
    @api.response(400, 'Bad Request', error_response_body)
    @api.response(403, 'Unauthorized')
    @api.response(415, 'Invalid Data Format')
    @api.response(500, 'Unexpected Error: The Predictor was not created', error_response_body_500)
    @api.expect(create_fields)
    def post(self):
        """
        Deploy a model

        * Send a JSON object with values for the following items in the request body.

        ```
        {
          "predictorName": "Predict1",
          "description":"This is a test.",
        }
        ```
        """
        return create_predictor()


    @api.response(200, 'Predictor successfully retrieved')
    @api.response(400, 'Bad Request', error_response_body)
    @api.response(404, 'Invalid Key')
    @api.response(500, 'Unexpected Error', error_response_body_500)

    def get(self):
        """
        Returns all predictors in the system that the user is authorized to access.
        """
        return get_predictors()


@api.route('/predictors/<string:predictorKey>')
@api.response(500, 'Unexpected Error')
class PredictorItem(Resource):
    @api.response(204, 'No Content')
    def delete(self, predictorKey):
        """
        Delete Model with modelKey
        """
        return delete_predictor(predictorKey)

    @api.response(200, 'Predictor successfully retrieved')
    @api.response(400, 'Bad Request')
    @api.response(401, 'Not Authorized')
    @api.response(403, 'Forbidden')
    @api.response(404, 'Invalid Key')
    @api.response(500, 'Unexpected Error')
    def get(self, predictorKey):
        """
        Retrieves Predictor with predictorlKey
        """
        return get_predictor(predictorKey)


@api.route('/predictors/<string:predictorKey>/attributes')
@api.response(500, 'Unexpected Error')
class PredictorAttributesResource(Resource):
    @api.response(200, 'OK')
    @api.response(400, 'Bad Request')
    @api.response(404, 'Not Found')
    def put(self, predictorKey):
        """
        Update Predictor attributes for the model using the specified predictor key
        """
        return update_predictor_attributes(predictorKey)
