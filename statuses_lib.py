import json, pathlib
STATUSES_FILE_NAME = "statuses"
STATUSES_FILE_PATH = pathlib.Path(f"./{STATUSES_FILE_NAME}.json")

def load_statuses():
    if STATUSES_FILE_PATH.exists():
        return json.loads(open(STATUSES_FILE_PATH).read())
    else:
        return dict()

def write_statuses(statusses_dict):
    json.dump(statusses_dict, open(STATUSES_FILE_PATH, "w+"))