import json
import logging

with open("data.json", "r") as file:
    CONFIGS = json.load(file)

logging.basicConfig(
    level=logging.DEBUG,
    filename="log.txt",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s"
)