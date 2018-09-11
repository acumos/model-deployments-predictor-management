#!/usr/bin/env python3
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

from setuptools import setup, find_packages

version = __import__('predictormanagerservice').get_version()

with open("README.md") as fd:
    long_description = fd.read()

setup(
    author='Pavel Kazakov, Karthic Raghavan, Ryan Hull',
    author_email='pk9069@att.com, rh183@att.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: Apache Software License',
    ],
    description=""""Acumos predictor manager provides the ability to undeploy model
    (predictors) and clean up resources.  Operationalize Models build on popular AI
    tools in the industry """,
    install_requires=['Flask>=1.0.2',
                      'flask-restplus>=0.11.0',
                      'gunicorn>=19.9.0',
                      'flask-cors>=3.0.6'],
    keywords='acumos machine learning model runner server predictor ml ai',
    license='Apache License 2.0',
    long_description=long_description,
    name='predictor-management',
    packages=find_packages(),
    python_requires='>=3.4',
    url='https://gerrit.acumos.org/r/#/admin/projects/model-deployments/predictor-management.git',
    version=version,
)
