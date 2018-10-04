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
from predictormanagerservice.api.namespaces import predictors_namespace as api

create_fields = api.model('CreatePredictor', {
    'predictorName': fields.String(required=True, description='Name of the Predictor.', example='PMMLPredictor'),
    'predictorType': fields.String(required=True, example='PMML'),
    'description': fields.String(required=True, description='Description of current Predictor',
                                 example='This is a test.'),

})


update_fields = api.model('UpdatePredictor', {
    'description': fields.String(required=True, description='Description of current Predictor',
                                 example='This is a test.'),
})


