import json
from utils import format_time, find_item, format_bytes
from typing import List, Dict, Optional, Any


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


def ls_l(
    json_data: str,
    a_option: bool = False,
    r_option: bool = False,
    h_option: bool = False,
    t_option: bool = False,
    filter_option: Optional[str] = None,
    path: Optional[str] = None,
) -> str:

    data: Dict[str, Any] = json.loads(json_data)
    contents: List[Dict[str, Any]] = data["contents"]

    if path:
        item = find_item(contents, path)
        if item is None:
            return f"Error: Path '{path}' not found."

        if item["permissions"].startswith("d"):
            contents = item.get("contents", [])
        else:
            content_permissions = item["permissions"]
            content_size = item["size"]
            if h_option:
                content_size = format_bytes(item["size"])
            content_time_modified = format_time(item["time_modified"])
            content_name = item["name"]
            return (
                content_permissions
                + " "
                + str(content_size)
                + " "
                + content_time_modified
                + " "
                + content_name
                + "\n"
            )

    if filter_option == "dir":
        contents = [content for content in contents if content["permissions"].startswith("d")]
    elif filter_option == "file":
        contents = [content for content in contents if content["permissions"].startswith("-")]
    elif filter_option is not None:
        return "error: Invalid filter option. Use 'dir' for directories or 'file' for files."
    if t_option:
        contents = sorted(contents, key=lambda x: x["time_modified"], reverse=r_option)
    ls_output: str = ""
    for content in contents:
        content_permissions = content["permissions"]
        content_size = content["size"]
        if h_option:
            content_size = format_bytes(content["size"])
        content_time_modified = format_time(content["time_modified"])
        content_name = content["name"]
        if a_option:
            ls_output += (
                content_permissions
                + " "
                + str(content_size)
                + " "
                + content_time_modified
                + " "
                + content_name
                + "\n"
            )

        elif not content_name.startswith("."):
            ls_output += (
                content_permissions
                + " "
                + str(content_size)
                + " "
                + content_time_modified
                + " "
                + content_name
                + "\n"
            )

    if r_option and not t_option:
        ls_output = "\n".join(ls_output.splitlines()[::-1])

    return ls_output
