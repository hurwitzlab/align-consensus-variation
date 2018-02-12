#!/usr/bin/env python
""" Docstring
Script that creates a bowtie2 index
"""
import subprocess
import argparse
import os
from plumbum import local

def build(fasta,name,outdir):
    """
    Construct bowtie2 indices (.bt2 files)
    :param fasta: Path to FASTA containing reference sequences
    :return:
    """
    try:
        subprocess.check_output(['bowtie2-build', '-h'])
    except OSError:
        raise RuntimeError('bowtie2-build not found; check if it is installed and in $PATH\n')

    bowtie2_build = local['bowtie2-build']
    os.chdir(outdir)
    stdout = bowtie2_build(fasta,name)
    print(stdout)


def main():
    build(args['fasta'],args['name'],args['outdir'])


if __name__ == "__main__":
    parser = \
    argparse.ArgumentParser(description="Script that builds a bowtie2 index")
    
    parser.add_argument("-f", "--fasta", action="store", \
            help="A fasta file")
    parser.add_argument("-n", "--name", action="store", \
            help="Prefix to give bowtie2 index, DEFAULT = genome", \
            default="genome")
    parser.add_argument("-d", "--outdir", action="store", \
            default="./", help="Output directory, DEFAULT = ./")
    args = vars(parser.parse_args())
    main()
