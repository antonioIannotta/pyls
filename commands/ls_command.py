import json
from typing import SupportsIndex


def ls(json_data: str, a_option: bool = False) -> str:
    data: str = json.loads(json_data)
    ls_output: str = ""
    for content in data['contents']:
        content_name= content['name']
        if a_option:
            ls_output += content_name + " "
        elif not content_name.startswith("."):
            ls_output += content_name + " "


    return ls_output