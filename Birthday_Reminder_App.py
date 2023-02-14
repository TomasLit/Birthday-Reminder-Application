import subprocess
from constants import MAIN_DIRECTORY

program_path = MAIN_DIRECTORY + "\interface.py"

subprocess.Popen(f'start cmd /k python "{program_path}"', shell=True)
