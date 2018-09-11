# -*- coding: utf-8 -*-
# ===============LICENSE_START=======================================================
# Acumos Apache-2.0
# ===================================================================================
# Copyright (C) 2017-2018 AT&T Intellectual Property & Tech Mahindra. All rights reserved.
# ===================================================================================
# This Acumos software file is distributed by AT&T and Tech Mahindra
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
from database.models import JobStatus

import pytz


class PredictorParser():
    def __init__(self, predictor):
        self.predictor = predictor

    def as_dict(self):
        predictor = self.predictor

        # TODO (pk9069): move to valid parser
        def parse_model(model):
            return {
                'modelKey': model.model_key,
                'modelVersion': model.model_version
            }

        repo_path = 'http://TODO/REPO/PATH'

        return {
            "predictorKey": predictor.predictor_key,
            "predictorName": predictor.predictor_name,
            "predictorVersion": predictor.predictor_version if hasattr(predictor, 'predictor_version') else -1,
            "repositoryPath":  repo_path + '/' + predictor.service_name() + '.git',
            "predictorType": predictor.predictor_type,
            "description": predictor.description,
            "status": predictor.status.lower(),
            "statusMessage": predictor.status_message if hasattr(predictor, 'status_message') else predictor.status,
            "ingressUrl": predictor.ingress_url if hasattr(predictor, 'ingress_url') else None,
            "createdBy": predictor.created_by,
            "createdDate": predictor.created_date,
            "modifiedDate": predictor.modified_date,
            "models": [parse_model(model) for model in predictor.models],
            "shareAll": True if predictor.share_all.lower() == "true" else False,
            "subscribedUsers": predictor.subscribe_users,
            "sharedUsers": predictor.shared_users,
            "sharedRoles": predictor.shared_roles,
            "metadata": predictor.metadata.as_dict(),
            "customMetadata": predictor.custom_metadata.as_dict(),
        }


class GoalVariableParser():
    def __init__(self, gobal_variable):
        self.goal_variable = gobal_variable

    def as_dict(self):
        return {
            'goalVariable': self.goal_variable.goal_variable,
            'isPrimary': self.goal_variable.is_primary,
        }


class InputFieldParser():
    def __init__(self, input_field):
        self.input_field = input_field

    def as_dict(self):
        return {
            'columnName': self.input_field.column_name,
            'columnValues': self.input_field.column_values,
            'includeInPrediction': self.input_field.include_in_prediction,
            'transformation': self.input_field.transformation,
        }


class PredictorScheduleParser():
    def __init__(self, predictor_schedule):
        self.predictor_schedule = predictor_schedule

    def as_dict(self):
        metadata = self.predictor_schedule.metadata.as_dict() if hasattr(self.predictor_schedule, 'metadata') else []
        start = {
            "year": self.predictor_schedule.scheduled_date_time.year,
            "month": self.predictor_schedule.scheduled_date_time.month,
            "day": self.predictor_schedule.scheduled_date_time.day,
            "hour": self.predictor_schedule.scheduled_date_time.hour,
            "minute": self.predictor_schedule.scheduled_date_time.minute,
        }
        dict_response = {
            "scheduleId": self.predictor_schedule.schedule_id,
            "scheduleName": self.predictor_schedule.schedule_name,
            "scheduleDescription": self.predictor_schedule.schedule_desc,
            "predictorKey": self.predictor_schedule.predictor_key,
            "modelKey": self.predictor_schedule.model_key,
            "modelVersion": self.predictor_schedule.model_version,
            "readDatasetKey": self.predictor_schedule.read_dataset_key,
            "writeDatasetKey": self.predictor_schedule.write_dataset_key,
            "start": start,
            "frequency": self.predictor_schedule.frequency,
            "hourlyIncrement": self.predictor_schedule.hourly_increment,
            "runOnWeekends": self.predictor_schedule.hourly_increment,
            "notificationFlags": self.predictor_schedule.notification_flag,
            "createdTimestamp": self.predictor_schedule.created_date,
            "createdUser": self.predictor_schedule.created_by,
            "metadata": metadata
        }
        return dict_response


class JobHistoryParser():
    def __init__(self, job_history):
        self.job_history = job_history

    def as_dict(self, predictor):
        if hasattr(self.job_history, 'end_date_time'):
            end_date_time = str(self.job_history.end_date_time.replace(tzinfo=pytz.utc))

        return {
            "jobId": self.job_history.job_id,
            "scheduleId": self.job_history.schedule_id,
            "scheduleName": self.job_history.schedule_name,
            # TODO (rk713f) : Ensure following fields are using a uniform utcnow() method
            "startDateTime": str(self.job_history.start_date_time.replace(tzinfo=pytz.utc)),
            "endDateTime": end_date_time,
            "status": JobStatus.as_string(self.job_history.status),
            "statusDescription": self.job_history.status_description,
            "predictorKey": self.job_history.predictor_key,
            "isVerified": self.job_history.is_verified
        }
