import subprocess
from time import sleep
import logging

from scripts.settings import *

# LOGGER INIT
MY_LOG = logging.getLogger(__file__)
MY_LOG.setLevel(logging.DEBUG)

LOG_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Create a file handler to write logs to a file
LOG_file_handler = logging.FileHandler(LOG_PATH)
LOG_file_handler.setLevel(logging.DEBUG)
LOG_file_handler.setFormatter(LOG_formatter)

# Create a stream handler to print logs to the console
LOG_console_handler = logging.StreamHandler()
LOG_console_handler.setLevel(logging.DEBUG)  # You can set the desired log level for console output
LOG_console_handler.setFormatter(LOG_formatter)

# Add the handlers to the logger
MY_LOG.addHandler(LOG_file_handler)
MY_LOG.addHandler(LOG_console_handler)

# CODE

MY_LOG.info(f"--------STARTING RUNNER-------->\n")

try:
    run = True
    while run:
        SHELL_CMD = GEN_SHELL_COMMAND()
        MY_LOG.info(f"Running SHELL_CMD={SHELL_CMD}\n")
        completedProc = subprocess.run(SHELL_CMD, shell=True)
        MY_LOG.critical(f"\tended with exit code <{completedProc.returncode}>\n")
        sleep(RERUN_SLEEP_SEC)
    MY_LOG.error(f"--------ENDING RUNNER \t NO REASON--------\n")
except KeyboardInterrupt:
    MY_LOG.info(f"--------ENDING RUNNER \t KEYBOARD INTERRUPT--------\n")
finally:
    pass
MY_LOG.info(f"--------EXITING RUNNER SCRIPT - BYE--------\n")


