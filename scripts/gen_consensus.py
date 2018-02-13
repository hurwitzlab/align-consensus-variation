#!/usr/bin/env python
""" Docstring
Script that takes an alignment and reference sequence and generates a consensus
"""
import subprocess
import argparse
from plumbum import local


def consens(alignments,reference,output):
    """
    Run samtools then bcftools then vcfutils.pl on a ref and alignment
    :return:
    """
    # check that we have access to samtools
    try:
        subprocess.check_output(['samtools', 'help'])
    except OSError:
        raise RuntimeError('samtools not found; check if it is installed and in $PATH\n')
    
    samtools = local['samtools']
    bcftools = local['bcftools']
    tabix = local['tabix']
    cat = local['cat']

    if (alignments.endswith('.sam')):
        alignments = convert_to_bam(alignments)

#DEBUG
#    print("Alignments are now {}".format(alignments))

    alignments = check_sorted(alignments)

#DEBUG
#    print("Alignments are now {}".format(alignments))
    
    with open('calls.vcf.gz','w') as calls:
        chain = samtools['mpileup','-uf',reference,alignments] \
                | bcftools['call','-mv','-Oz','-o','calls']
        chain()
        tabix(calls)
        chain2 = ((cat[reference] | bcftools['consensus',calls]) > output)
        stdout = chain2()
        print(stdout)


def convert_to_bam(alignments):
    print("Converting {} to bam format".format(alignments))
    newname = str(alignments).replace('.sam','.bam')
    samtools = local['samtools']
    with open(newname,'wb',0) as alignments_bam:
        chain = ((samtools['view','-S','-b',alignments]) > alignments_bam)
        chain()
        return(alignments_bam)


def check_sorted(alignments):
    print("Checking that {} is sorted".format(alignments))
    samtools = local['samtools']

    sort_string = samtools('view','-H',alignments).split()[2]
    print("Sorting status is {:s}".format(sort_string))

    if (str(sort_string) == 'SO:unsorted'):
        print("{} is unsorted, sorting for you".format(alignments))
        samtools('sort','-o',alignments,alignments)
        return(alignments)
    else:
        return(alignments)
 

if __name__ == "__main__":
    parser = \
    argparse.ArgumentParser(description="Script that generates a consensus")
    
    parser.add_argument("-a", "--alignments", action="store", \
            help="Alignments file, in sam or bam format")
    parser.add_argument("-r", "--reference", action="store", \
            help="Reference fasta sequence")
    parser.add_argument("-o", "--output", action="store", \
            default="./consensus.fna", \
            help="Output fastq file, DEFAULT = ./output.fq")
    args = vars(parser.parse_args())
    consens(args['alignments'],args['reference'],args['output'])
