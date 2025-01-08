import json
from settings import *



def load_statuses():
    if STATUSES_FILE_PATH.exists():
        return json.loads(open(STATUSES_FILE_PATH).read())
    else:
        return dict()

def write_statuses(statusses_dict):
    json.dump(statusses_dict, open(STATUSES_FILE_PATH, "w+"))