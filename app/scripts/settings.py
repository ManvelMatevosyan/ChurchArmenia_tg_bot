from pathlib import Path
from sys import executable as PYTHON_BIN

ABS_ROOT_DIR = str(Path(__file__).parent.resolve())

# runner.py PARAMS
LOG_PATH = Path(ABS_ROOT_DIR + "/data/runner_log.txt")
RERUN_SLEEP_SEC = 2
GEN_SHELL_COMMAND = lambda : f"{PYTHON_BIN} {ABS_ROOT_DIR}/scripts/ChurchArmenia.py"

# statuses.py PARAMS
STATUSES_FILE_NAME = "statuses"
STATUSES_FILE_PATH = Path(f"{ABS_ROOT_DIR}/data/{STATUSES_FILE_NAME}.json")