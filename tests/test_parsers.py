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


from predictormanagerservice.api.v2.parsers import PredictorParser
from datetime import datetime

import pytz


class MockedPredictorDocument():
    def __init__(self):
        self.predictor_key = '1234'
        self.predictor_name = 'name1'
        self.predictor_version = '1234'
        self.predictor_type = 'H2O'
        self.description = 'Mock Desc'
        self.status = 'test'


def test_as_dict():
    parsed_dict = PredictorParser(MockedPredictorDocument()).as_dict()
    assert parsed_dict.get('predictorKey') == '1234'
    assert parsed_dict.get('predictorName') == 'name1'
    assert parsed_dict.get('predictorVersion') == '1234'
    assert parsed_dict.get('predictorType') == 'H2O'
    assert parsed_dict.get('description') == 'Mock Desc'
    assert parsed_dict.get('status') == 'test'
    
    

