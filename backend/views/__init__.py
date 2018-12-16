#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Views module.
#
###############################################################################

from flask import Blueprint, current_app

views = Blueprint("views", __name__)  # initialize blueprint

@views.route("/")
def index():
    """
    Default response.

    :return: Default response
    """

    return "hello"
