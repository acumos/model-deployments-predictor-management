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

from .mock_context import mongo_test_context
from contextlib import contextmanager
from flask import Flask
from werkzeug.exceptions import NotFound

import json
import pytest
import uuid

app = Flask(__name__)


@contextmanager
def business_test_context(**kwargs):
    """Custom test context for mocking out MongoEngine"""

    with mongo_test_context():
        with app.test_request_context(**kwargs):
            from predictormanagerservice.api.v2 import business
            yield business


def test_predictor_crud_workflow():

    with business_test_context() as business:
        with pytest.raises(NotFound):
            # not found should be returned for a predictor that does not exist
            business.get_predictor(str(uuid.uuid4()))


    create_data = {
        'predictorName': "H2O_DEMO",
        'predictorType': "H2OMojo",
        'description': "H2O test predictor"
    }

    update_data = {
        'description': "Updated H2O test predictor"
    }
    headers = {
        'content-type': 'application/json'
    }
    predictor_key = None
    with business_test_context(method='POST', headers=headers, data=json.dumps(create_data)) as business:
        predictor, status_code = business.create_predictor()
        assert status_code == 201
        assert "H2O_DEMO" == predictor['predictorName']
        predictor_key = predictor['predictorKey']

    with business_test_context(method='GET', headers=headers) as business:
        predictor = business.get_predictors()
        assert len(predictor) == 1
        assert predictor[0]['predictorName'] == "H2O_DEMO"
        assert predictor[0]['predictorType'] == "H2OMojo"
        assert predictor[0]['description'] == "H2O test predictor"

    with business_test_context(method='GET', headers=headers) as business:
        predictor = business.get_predictor(predictor_key)
        assert predictor['predictorName'] == "H2O_DEMO"
        assert predictor['predictorType'] == "H2OMojo"
        assert predictor['description'] == "H2O test predictor"

    with business_test_context(method='PUT', headers=headers, data=json.dumps(update_data)) as business:
        predictor = business.update_predictor_attributes(predictor_key)
        assert predictor['predictorName'] == "H2O_DEMO"
        assert predictor['predictorType'] == "H2OMojo"
        assert predictor['description'] == "Updated H2O test predictor"


    with business_test_context(method='DELETE', headers=headers) as business:
        predictor = business.delete_predictor(predictor_key)

    with business_test_context() as business:
        with pytest.raises(NotFound):
            business.get_predictor(predictor_key)
