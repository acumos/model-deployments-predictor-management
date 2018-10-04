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


from acumoscommon.responses import error_response, bad_request, not_found, created_response, \
    no_content_response
from flask import Flask
from werkzeug.exceptions import BadRequest

import pytest


app = Flask(__name__)


def test_error_response():
    with app.test_request_context():
        with pytest.raises(BadRequest):
            error_response(400, 'test')

def test_bad_request():
    with app.test_request_context():
        with pytest.raises(BadRequest):
            bad_request('test')
