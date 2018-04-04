## Alignment, concensus and variation simple pipeline
Steps:
* Setup anaconda (python3), plumbum (python module), other software > setup.py
* Align the parent to reference > bowtie_index.py, align.py
* Create a consensus of the parent > gen_consensus.py
* Align the daughter to the parent consensus > bowtie_index.py, align.py
* Create an ann.vcf file of the daughter alignment using the reference gff > gen_consensus.py (for calls.vcf), gen_vcf.py

# Source data is in /data

# Assignment text:
You’ll see  GCF_000005845.2_ASM584v2_genomic.fna, GCF_000005845.2_ASM584v2_genomic.gff and 2 sets of fastq files. GCF_000005845.2_ASM584v2_genomic is the reference, sample-1 is the parent and sample-2 is the daughter.

# Example commands used:
<From within ./scripts/ directory>
* `./setup.py`
* `./bowtie_index.py -f ../data/GCF_000005845.2_ASM584v2_genomic.fna -d ../data/`
* `./align.py -f ../data/sample-1_S1_L001_R1_001.fastq -r ../data/sample-1_S1_L001_R2_001.fastq -i ../data/genome -s ../data/parent_alignments.sam`
* `./gen_consensus ./gen_consensus.py -a ../data/parent_alignments.sam -r ../data/GCF_000005845.2_ASM584v2_genomic.fna -o ../data/consensus.fna -c ../data/parents.vcf.gz`
* `./bowtie_index.py -f ../data/consensus.fna -n consensus -d ../data/`
* `./align.py -f ../data/sample-2_S6_L001_R1_001.fastq -r ../data/sample-2_S6_L001_R2_001.fastq -i ../data/consensus -s ../data/daughter_alignments.sam`
* `./gen_consensus.py -a ../data/daughter_alignments.sam -r ../data/consensus.fna -o /dev/null -c ../data/daughter.vcf.gz`
* `./gen_vcf.py -g ../data/GCF_000005845.2_ASM584v2_genomic.gff -c ../data/daughter.vcf.gz -o ../data/ann.vcf -b ../data/daughter.bed`

# Programs and versions:
Anaconda3
`conda version : 4.4.9,
conda-build version : 3.0.27,
python version : 3.6.3.final.0`

Bowtie2
`version 2.3.0`

samtools
`version 1.7
Using htslib 1.7`

bcftools
`version 1.6
Using htslib 1.6`

bedops
`version 2.4.30`
