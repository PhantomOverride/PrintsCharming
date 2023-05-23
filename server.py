#!/usr/bin/env python
# encoding: utf-8
import json
from PrintsCharming import PrintsCharming
from flask import Flask, request, jsonify
app = Flask(__name__)

pc = PrintsCharming()

@app.route('/')
def index():
    return pc.hello()

@app.route('/<path:path>',methods = ['GET', 'POST'])
def catch_all(path):
    print(request.get_json(force=True))
    pc.handle(path)
    return ":)"
app.run()
