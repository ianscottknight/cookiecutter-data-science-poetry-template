
import os
import dotenv
from pathlib import Path
import re

dotenv.load_dotenv()

# TODO: assign environmental variables
#VAR = os.getenv("VAR_NAME")

def get_root_dir():
    """Returns project root directory based on hierarchical depth of util.py"""
    return Path(__file__).parent.parent

ROOT_DIR = get_root_dir()

DATA_DIR = os.path.join(ROOT_DIR, "data")
DATA_RAW_DIR = os.path.join(DATA_DIR, "raw")
DATA_INTERIM_DIR = os.path.join(DATA_DIR, "interim")
DATA_PROCESSED_DIR = os.path.join(DATA_DIR, "processed")
DATA_EXTERNAL_DIR = os.path.join(DATA_DIR, "external")

SRC_DIR = os.path.join(ROOT_DIR, "src")
MAKE_DATASET_SCRIPT_PATH = os.path.join(SRC_DIR, "data", "make_dataset.py")
BUILD_FEATURES_SCRIPT_PATH = os.path.join(SRC_DIR, "features", "build_features.py")
TRAIN_MODEL_SCRIPT_PATH = os.path.join(SRC_DIR, "models", "train_model.py")
PREDICT_MODEL_SCRIPT_PATH = os.path.join(SRC_DIR, "models", "predict_model.py")
VISUALIZE_SCRIPT_PATH = os.path.join(SRC_DIR, "visualization", "visualize.py")

MODELS_DIR = os.path.join(ROOT_DIR, "models")

NOTEBOOKS_DIR = os.path.join(ROOT_DIR, "notebooks")


def load_txt_file_as_list(filepath):
    with open(filepath, "r") as f:
        lst = [line.strip() for line in f.readlines()]
    return lst

