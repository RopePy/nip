import json

__all__ = ['pformat_json']

def pformat_json(js):
    return json.dumps(js, indent=4)
