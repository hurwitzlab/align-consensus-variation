#!/usr/bin/env python

""" Docstring
Script to check for / install conda
And then install
-bowtie2
-samtools/bcftools
""" 
from plumbum import local

def setupPlumbum():
    wget = local['wget']
    bash = local['bash']

def checkConda():
    try:
        import conda.cli
    except ImportError:
        print("Conda not found, installing now...")
        wget("https://repo.continuum.io/archive/Anaconda3-5.0.1-MacOSX-x86_64.sh")
        bash("Anaconda3-5.0.1-MacOSX-x86_64.sh")

def installTools():
    conda.cli.main('conda', 'install', '-c', 'bioconda', '-y', 'bowtie2')
    conda.cli.main('conda', 'install', '-c', 'bioconda', '-y', 'samtools')

setupPlumbum()
checkConda()
installTools()
