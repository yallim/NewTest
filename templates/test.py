import os
import logging
from cgi import logfp
from multiprocessing.util import log_to_stderr

def show_strings(string_value):
    global logs
    match string_value:
        case "num":
            print(string_value)
            logs = string_value
            return logs
        case "string":
            print(string_value)
            return f"string entered: {logs}"
        case "":
            print(string_value)
            return logs

