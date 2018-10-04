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

from unittest.mock import patch

import json
import tempfile

app = Flask(__name__)


with mongo_test_context():
    from predictormanagerservice.app import initialize_app
    initialize_app(app)


def test_endpoints():

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
    with app.test_client() as c:
        r = c.post('/v2/predictors', headers=headers, data=json.dumps(create_data))
        assert r.status_code == 201
        predictor_key = json.loads(r.get_data().decode()).get('predictorKey')

        r = c.get('/v2/predictors')
        assert r.status_code == 200
        assert len(json.loads(r.get_data().decode())) > 0

        r = c.get('/v2/predictors/{}'.format(predictor_key))
        assert r.status_code == 200
        assert json.loads(r.get_data().decode()).get('predictorName') == 'H2O_DEMO'

        r = c.put('/v2/predictors/{}/attributes'.format(predictor_key), headers=headers, data=json.dumps(update_data))
        assert r.status_code == 200
        assert json.loads(r.get_data().decode()).get('description') == 'Updated H2O test predictor'

        r = c.delete('/v2/predictors/{}'.format(predictor_key), headers=headers)
        assert r.status_code == 204
