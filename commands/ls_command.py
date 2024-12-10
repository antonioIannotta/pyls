import json
from utils import format_time, find_item, format_bytes
from typing import List, Dict, Optional, Any


def ls(
    json_data: str,
    a_option: bool = False,
    l_option: bool = False,
    r_option: bool = False,
    h_option: bool = False,
    t_option: bool = False,
    filter_option: Optional[str] = None,
    path: Optional[str] = None,
) -> str:
    """
    This command implements the function of ls, with its several arguments
    :param json_data: the json data corresponding to the file provided in input to the main
    :param a_option: the -A option
    :param l_option: the -l option
    :param r_option: the -r option
    :param h_option: the -h option
    :param t_option: the -t option
    :param filter_option: the filter option to specify if either a dir or a file is desired
    :param path: the path corresponding to the file in which the information are desired
    :return: the output of the ls commnad
    """
    data: Dict[str, Any] = json.loads(json_data)
    contents: List[Dict[str, Any]] = data.get("contents", [])

    if path:
        item = find_item(contents, path)
        if item is None:
            return f"Error: Path '{path}' not found."

        if item["permissions"].startswith("d"):
            contents = item.get("contents", [])
        else:
            if l_option:
                content_permissions = item["permissions"]
                content_size = format_bytes(item["size"]) if h_option else item["size"]
                content_time_modified = format_time(item["time_modified"])
                content_name = item["name"]
                return (
                    f"{content_permissions} {content_size} {content_time_modified} {content_name}\n"
                )
            else:
                return item["name"]

    if filter_option == "dir":
        contents = [c for c in contents if "contents" in c]
    elif filter_option == "file":
        contents = [c for c in contents if "contents" not in c]
    elif filter_option:
        return "Error: Invalid filter option. Use 'dir' for directories or 'file' for files."

    if t_option:
        contents = sorted(contents, key=lambda x: x["time_modified"], reverse=r_option)

    # Generate output
    ls_output = ""
    for content in contents:
        content_name = content["name"]

        if not a_option and content_name.startswith("."):
            continue

        if l_option:
            content_permissions = content["permissions"]
            content_size = format_bytes(content["size"]) if h_option else content["size"]
            content_time_modified = format_time(content["time_modified"])
            ls_output += f"{content_permissions} {content_size} {content_time_modified} {content_name}\n"
        else:
            ls_output += f"{content_name} "

    if r_option and not t_option:
        if not l_option:
            ls_output = ' '.join(ls_output.split()[::-1])
        ls_output = "\n".join(ls_output.splitlines()[::-1])

    return ls_output.strip()
