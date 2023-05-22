#!/usr/bin/env python
# encoding: utf-8
import json
from PrintsCharming import PrintsCharming
from flask import Flask, jsonify
app = Flask(__name__)

pc = PrintsCharming()

@app.route('/')
def index():
    return pc.hello()

app.run()
