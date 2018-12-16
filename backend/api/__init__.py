#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# HTTP APIs module.
#
###############################################################################

from flask import Blueprint, current_app
from .people import *

# import pprint

main = Blueprint("main", __name__)  # initialize blueprint

@main.route("/")
def index():
    """
    Default response.

    :return: Default response
    """

    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(current_app.config['DATABASE_URI'])
    return current_app.config['DATABASE_URI']
