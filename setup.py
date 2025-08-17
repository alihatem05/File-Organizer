from settings import CONFIGS, logging
from pathlib import Path

def checker(PATH):
    cats = set(CONFIGS["categories"].keys())
    if not PATH.exists():
        return cats
    for f in PATH.iterdir():
        if f.name in cats:
            cats.remove(f.name)
    return cats

def create_missing(PATH, missing_files):
    if not PATH.exists():
        PATH.mkdir(exist_ok=True)
        logging.info("Main output directory created.")
    for c in missing_files:
        temp = PATH / c
        temp.mkdir(exist_ok=True)
        logging.info(f"{temp.name} directory created.")
    temp = PATH / "others"
    temp.mkdir(exist_ok=True)
    logging.info(f"{temp.name} directory created.")

def setup():
    logging.debug(f"********SETUP INITIALIZED********")
    PATH = Path(CONFIGS["output-path"])
    missing_files = checker(PATH)
    if missing_files:
        create_missing(PATH, missing_files)
    logging.debug(f"********SETUP COMPLETED********")
    return 1