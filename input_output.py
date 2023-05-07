import json


def read_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
        return data


def write_json(json_file, overwrite_data):
    with open(json_file, 'w') as f:
        json.dump(overwrite_data, f)


def get_salt():
    with open("salt.txt", "r") as salt:
        return salt.read()
