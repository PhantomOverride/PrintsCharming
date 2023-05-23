from flask import jsonify
import json
__version__ = '0.0.1'

class PrintsCharming:
    def __init__(self):
        pass

    def load_rules(self, location):
        pass

    def run_rules(self, rules, input):
        pass

    def do_fingerprint(self):
        self.load_rules()

    def handle(self, pipeline, input):
        if (pipeline == "fingerprint"):
            return self.do_fingerprint()
        elif (pipeline == "asdf"):
            return "asdf"
        else:
            return None

    def test(self):
        return jsonify({
            "detections": [
                {
                    "rule": "jQuery ([\d.]+)",
                    "tags": ["all", "js"],
                    "match": "jQuery 1.2.3.4",
                    "type": "fingerprint",
                    "component": "jquery",
                    "version": "1.2.3.4"
                },
                {
                    "rule": "angular ([\d.]+)",
                    "tags": ["all", "js"],
                    "match": "angular 1.2.3.4",
                    "type": "fingerprint",
                    "component": "angular",
                    "version": "1.2.3.4"
                }
            ]
        })




