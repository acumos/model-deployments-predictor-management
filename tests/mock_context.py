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
from contextlib import contextmanager
from datetime import datetime
from unittest.mock import patch

import pytz


class MockedFilteredResult():
    def __init__(self, objects=None):
        self.objects = objects

    def first(self):
        if self.objects is not None:
            return self.objects[0]
        return None


class MockedFilter():
    def __init__(self):
        self.mocked_predictors = {}

    def filter(self, predictor_key=None):
        if predictor_key in self.mocked_predictors:
            return MockedFilteredResult([self.mocked_predictors[predictor_key]])
        return MockedFilteredResult()

    def all(self):
        return self.mocked_predictors.values()

    def put(self, predictor_key, predictor):
        self.mocked_predictors[predictor_key] = predictor

    def delete(self, predictor_key):
        del self.mocked_predictors[predictor_key]


class MockedPredictorDocument():
    objects = MockedFilter()

    def __init__(self, predictor_key=None):
        self.predictor_key = predictor_key
        self.description = None
        self.predictor_type = None


    def save(self):
        self.objects.put(self.predictor_key, self)

    def delete(self):
        self.objects.delete(self.predictor_key)


@contextmanager
def mongo_test_context():
    """Custom test context for mocking out MongoEngine"""

    with patch('flask_mongoengine.MongoEngine'):
        with patch('predictormanagerservice.database.models.PredictorDocument', new=MockedPredictorDocument):
            yield
