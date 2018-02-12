#!/usr/bin/env python
""" Docstring
Script that aligns reads to a reference using bowtie2
"""
import subprocess
import argparse
from plumbum import local


def align(forward,reverse,index,sam_out):
    """
    Call bowtie2-align on paired read data
    :return:
    """
    # check that we have access to bowtie2
    try:
        subprocess.check_output(['bowtie2', '-h'])
    except OSError:
        raise RuntimeError('bowtie2 not found; check if it is installed and in $PATH\n')

    bowtie2 = local['bowtie2']
    stdout = bowtie2('-x' + index,'-1' + forward,'-2' + reverse, \
            '-S' + sam_out)
    print(stdout)


if __name__ == "__main__":
    parser = \
    argparse.ArgumentParser(description="Script that builds a bowtie2 index")
    
    parser.add_argument("-f", "--forward", action="store", \
            help="Forward reads, comma separated")
    parser.add_argument("-r", "--reverse", action="store", \
            help="Reverse reads, comma separated")
    parser.add_argument("-i", "--index", action="store", \
            help="Bowtie2 index, just the path and prefix")
    parser.add_argument("-s", "--sam_out", action="store", \
            default="./alignments.sam", \
            help="Output sam file, DEFAULT = ./alignments.sam")
    args = vars(parser.parse_args())
    align(args['forward'],args['reverse'],args['index'],args['sam_out'])
