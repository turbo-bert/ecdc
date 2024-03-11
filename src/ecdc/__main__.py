import logging
import time
FORMAT = '%(asctime)s+00:00 %(levelname)10s: %(message)-80s    (%(filename)s,%(funcName)s:%(lineno)s)'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logging.Formatter.converter = time.gmtime

import rich
from rich.pretty import pprint as PP
from rich.console import Console
from rich.table import Table
CONSOLE = Console()

import argparse
import os
import sys

import pathlib

parser = argparse.ArgumentParser(prog="ecdc", description="Work (more) quickly with yaml files in a folder for docker compose.", epilog="Make sure EDITOR and ECDC_HOME are exported")
parser.add_argument("--name", nargs=1, type=str, metavar="NAME", default=["unnamed"], help="Name to use in for selected operation")
parser.add_argument("--gen-wp", action="store_true", help="")

args = parser.parse_args()

EDITOR = os.getenv("EDITOR", "nano")
NAME = args.name[0]
HOME = os.getenv("ECDC_HOME", None)
KNOWN_FILES = []

def find_yaml_files():
    global KNOWN_FILES
    KNOWN_FILES = []
    for f in os.listdir(HOME):
        if f.upper().endswith(".YAML") or f.upper().endswith(".YML"):
            if os.path.isfile(os.path.join(HOME, f)):
                KNOWN_FILES.append(f)

def show_yaml_files():
    PP(KNOWN_FILES)

if HOME == None:
    logging.error("ENV is missing ECDC_HOME (path to your yaml/yml files) - exiting with code 1.")
    sys.exit(1)

logging.info("HOME is %s" % HOME)
find_yaml_files()
show_yaml_files()
