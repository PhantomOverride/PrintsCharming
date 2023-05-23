from flask import jsonify
import json
import base64
import re
__version__ = '0.0.1'

class PrintsCharming:
    def __init__(self):
        self.rules = self.load_rules("rules/fingerprint/samples.json")

    def load_rules(self, location):
        with open(location) as f:
            rules = json.load(f)
        return rules["rules"]

    def run_rules(self, rules, input):
        # remember that input["tags"] is a list
        detections = []
        try:
            raw_input = base64.b64decode(input["data"]).decode('utf-8')
        except:
            return "Error decoding input -- is the base64 valid?"
        for rule in rules:
            regex = rule["pattern"]
            finds = re.finditer(regex, raw_input)
            for find in finds:
                if len(find.groups()) > 0:
                    v = find.groups(1)[0]
                else:
                    v = ""
                d = {
                    "rule": rule["pattern"],
                    "match": find.group(0),
                    "type": rule["type"],
                    "component": rule["component"],
                    "version": v
                }
                detections.append(d)
        return detections

    def do_fingerprint(self, input):
        return self.run_rules(self.rules, input)

    def handle(self, pipeline, input):
        if (pipeline == "fingerprint"):
            return self.do_fingerprint(input)
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




