#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Backend module. 
#
###############################################################################

import os
import logging
import connexion

from flask import Flask, request
from flask_cors import CORS

from backend.api import main
from backend.config import config

class RequestFormatter(logging.Formatter):
    def format(self, record):
        record.url = request.url
        record.remote_addr = request.remote_addr
        return super().format(record)

def create_app(test_config=None):
    """
    Flask application factories - http://flask.pocoo.org/docs/1.0/patterns/appfactories/

    :param test_config: Test configuration file.
    :return app: Flask app object.
    """

    # Environment variable to configure the config to use
    _FLASK_ENV_ = 'FLASK_ENV'

    # app = Flask(__name__)
    connexionApp = connexion.App(__name__, specification_dir='../')

    # Read the swagger.yml file to configure the endpoints
    connexionApp.add_api('swagger.yml')

    # Add CORS
    CORS(connexionApp.app)

    # check environment variables to see which config to load
    env = os.environ.get(_FLASK_ENV_, "docker")

    # for configuration options, look at config.py
    if test_config:
        # purposely done so we can inject test configurations
        # this may be used as well if you'd like to pass
        # in a separate configuration although I would recommend
        # adding/changing it in api/config.py instead
        # ignore environment variable config if config was given
        connexionApp.app.config.from_mapping(**test_config)
    else:
        connexionApp.app.config.from_object(config[env])

    # logging format
    formatter = RequestFormatter(
        "%(asctime)s %(remote_addr)s: requested %(url)s: %(levelname)s in [%(module)s: %(lineno)d]: %(message)s"
    )

    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(app.config)

    # import and register blueprints
    connexionApp.app.register_blueprint(main)

    return connexionApp.app


app = create_app()
