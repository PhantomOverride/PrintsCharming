# PrintsCharming

PrintsCharming is a locally hosted service that will try to fingerprint the stuff you throw at it.

## Todo
- All the things!
- REST API
- CLI client (fingerprint file(s) or URL(s))
- Rules to detect common components
- Web client
- Web browser plugin
- Burp plugin
- Fingerprinting HTTP request and response headers
- Rules that generate insight instead of component detection

## Data format

Request format:
```
{
    "tags": "html",
    "data": "base64-encoded data"
}
```

Response format:
```
{
    "detections": [
        {
            "rule": "jQuery ([\d.]+)",
            "match": "jQuery 1.2.3.4",
            "type": "fingerprint",
            "component": "jquery",
            "version": "1.2.3.4"
        }
    ]
}
```