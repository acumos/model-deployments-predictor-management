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

import logging


logger = logging.getLogger(__name__)


class PredictorException(Exception):
    pass


class PredictorScoringException(Exception):
    pass


class PredictorType():
    TYPE_CMLPSTUDIO = 'CMLPStudio'
    TYPE_H2O_POJO = 'H2OPojo'
    TYPE_H2O_MOJO = 'H2OMojo'
    TYPE_RDS = "RDS"


class BasePredictor():
    """Base class for all predictors"""

    def __init__(self, predictor_model):
        self._predictor_model = predictor_model



class H2OPredictor(BasePredictor):
    pass


class RDSPredictor(BasePredictor):
    pass



_predictor_mappings = {
    PredictorType.TYPE_H2O_POJO: lambda model: H2OPredictor(model),
    PredictorType.TYPE_H2O_MOJO: lambda model: H2OPredictor(model),
    PredictorType.TYPE_RDS: lambda model: RDSPredictor(model)
}


def get_predictor_instance(predictor_model):
    predictor_type = predictor_model.predictor_type
    if predictor_type not in _predictor_mappings.keys():
        raise PredictorException(f'Predictor type {predictor_type} not found.')
    return _predictor_mappings[predictor_type](predictor_model)


def get_all_predictor_types():
    return [key for key in _predictor_mappings.keys()]
