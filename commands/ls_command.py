import json

def ls(json_data: str) -> str:
    data = json.loads(json_data)
    ls_output = ""
    for content in data['contents']:
        content_name = content['name']
        if not content_name.startswith("."):
            ls_output += content_name + " "

    return ls_output