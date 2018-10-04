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

from acumoscommon.responses import not_found, no_content_response, created_response, bad_request
from predictormanagerservice.database.models import PredictorDocument, PredictorStatus
from flask import request
from predictormanagerservice.predictors.predictors import get_all_predictor_types, PredictorType
from predictormanagerservice.api.v2.parsers import PredictorParser


from acumoscommon.responses import ErrorId

import json
import logging
import uuid
import pytz
import uuid
from datetime import datetime

logger = logging.getLogger(__name__)


def _get_predictor_object(key):
    item = PredictorDocument.objects.filter(predictor_key=key).first()
    if item is None:
        not_found("Predictor with key {} not found".format(key))
    return item

def create_predictor():

    obj = request.get_json()
    if not obj.get("predictorName", ""):
        bad_request("predictorName is required")

    predictor_type = obj.get('predictorType', None)

    if predictor_type not in get_all_predictor_types():
        bad_request('Invalid predictor_type %1.', variables=[predictor_type], error_id=ErrorId.INVALID_INPUT_ENUMS)

    predictor = PredictorDocument()
    predictor.document_id = str(uuid.uuid4())
    predictor.predictor_name = obj["predictorName"]
    predictor.predictor_type = predictor_type
    predictor.description = obj["description"]
    predictor.predictor_endpoint = None
    
    now = str(datetime.utcnow().replace(tzinfo=pytz.utc))
    predictor.predictor_key = str(datetime.now().strftime("%Y%m%d%H%M%S"))
    predictor.created_date = now
    predictor.modified_date = now
    predictor.status = PredictorStatus.INITIALIZING
    
    predictor.save()

    return PredictorParser(predictor).as_dict(), 201


def get_predictors():
    predictors = PredictorDocument.objects.all()
    return [PredictorParser(predictor).as_dict() for predictor in predictors]


def get_predictor(predictor_key):
    predictor = _get_predictor_object(predictor_key)
    return PredictorParser(predictor).as_dict()


def delete_predictor(predictor_key):
    predictor = _get_predictor_object(predictor_key)
    predictor.delete()
    return no_content_response()


def update_predictor_attributes(predictor_key):
    predictor = _get_predictor_object(predictor_key)
    obj = request.get_json()
    if obj is None:
        bad_request('Request must be application/json')

    # only updating the description is currently allowed
    predictor.description = obj.get('description')
    predictor.save()

    return PredictorParser(predictor).as_dict()



