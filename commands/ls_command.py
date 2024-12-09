import json
from utils import format_time
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


def ls_l(json_data: str, a_option: bool = False, r_option: bool = False) -> str:
    data: str = json.loads(json_data)
    ls_output: str = ""
    for content in data['contents']:
        content_permissions = content['permissions']
        content_size = content['size']
        content_time_modified = format_time(content['time_modified'])
        content_name = content['name']
        if a_option:
            ls_output += (content_permissions +
                          " " + str(content_size) +
                          " " + content_time_modified +
                          " " + content_name + "\n")
        elif not content_name.startswith("."):
                ls_output += (content_permissions +
                              " " + str(content_size) +
                              " " + content_time_modified +
                              " " + content_name + "\n")

    if r_option:
        #print(ls_output.split("\n")[::-1])
        ls_output = "\n".join(ls_output.splitlines()[::-1])

    return ls_output