
import os
import dotenv
from pathlib import Path


dotenv.load_dotenv()

# TODO: assign environmental variables
#VAR = os.getenv("VAR_NAME")

def get_package_dir():
    """Returns package directory based on hierarchical depth of util.py"""
    return Path(__file__).parent

PACKAGE_DIR = get_package_dir()

DATA_DIR = os.path.join(PACKAGE_DIR, "data")
DATA_RAW_DIR = os.path.join(DATA_DIR, "raw")
DATA_INTERIM_DIR = os.path.join(DATA_DIR, "interim")
DATA_PROCESSED_DIR = os.path.join(DATA_DIR, "processed")
DATA_EXTERNAL_DIR = os.path.join(DATA_DIR, "external")

MODELS_DIR = os.path.join(PACKAGE_DIR, "models")


def load_txt_file_as_list(filepath):
    with open(filepath, "r") as f:
        lst = [line.strip() for line in f.readlines()]
    return lst

