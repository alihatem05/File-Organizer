from settings import CONFIGS, logging
from pathlib import Path
import shutil
import setup

def organizer():
    setup.setup()
    read_files()
    logging.debug(f"********ORGANIZING COMPLETED********")

def read_files():
    logging.debug(f"********READ_FILES INITIALIZED********")
    PATH = Path(CONFIGS["input-path"])
    for f in Path.iterdir(PATH):
        categorize(f)

def categorize(file):
    filename = file.name
    logging.debug(f"**CATEGORIZE {filename} INITIALIZED**")
    suffix = file.suffix
    logging.debug(f"{filename} extension is {suffix}")
    cats = CONFIGS["categories"]
    found = False
    for cat, extensions in cats.items():
        logging.debug(f"Checking {cat} category...")
        if suffix in extensions:
            move_file(file, cat)
            found = True
            logging.debug(f"{filename} is {cat} category")
            break
    if not found:
        move_file(file, "others")
        logging.debug(f"{filename} is others category")
    
    
def move_file(file, category):
    OUT_PATH = Path(CONFIGS["output-path"]) / category / file.name
    shutil.move(file, OUT_PATH)
    logging.info(f"{file} moved to {category}")


organizer()