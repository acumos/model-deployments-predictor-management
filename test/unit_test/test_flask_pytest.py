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
from os.path import dirname, realpath, join
import sys
import pytest
import json
parentddir = dirname(dirname(dirname(realpath(__file__))))
sys.path.append(join(parentddir, 'predictormanagerservice'))

from predictormanagerservice.app import app, initialize_app


BASE_URL = 'http://127.0.0.1:8061/v2/'


@pytest.fixture(scope='session')
def test_client():
    testing_client = app.test_client()
    initialize_app(testing_client)
    testing_client.testing = True
    return testing_client


# @api.route('/predictors)
def test_get_predictors(test_client):
    response = test_client.get(BASE_URL + 'predictors?searchCriteria=test&searchType=test&patternType=test')
    assert response.status_code == 501
    assert json.loads(response.get_data())['message'] == 'Method not yet implemented'


# @api.route('/predictors/<string:predictorKey>')
def test_delete_predictors_key(test_client):
    response = test_client.delete(BASE_URL + 'predictors/dummyKey')
    assert response.status_code == 501
    assert json.loads(response.get_data())['message'] == 'Method not yet implemented'


# @api.route('/predictors/<string:predictorKey>')
def test_get_predictors_key(test_client):
    response = test_client.get(BASE_URL + 'predictors/dummyKey')
    assert response.status_code == 501
    assert json.loads(response.get_data())['message'] == 'Method not yet implemented'


# @api.route('/predictors/<string:predictorKey>/schedules')
def test_get_predictors_key_schedules(test_client):
    response = test_client.get(BASE_URL + 'predictors/dummyKey/schedules')
    assert response.status_code == 501
    assert json.loads(response.get_data())['message'] == 'Method not yet implemented'


# @api.route('/predictors/<string:predictorKey>/schedules/<string:scheduleId>')
def test_delete_predictors_key_schedules_scheduleid(test_client):
    response = test_client.delete(BASE_URL + 'predictors/dummyKey/schedules/dummyId')
    assert response.status_code == 501
    assert json.loads(response.get_data())['message'] == 'Method not yet implemented'


# @api.route('/predictors/<string:predictorKey>/schedules/<string:scheduleId>')
def test_get_predictors_key_schedules_scheduleid(test_client):
    response = test_client.get(BASE_URL + 'predictors/dummyKey/schedules/dummyId')
    assert response.status_code == 501
    assert json.loads(response.get_data())['message'] == 'Method not yet implemented'


# @api.route('/predictors/<string:predictorKey>/schedules/<string:scheduleId>/results')
def test_get_predictors_key_schedules_scheduleid_results(test_client):
    response = test_client.get(BASE_URL + 'predictors/dummyKey/schedules/dummyId/results')
    assert response.status_code == 501
    assert json.loads(response.get_data())['message'] == 'Method not yet implemented'


# @api.route('/predictors/<string:predictorKey>/status')
def test_post_status(test_client):
    response = test_client.post(BASE_URL + 'predictors/predictorKey/status')
    assert response.status_code == 501
    assert json.loads(response.get_data())['message'] == 'Method not yet implemented'


# @api.route('/predictors/<string:predictorKey>/status')
def test_get_status(test_client):
    response = test_client.get(BASE_URL + 'predictors/predictorKey/status')
    assert response.status_code == 501
    assert json.loads(response.get_data())['message'] == 'Method not yet implemented'


# @api.route('/predictors/<string:predictorKey>/schedules')
def test_post_predictors_key_schedule(test_client):

    body = {
        "scheduleName": "Schedule1",
        "scheduleDescription": "Schedule1 description.",
        "modelKey": "com_att_cmlp_m09286_ST_CMLP_pmmlDecisionTreeIrisDataset",
        "modelVersion": "1",
        "readDatasetKey": "tmp",
        "writeDatasetKey": "tmp",
        "start": {
          "year": 2019,
          "month": 1,
          "day": 1,
          "hour": 22,
          "minute": 34
        },
        "runOnWeekends": "N",
        "notificationFlag": "NOTIFYALL",
        "hourly_increment": 2,
        "metadata": [
          {
            "key": "K8S_POD_REPLICAS",
            "value": "2"
          }
        ],
        "frequency": "daily"
    }

    request_headers = {
        'content-type': 'application/json',
        'accept': 'application/json',
        'Authorization': 'Basic password',
    }

    response = test_client.post(BASE_URL + 'predictors/dummyKey/schedules',
                                data=json.dumps(body), headers=request_headers)
    assert response.status_code == 501
    assert json.loads(response.get_data())['message'] == 'Method not yet implemented'


# @api.route('/predictors)
def test_post_predictors(test_client):

    body = {
        "predictorName": "PMMLPredictor",
        "predictorType": "PMML",
        "description": "This is a test.",
        "shareAll": True,
        "subscribedUsers": [
          "[\"mw055d@csp.att.com\"]"
        ],
        "sharedUsers": [
          "[\"mw055d@csp.att.com\"]"
        ],
        "sharedRoles": [
          "[\"admin\"]"
        ],
        "models": [
          {
            "modelKey": "com_att_cmlp_m09286_ST_CMLP_pmmlDecisionTreeIrisDataset",
            "modelVersion": "1"
          }
        ],
        "metadata": [
          {
            "key": "K8S_POD_REPLICAS",
            "value": "2"
          }
        ],
        "customMetadata": [
          {
            "key": "K8S_POD_REPLICAS",
            "value": "2"
          }
        ]
    }

    request_headers = {
        'content-type': 'application/json',
        'accept': 'application/json',
        'Authorization': 'Basic password',
    }

    response = test_client.post(BASE_URL + 'predictors',
                                data=json.dumps(body), headers=request_headers)
    assert response.status_code == 501
    assert json.loads(response.get_data())['message'] == 'Method not yet implemented'


# @api.route('/predictors/<string:predictorKey>')
def test_put_predictors_key(test_client):

    body = {
        "description": "This is a test.",
        "shareAll": True,
        "subscribeUsers": [
          "[\"mw055d@csp.att.com\"]"
        ],
        "sharedUsers": [
          "[\"mw055d@csp.att.com\"]"
        ],
        "sharedRoles": [
          "[\"user\"]"
        ],
        "models": [
          {
            "modelKey": "com_att_cmlp_m09286_ST_CMLP_pmmlDecisionTreeIrisDataset",
            "modelVersion": "1"
          }
        ],
        "metadata": [
          {
            "key": "K8S_POD_REPLICAS",
            "value": "2"
          }
        ],
        "customMetadata": [
          {
            "key": "K8S_POD_REPLICAS",
            "value": "2"
          }
        ]
    }

    request_headers = {
        'content-type': 'application/json',
        'accept': 'application/json',
        'Authorization': 'Basic password',
    }

    response = test_client.put(BASE_URL + 'predictors/dummyKey',
                               data=json.dumps(body), headers=request_headers)
    assert response.status_code == 501
    assert json.loads(response.get_data())['message'] == 'Method not yet implemented'
