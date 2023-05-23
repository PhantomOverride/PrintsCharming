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
    "tags": ["all"],
    "data": "base64-encoded data"
}
```
Tags indicate which rules should be used for the run.
Data is the input data, base64 encoded.

Response format:
```
{
    "detections": [
        {
            "rule": "jQuery ([\d.]+)",
            "match": "jQuery 1.2.3.4",
            "type": "regex",
            "component": "jquery",
            "version": "1.2.3.4"
        }
    ]
}
```
Detections is a list of detections, based on the rules used. The interesting output is component and version, which contains the fingerprint.

Rules format:

```
{
  "tags": ["js"],
  "type": "regex",
  "pattern": "jQuery ([\\d.]+)",
  "component": "jquery",
  "version": ""
}
```
Version will be overridden by any capture group.