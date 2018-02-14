#!/usr/bin/env python
""" Docstring
Script that makes an annotated vcf
"""
import os
import subprocess
import argparse
from plumbum import local


def annotate(gff,calls,output,bed):
    """
    Converts gff to a bed file
    bgzips the bed file
    tabixs the bed file
    run bcftools on the bedfile
    :return:
    """
    # check that we have access to samtools
    try:
        subprocess.check_output(['bcftools', 'help'])
    except OSError:
        raise RuntimeError('bcftools not found; check if it is installed and in $PATH\n')
    
    # setup command line tools with plumbum
    bcftools = local['bcftools']
    tabix = local['tabix']
    gff2bed = local['gff2bed']
    bgzip = local['bgzip']

    # create file with 'header'
    with open('header.txt','w') as header:
        header.write('##INFO=<ID=GENE,Number=1,Type=String,Description="Gene name">')
    
    chain = ( gff2bed < gff > bed )
    stdout = chain()
    print(stdout)
    bgzip(bed)
    tabix('-p','bed',bed + '.gz')
    chain = ( (bcftools['annotate','-a',bed + '.gz',\
            '-c','CHROM,FROM,TO,GENE','-h','header.txt',\
            calls] > output ))
    stdout = chain()
    print(stdout)


if __name__ == "__main__":
    parser = \
    argparse.ArgumentParser(description="Script that annotates a vcf")
    
    parser.add_argument("-g", "--gff", action="store", \
            help="Gff file")
    parser.add_argument("-c", "--calls", action="store", \
            default="./calls.vcf.gz", \
            help="Calls output file of bcftools, DEFAULT=./calls.vcf.gz")
    parser.add_argument("-o", "--output", action="store", \
            default="./ann.vcf", \
            help="Output annotated vcf, DEFAULT=./ann.vcf")
    parser.add_argument("-b", "--bed", action="store", \
            default="./annotations.bed", \
            help="Intermediate bed file, DEFAULT=./annotations.bed")

    args = vars(parser.parse_args())
    annotate(args['gff'],args['calls'],args['output'],args['bed'])
