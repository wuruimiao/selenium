import json
import os

import selenium_profiles
from selenium_profiles.utils.colab_utils import is_colab


def sel_profiles_path():
    return os.path.dirname(selenium_profiles.__file__) + "/"


def read(filename: str, encoding: str = "utf-8", sel_root=True):
    if sel_root:
        path = sel_profiles_path() + filename
    else:
        path = filename
    with open(path, encoding=encoding) as f:
        return f.read()

def write(filename: str, content:str, encoding: str = "utf-8", sel_root=True):
    if sel_root:
        path = sel_profiles_path() + filename
    else:
        path = filename
    with open(path,"w", encoding=encoding) as f:
        return f.write(content)

def read_json(filename: str = 'example.json', encoding: str = "utf-8",sel_root=True):
    if sel_root:
        path = sel_profiles_path() + filename
    else:
        path = filename
    with open(path, 'r', encoding=encoding) as f:
        return json.load(f)


def write_json(obj: dict or list, filename: str = "out.json", encoding: str = "utf-8",sel_root=True):
    if sel_root:
        path = sel_profiles_path() + filename
    else:
        path = filename
    with open(path, "w", encoding=encoding) as outfile:
        outfile.write(json.dumps(obj))

def check_cmd(value, values):
    if value not in values:
        raise ValueError("got " + str(value) + " , but expected " + str(values))

def valid_key(got:list or set, valid:list, obj_name:str):
    for key in got:
        if key not in valid:
            raise ValueError(f"'{key}' isn't a valid key for {obj_name}")

def my_platform():
    import platform
    if is_colab():
        return "Google-Colab"
    else:
        return platform.system()
