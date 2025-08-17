from jason import CONFIGS
from pathlib import Path
import json
import shutil
import setup

def read_files():
    PATH = Path(CONFIGS["input-path"])
    for f in Path.iterdir(PATH):
        move_file(f)
    
def move_file(file_path):
    out_path = CONFIGS["output-path"]
    shutil.move(file_path, out_path)

# setup()
# read_files() 
# print("success")
print(setup.setup())