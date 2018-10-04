.. ===============LICENSE_START=======================================================
.. Acumos CC-BY-4.0
.. ===================================================================================
.. Copyright (C) 2017-2018 AT&T Intellectual Property. All rights reserved.
.. ===================================================================================
.. This Acumos documentation file is distributed by AT&T
.. under the Creative Commons Attribution 4.0 International License (the "License");
.. you may not use this file except in compliance with the License.
.. You may obtain a copy of the License at
..
..      http://creativecommons.org/licenses/by/4.0
..
.. This file is distributed on an "AS IS" BASIS,
.. WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
.. See the License for the specific language governing permissions and
.. limitations under the License.
.. ===============LICENSE_END=========================================================

===================================================
Acumos Predictor Management Python Developer Guide
===================================================
This service stores the predictor details in a mongo DB and provides crud operations on the predictor resources.  The connection to mongodb can be configured by passing in a settings.cfg either as a parameter on command line or using the one stored in the properties folder and setting with the correct values.

The main class to start this service is /predictor-management/run.py

The command line interface gives options to run the application.   Type help for a list of available options.   
> python run.py  help
usage: run.py [-h] [--host HOST] [--settings SETTINGS]  [--port PORT]

By default without adding arguments the swagger interface should be available at: http://localhost:8085/v2/

Testing
=======

The only prerequisite for running testing is installing python and tox.   It is recommended to use a virtual environment for running any python application.  If using a virtual environment make sure to run “pip install tox” to install it

We use a combination of ``tox``, ``pytest``, and ``flake8`` to test
``predictor-management``. Code which is not PEP8 compliant (aside from E501) will be
considered a failing test. You can use tools like ``autopep8`` to
“clean” your code as follows:

.. code:: bash

    $ pip install autopep8
    $ cd predictor-management
    $ autopep8 -r --in-place --ignore E501 predictormanagerservice/ test/ 

Run tox directly:

.. code:: bash

    $ cd predictor-management
    $ tox

You can also specify certain tox environments to test:

.. code:: bash

    $ tox -e py34  # only test against Python 3.4
    $ tox -e flake8  # only lint code

And finally, you can run pytest directly in your environment *(recommended starting place)*:

.. code:: bash

    $ pytest
    $ pytest -s   # verbose output
