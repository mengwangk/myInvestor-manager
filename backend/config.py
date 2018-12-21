#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Configurations for dev and prod. 
#
###############################################################################

import os
import logging

class Config(object):
    LOG_FILE = 'myinvestor.log'

class ProductionConfig(Config):
    """
    Production configuration.
    """
    DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = False
    LOG_LEVEL = logging.ERROR


class DockerDevConfig(Config):
    """
    Docker development configuration.
    """
    DATABASE_URI =  os.environ.get("DATABASE_URL")
    DEBUG = True
    LOG_LEVEL = logging.DEBUG

# Config map
config = {"production": ProductionConfig, "development": DockerDevConfig}
