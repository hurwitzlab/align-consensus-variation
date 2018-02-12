#!/usr/bin/env python

""" Docstring
Script to check for / install conda
And then install
-bowtie2
-samtools/bcftools
"""
from subprocess import call
import sys


def setupPlumbum():
    try:
        from plumbum import local
    except ImportError:
        print("Need to grab plumbum")
        try:
            retcode = call("conda install" + " -c conda-forge plumbum", shell=True)
            if retcode < 0:
                print("Child was terminated by signal", -retcode, file=sys.stderr)
            else:
                print("Child returned", retcode, file=sys.stderr)
                if retcode != 0:
                    sys.exit("Something went wrong")
        except OSError as e:
            print("Execution failed:", e, file=sys.stderr)


def checkConda():
    try:
        import conda.cli
    except ImportError:
        print("Conda not found, installing now...")
        try:
            print("Downloading Conda")
            retcode = call("wget" + " https://repo.continuum.io/archive/Anaconda3-5.0.1-MacOSX-x86_64.sh", shell=True)
            if retcode < 0:
                print("Child was terminated by signal", -retcode, file=sys.stderr)
            else:
                print("Child returned", retcode, file=sys.stderr)
                if retcode != 0:
                    sys.exit("Something went wrong")

        except OSError as e:
            print("Download failed:", e, file=sys.stderr)
        try:
            print("Installing Conda")
            retcode = call("bash" + " Anaconda3-5.0.1-MacOSX-x86_64.sh", shell=True)
            if retcode < 0:
                print("Child was terminated by signal", -retcode, file=sys.stderr)
            else:
                print("Child returned", retcode, file=sys.stderr)
                if retcode != 0:
                    sys.exit("Something went wrong")
        except OSError as e:
            print("Execution failed:", e, file=sys.stderr)


def installTools():
    import conda.cli
    conda.cli.main('conda', 'install', '-c', 'bioconda', '-y', 'bowtie2')
    conda.cli.main('conda', 'install', '-c', 'bioconda', '-y', 'samtools')
    conda.cli.main('conda', 'install', '-c', 'bioconda', '-y', 'bcftools')


checkConda()
setupPlumbum()
installTools()
