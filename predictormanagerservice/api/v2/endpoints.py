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
from api.v2.serializers import create_fields, update_fields, predictor_scheduler_fields
from api.v2.parser import error_response_body, error_response_body_500
from api.namespaces import predictors_namespace_v2 as api
from flask_restplus import Resource, abort


def placeholder():
    abort(501, 'Method not yet implemented')


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
          "shareAll": False,
          "subscribedUsers": ["ml1234@att.com"],
          "sharedUsers": ["ml1234@csp.att.com"],
          "sharedRoles": ["admin"],
          "models": [{
            "model_key": "com_att_cmlp_UserId_ST_CMLP_pmmlDecisionTreeIrisDataset",
            "model_version": "1.0"
           }],
          "metadata": [
            {
              "key": "K8S_POD_REPLICAS",
              "value": "2"
            }
          ],
          "customMetadata": [
            {
              "key": "123",
              "value": "today"
            }
          ]
        }
        ```
        """
        placeholder()

    @api.response(200, 'Predictor successfully retrieved')
    @api.response(400, 'Bad Request', error_response_body)
    @api.response(404, 'Invalid Key')
    @api.response(500, 'Unexpected Error', error_response_body_500)
    @api.doc(params={'searchCriteria': ('If searchType is basic, format is a string. If searchType is advanced, '
                                        'format is JSON-encoded key:value pairs, where key is attribute name'),
                     'searchType': 'The type of search. Either basic or advanced.',
                     'patternType': 'The pattern type. Either regex or glob; defaults to regex.'})
    def get(self):
        """
        Returns all predictors in the system that the user is authorized to access. Also supports advanced filtering.
        """
        placeholder()


@api.route('/predictors/<string:predictorKey>')
class PredictorItem(Resource):

    @api.response(200, 'Predictor successfully retrieved')
    @api.response(400, 'Bad Request', error_response_body)
    @api.response(404, 'Invalid Key')
    @api.response(500, 'Unexpected Error', error_response_body_500)
    def get(self, predictorKey):
        """
        Returns the Predictor with predictorKey.
        """
        placeholder()

    @api.response(200, 'Predictor has been updated')
    @api.response(400, 'Bad Request', error_response_body)
    @api.response(404, 'Invalid Key')
    @api.response(415, 'Invalid Data Format')
    @api.response(500, 'Unexpected Error', error_response_body_500)
    @api.expect(update_fields)
    def put(self, predictorKey):
        """
        Updates the Predictor with predictorKey.

        Use this method to change a Predictor.

        * Send a JSON object with only the updated values for the following items in the request body.

        ```
        {
          "description":"This is a test.",
          "shareAll": False,
          "subscribedUsers":
          ["ml1234@att.com"],
          "sharedUsers": ["ml1234@csp.att.com"],
          "sharedRoles": ["admin"],
          "models": [{
            "model_key": "com_att_cmlp_UserId_ST_CMLP_pmmlDecisionTreeIrisDataset",
            "model_version": "1.0"
           }],
          "metadata":[
            {
              "key": "K8S_POD_REPLICAS",
              "value": "2"
            }
          ],
          "customMetadata": [
            {
              "key": "123",
              "value": "today"
            }
          ]
        }
        ```

        * Specify the ID of the Predictor to modify in the request URL path.
        """
        placeholder()

    @api.response(204, 'Predictor successfully deleted')
    @api.response(400, 'Bad Request', error_response_body)
    @api.response(404, 'Invalid Key')
    @api.response(500, 'Unexpected Error', error_response_body_500)
    def delete(self, predictorKey):
        """
        Performs a safe-delete on Predictor with predictorKey.
        """
        placeholder()


@api.route('/predictors/<string:predictorKey>/status')
class PredictorItemById(Resource):
    @api.response(200, 'Predictor status returned')
    @api.response(400, 'Bad Request', error_response_body)
    @api.response(404, 'Invalid Key')
    @api.response(500, 'Unexpected Error', error_response_body_500)
    def get(self, predictorKey):
        """
        Returns the Predictor status with predictorKey.
        """
        placeholder()

    @api.response(200, 'Predictor status returned')
    @api.response(400, 'Bad Request', error_response_body)
    @api.response(404, 'Invalid Key')
    @api.response(500, 'Unexpected Error', error_response_body_500)
    def post(self, predictorKey):
        """
        Updates the status of the predictor and returns the new status
        """
        placeholder()

    @api.hide
    def put(self, predictorKey):
        """
        Internal method called by the task queue
        """
        placeholder()


@api.route('/scoring/<string:scheduleId>')
class ScoringJob(Resource):
    @api.hide
    @api.response(200, 'Scoring job completed successfully')
    @api.response(400, 'Bad Request', error_response_body)
    @api.response(404, 'Invalid Key')
    @api.response(415, 'Invalid Data Format')
    @api.response(500, 'Unexpected Error', error_response_body_500)
    def put(self, scheduleId):
        """
        Batch job to consolidate the Scoring Model for a series of Predictors.
        """
        placeholder()


@api.route('/predictors/<string:predictorKey>/schedules')
class JobScheduleCollection(Resource):
    @api.response(200, 'Scheduled Jobs successfully retrieved')
    @api.response(400, 'Bad Request', error_response_body)
    @api.response(404, 'Invalid Key')
    @api.response(500, 'Unexpected Error', error_response_body_500)
    def get(self, predictorKey):
        """
        Get Scheduled Jobs for Predictor key.
        """
        placeholder()

    @api.response(200, 'Predictor successfully scheduled')
    @api.response(400, 'Bad Request', error_response_body)
    @api.response(500, 'Unexpected Error', error_response_body_500)
    @api.expect(predictor_scheduler_fields)
    def post(self, predictorKey):
        """
        Creates a job schedule for a predictor.
        """
        placeholder()


@api.route('/predictors/<string:predictorKey>/schedules/<string:scheduleId>')
class JobScheduleItem(Resource):
    @api.response(204, 'Schedule successfully deleted')
    @api.response(400, 'Bad Request', error_response_body)
    @api.response(404, 'Invalid Key')
    @api.response(500, 'Unexpected Error', error_response_body_500)
    def delete(self, predictorKey, scheduleId):
        """Delete predictor schedule """
        placeholder()

    @api.response(204, 'Schedule successfully deleted')
    @api.response(400, 'Bad Request', error_response_body)
    @api.response(404, 'Invalid Key')
    @api.response(500, 'Unexpected Error')
    def get(self, predictorKey, scheduleId):
        """Delete predictor schedule """
        placeholder()


@api.route('/predictors/<string:predictorKey>/schedules/<string:scheduleId>/results')
class JobHistory(Resource):
    @api.response(200, 'List of all job histories')
    @api.response(400, 'Bad Request', error_response_body)
    @api.response(404, 'Predictor with predictor key not found')
    @api.response(500, 'Internal Server Error', error_response_body_500)
    def get(self, predictorKey, scheduleId):
        """
        Returns all the Predictor jobs from the job history table for predictorKey, scheduleId
        """
        placeholder()
