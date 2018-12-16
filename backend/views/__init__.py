#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Views module.
#
###############################################################################

from flask import Blueprint, current_app, render_template

views = Blueprint("views", __name__, template_folder="./")  # initialize blueprint

@views.route("/")
def index():
    """
    Default response.

    :return: Default response
    """

    render_template("index.html")
