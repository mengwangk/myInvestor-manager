#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Start-up module. 
#
###############################################################################
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

# if __name__ == '__main__':
#    app.run(debug=True,host='0.0.0.0',port=5000)
