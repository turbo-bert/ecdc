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

parser = argparse.ArgumentParser(prog="ecdc")
#parser.add_argument("--bla4", action="store_true", help="Help for BLA_4")


args = parser.parse_args()

