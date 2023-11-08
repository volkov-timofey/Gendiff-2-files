import json


def get_json(diff: dict) -> str:
    """
    Formatter json valid string
    """

    return json.dumps(diff)
