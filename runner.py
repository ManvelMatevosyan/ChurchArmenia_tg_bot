import subprocess
from time import sleep
from pathlib import Path
from datetime import datetime

# PARAMS
LOG_PATH = Path("./runner_log.txt")
RERUN_SLEEP_SEC = 2
SHELL_CMD = "python ./ChurchArmenia.py"

# CODE
runner_log = None
if LOG_PATH.exists():
    runner_log = open(LOG_PATH, "a+")
else:
    runner_log = open(LOG_PATH, "w+")

runner_log.write(f"--------STARTING RUNNER AT <{datetime.now()}....>\n")
runner_log.flush()
try:
    run = True
    while run:
        runner_log.write(f"Running at <{datetime.now()}....>\n")
        runner_log.flush()
        completedProc = subprocess.run(SHELL_CMD)
        runner_log.write(f"\tended at <{datetime.now()}> with exit code <{completedProc.returncode}>\n")
        runner_log.flush()
        sleep(RERUN_SLEEP_SEC)
    runner_log.write(f"--------ENDING RUNNER AT <{datetime.now()}>\n")
    runner_log.flush()
except KeyboardInterrupt:
    runner_log.write(f"--------KEYBOARD INTERRUPT AT <{datetime.now()}>\n")
    runner_log.flush()
finally:
    runner_log.flush()
    runner_log.close()



