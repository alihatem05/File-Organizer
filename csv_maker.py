from settings import CONFIGS, logging
from pathlib import Path
import csv

def setup_csv():
    counts = counter()
    csv_file = Path("categories.csv")

    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)

        if csv_file.stat().st_size == 0:
            writer.writerow(["Category", "File Count"])

        for category, count in counts.items():
            writer.writerow([category, count])
            logging.debug(f"Logged {count} files for {category} category")

def counter():
    PATH = Path(CONFIGS["output-path"])
    counts = {}

    for folder in PATH.iterdir():
        if folder.is_dir():
            counts[folder.name] = len([f for f in folder.iterdir() if f.is_file()])

    return counts
