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

from datetime import datetime
from enum import Enum
from flask_mongoengine import MongoEngine
import uuid
import pytz
from predictormanagerservice.api.config_util import generate_predictor_key

db = MongoEngine()


def utcnow():
    return datetime.utcnow().replace(tzinfo=pytz.utc)


class PredictorStatus:
    ACTIVE = "active"
    INITIALIZING = "initializing"
    UPDATING = "updating"
    FAILED = "failed"
    INACTIVE = "inactive"

class PredictorDocument(db.Document):
    document_id = db.StringField()
    predictor_key = db.StringField()
    predictor_name = db.StringField()
    predictor_type = db.StringField()
    predictor_version = db.FloatField(required=False)
    description = db.StringField()
    status = db.StringField()
    status_message = db.StringField(required=False)
    created_date = db.StringField()
    modified_date = db.StringField()
    predictor_endpoint = db.StringField(required=False)


    def as_dict(self):
        response = {
            "predictor_key": self.predictor_key,
            "predictor_name": self.predictor_name,
            "predictor_type": self.predictor_type,
            "description": self.description,
            "status": self.status.lower(),
            "predictor_endpoint": self.predictor_endpoint if hasattr(self, 'predictor_endpoint') else None,
            "created_date": self.created_date,
            "modified_date": self.modified_date

        }
        return response

