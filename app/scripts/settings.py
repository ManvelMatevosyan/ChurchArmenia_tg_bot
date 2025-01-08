from pathlib import Path
from sys import executable

PYTHON_FALLBACK_BIN = "python3.10"
PYTHON_BIN = executable if executable else PYTHON_FALLBACK_BIN

ABS_ROOT_DIR = str(Path(__file__).parent.parent.resolve())

# runner.py PARAMS
LOCK_FILE = ABS_ROOT_DIR + "/runner.py.lock"
LOG_PATH = Path(ABS_ROOT_DIR + "/data/runner_log.txt")
RERUN_SLEEP_SEC = 2
GEN_SHELL_COMMAND = lambda : f"{PYTHON_BIN} {ABS_ROOT_DIR}/scripts/ChurchArmenia.py"

# statuses.py PARAMS
STATUSES_FILE_NAME = "statuses"
STATUSES_FILE_PATH = Path(f"{ABS_ROOT_DIR}/data/{STATUSES_FILE_NAME}.json")