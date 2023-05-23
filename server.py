#!/usr/bin/env python
# encoding: utf-8
from PrintsCharming import PrintsCharming
from flask import Flask, request
app = Flask(__name__)

pc = PrintsCharming()

@app.route('/')
def index():
    return "Hello! This is a web service that fingerprints stuff! (:"

@app.route('/test')
def test():
    return pc.test()

@app.route('/<path:path>',methods = ['GET', 'POST'])
def catch_all(path):
    #print("Inbound request")
    #print(request.get_json(force=True))
    return pc.handle(path, request.get_json(force=True))

#todo port and stuff!
app.run()
