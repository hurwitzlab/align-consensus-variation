#!/usr/bin/env python
""" Docstring
Script that aligns reads to a reference using bowtie2
"""

import sys
import argparse
import os
from plumbum import local

if __name__ == "__main__":
    parser = \
    argparse.ArgumentParser(description="Script that aligns reads to a reference using bowtie2")
    
    parser.add_argument("-r", "--report", action="store", \
            help="Centrifuge report file, usually: centrifue_report.tsv")
    parser.add_argument("-t", "--taxid", action="store_true", \
            help="Print only taxids")
    parser.add_argument("-n", "--name", action="store_true", \
            help="Print only species names")

