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

To setup MongoDB for testing please visit https://docs.mongodb.com/manual/administration/install-on-linux/

As mentioned in the database install guide these are the settings in properties/settings.cfg that are needed to connect to a mongo instance.

.. code:: bash

    $ [MONGO]
    $ mongo_dbname = TEST_DB
    $ mongo_username = someuser
    $ mongo_password = dummy
    $ mongo_host = localhost
    $ mongo_port = 27017

There are many guides for installing Mongo but a general setup may go something like this:

Set up the config file for MongoDB
\Path\to\Mongo\MongoDB\Server\3.2\mongod.cfg
.. code:: bash

    $ 
    $ systemLog:
    $     destination: file
    $     path: \location\data\log\
    $ storage:
    $     dbPath: \location\data\db

Start the mongo service from command line

.. code:: bash

    $ # Create admin user
    $ use admin
    $ db.createUser( { user: "admin", pwd: "password", roles: [{ role: "dbOwner", db: "admin" }] } )
    $ 
    $ # Create Database and user login for dbOwner
    $ use ACUMOS_DB
    $ db.createUser( { user: "someuser", pwd: "**ChangeMe**", roles: [{ role: "dbOwner", db: "ACUMOS_DB" }] } )
    $ 
    $ # Validate credentials login
    $ db.auth("someuser", "**ChangeMe***")
    $ show collections
    $ 
    $ # Start mongo with auth to mimic TEST
    $ mongod —auth —dbpath data/db
    $ 
    $ # Login and test user
    $ mongo
    $ use ACUMOS_DB
    $ db.auth("someuser", "**ChangeMe**", ")
    $ db.predictorcatalog.insert( {"predictorKey":"ABC123", "notes": "Hello World" })  #this is optional
    $ exit

Once it is setup then make sure to start it with auth enabled

net stop MongoDB <- To kill stop it if its already running

mongod --auth --port 27017 


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
