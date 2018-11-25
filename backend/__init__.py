#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Backend module. 
#
###############################################################################
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import os
import logging

from flask import Flask, request
from flask_cors import CORS
from flask_migrate import Migrate
from sqlalchemy_utils import create_database, database_exists

# postgresql://myinvestor:Money123$@postgres:5432/myinvestordb


