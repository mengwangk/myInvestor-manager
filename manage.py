#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Worldss"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)