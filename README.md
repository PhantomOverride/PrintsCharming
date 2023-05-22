# PrintsCharming

PrintsCharming is a locally hosted service that will try to fingerprint the stuff you throw at it.

Request format:
```
{
    "type": "html",
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