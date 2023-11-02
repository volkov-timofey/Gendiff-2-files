import json as default_json


def json(diff: dict) -> str:
    """
    Formatter json valid string
    """
    return default_json.dumps(diff)
