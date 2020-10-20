
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


def read_txt_file_as_list(filepath):
	with open(filepath, "r") as f:
		lst = [line.strip() for line in f.readlines()]
	return lst

def write_txt_file_from_list(filepath, lst):
	with open(filepath, "w") as f:
		for item in lst:
			f.write(f"{item}\n")

def query_yes_no(question, default="yes"):
	"""Ask a yes/no question via raw_input() and return their answer.

	"question" is a string that is presented to the user.
	"default" is the presumed answer if the user just hits <Enter>.
		It must be "yes" (the default), "no" or None (meaning
		an answer is required of the user).

	The "answer" return value is True for "yes" or False for "no".
	"""
	valid = {"yes": True, "y": True, "ye": True,
			 "no": False, "n": False}
	if default is None:
		prompt = " [y/n] "
	elif default == "yes":
		prompt = " [Y/n] "
	elif default == "no":
		prompt = " [y/N] "
	else:
		raise ValueError("invalid default answer: '%s'" % default)

	while True:
		sys.stdout.write(question + prompt)
		choice = raw_input().lower()
		if default is not None and choice == '':
			return valid[default]
		elif choice in valid:
			return valid[choice]
		else:
			sys.stdout.write("Please respond with 'yes' or 'no' "
							 "(or 'y' or 'n').\n")

def remove_directory(dir_path):
	if os.path.exists(dir_path):
		shutil.rmtree(dir_path)

def reset_directory(dir_path):
	remove_directory(dir_path)
	os.makedirs(dir_path)
	