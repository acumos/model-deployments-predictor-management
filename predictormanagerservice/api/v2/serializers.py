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
from api.namespaces import predictors_namespace_v2 as api

metadata_fields = api.model('Metadata', {
    'key': fields.String(required=True, description='Key used in metadata entry.', example='K8S_POD_REPLICAS'),
    'value': fields.String(required=True, description='Value used in metadata entry.', example='2')
})

input_field = api.model('InputField', {
    "columnName": fields.String(required=True, description='The input field name', example='sepal_length'),
    "columnValues": fields.List(
        fields.Float(),
        description='User inputs comma seperated values for column name',
        example=[4.3]
    ),
    "includeInPrediction": fields.Boolean(
        required=False,
        default=True,
        description='Boolean flag used to determine whether field is used to make prediction',
        example=True
    ),
    "transformation": fields.String(
        required=False,
        default=None,
        description='Transformation rule applied to this column. masked' ' [OR] fillNa [OR] 1+1*5 [OR] ""  ',
        example="masked"
    )

})

goal_variables = api.model('GoalVariable', {
    "goalVariable": fields.String(required=True, description='Model version', example="sepal_length"),
    "isPrimary": fields.Boolean(required=True, description='primary field or secondary field', example=True)
})


model_fields = api.model('ModelFields', {
    'modelKey': fields.String(required=True, description='Model key to associate with predictor',
                              example='com_att_cmlp_m09286_ST_CMLP_pmmlDecisionTreeIrisDataset'),
    'modelVersion': fields.String(required=True, description='Model version', example="1")
})

scheduled_datetime_field = api.model('ScheduleDateFields', {
    'year': fields.Integer(required=True, description='Year to schedule predictor', example=2019),
    'month': fields.Integer(required=True, description='Month to schedule predictor', example=1),
    'day': fields.Integer(required=True, description='Day to schedule predictor', example=1),
    'hour': fields.Integer(required=True, description='Hour to schedule predictor', example=22),
    'minute': fields.Integer(required=True, description='Minute to schedule predictor', example=34),
})

create_fields = api.model('CreatePredictor', {
    'predictorName': fields.String(required=True, description='Name of the Predictor.', example='PMMLPredictor'),
    'predictorType': fields.String(required=True, example='PMML'),
    'description': fields.String(required=True, description='Description of current Predictor',
                                 example='This is a test.'),
    'shareAll': fields.Boolean(required=False, description='Whether to share predictor with everyone', example=False),
    'subscribedUsers': fields.List(fields.String(required=False, description='', example='["mw055d@csp.att.com"]')),
    'sharedUsers': fields.List(fields.String(required=False, description='', example='["mw055d@csp.att.com"]')),
    'sharedRoles': fields.List(fields.String(required=False, description='', example='["admin"]')),
    'models': fields.List(fields.Nested(model_fields)),
    'metadata': fields.List(fields.Nested(metadata_fields)),
    'customMetadata': fields.List(fields.Nested(metadata_fields))
})


update_fields = api.model('UpdatePredictor', {
    'description': fields.String(required=True, description='Description of current Predictor',
                                 example='This is a test.'),
    'shareAll': fields.Boolean(required=False, description='', example=False),
    'subscribeUsers': fields.List(fields.String(required=False, description='', example='["mw055d@csp.att.com"]')),
    'sharedUsers': fields.List(fields.String(required=False, description='', example='["mw055d@csp.att.com"]')),
    'sharedRoles': fields.List(fields.String(required=False, description='', example='["user"]')),
    'models': fields.List(fields.Nested(model_fields)),
    'metadata': fields.List(fields.Nested(metadata_fields)),
    'customMetadata': fields.List(fields.Nested(metadata_fields))
})


predictor_scheduler_fields = api.model('PredictorSchedule', {
    'scheduleName': fields.String(required=True, description='Name for the scheduling job', example="Schedule1"),
    'scheduleDescription': fields.String(required=True, description='A description of the scheduling job',
                                         example="Schedule1 description."),
    'modelKey': fields.String(required=True, description='Model key for the scheduling job',
                              example="com_att_cmlp_m09286_ST_CMLP_pmmlDecisionTreeIrisDataset"),
    'modelVersion': fields.String(required=True, description='Model version for the scheduling job', example="1"),
    'readDatasetKey': fields.String(required=False, description='Dataset key for scoring', example="tmp"),
    'writeDatasetKey': fields.String(required=False, description='Dataset key for writing results', example="tmp"),
    'start': fields.Nested(scheduled_datetime_field),
    'runOnWeekends': fields.String(required=True, description='Whether to run on weekends', example='N'),
    'notificationFlag': fields.String(required=True, description='The notification flag', example='NOTIFYALL'),
    'hourly_increment': fields.Integer(required=False, description='Hourly increment for hourly schedule', example=2),
    'metadata': fields.List(fields.Nested(metadata_fields), required=False),
    'frequency': fields.String(required=True, description='Frequency of running the schedule', example='daily'),
})
