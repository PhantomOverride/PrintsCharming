from flask import jsonify
__version__ = '0.0.1'

class PrintsCharming:
    def __init__(self):
        pass

    def hello(self):
        return jsonify({
            "detections": [
                {
                    "rule": "jQuery ([\d.]+)",
                    "match": "jQuery 1.2.3.4",
                    "type": "fingerprint",
                    "component": "jquery",
                    "version": "1.2.3.4"
                }
            ]
        })

