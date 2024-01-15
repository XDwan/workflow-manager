import os
import yaml
import pandas as pd
import numpy as np
import itertools


def dir_create(path, dir_name):
    dir_path = os.path.join(path, dir_name)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    return dir_path


def path_join(path, dir_name):
    return os.path.join(path, dir_name)


def check_file(path):
    if os.path.exists(path):
        return True
    return False


def load_yaml(path):
    with open(path, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data


def add_config(key, value):
    return key + " " + str(value) + " "


def filter_dataframe(frame, loc, value):
    pass


def merge_list(data_list):
    return list(itertools.product(*data_list))
