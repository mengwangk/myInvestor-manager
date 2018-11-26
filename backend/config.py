#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Configurations for dev and prod. 
#
###############################################################################

import os

class Config(object):
    LOG_FILE = 'myinvestor.log'

class ProductionConfig(Config):
    DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = False


class DockerDevConfig(Config):
    DATABASE_URI =  os.environ.get("DATABASE_URL")
    DEBUG = True

config = {"production": ProductionConfig, "development": DockerDevConfig}
