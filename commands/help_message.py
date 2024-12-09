HELP_MESSAGE = """

    Usage: pyls.py [OPTIONS]
    
    This tool lists in Linux style the information contained within a json file received as input
    
    Options:
    -h      Show human readable size
    -A      Prints all the files and directories, even the ones that begins with "."
    -l      Lists the result vertically with additional information
    -r      Lists the result in reverse
    -t      Prints the result sorted by last modified
    --filter=<option>   This will filter the result based on the option, that are only "file" and "dir". If none of these
                        two options are passed as input, an error message is displayed
    
    Examples:
    python -m pyls example_file.json
    python -m pyls example_file.json -l -A
    python -m pyls example_file.json -l -A -t
    
    To display this help message:
    python -m pyls --help

"""