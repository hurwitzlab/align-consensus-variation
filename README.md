## Alignment, concensus and variation simple pipeline
Steps:
* Setup anaconda (python3), plumbum (python module), other software > 00-setup.py
* Align the parent to reference > 01-align.py
* Create a consensus of the parent > 02-consensus.py
* Align the daughter to the parent consensus > 03-align-to-con.py
* Create an ann.vcf file of the daughter alignment using the reference gff > 04-generate-vcf.py

# Source data is here:
https://jmilabs.exavault.com/share/view/1ymd-5kbeaurx

# Assignment text:
At this link https://jmilabs.exavault.com/share/view/1ymd-5kbeaurx you’ll see  GCF_000005845.2_ASM584v2_genomic.fna, GCF_000005845.2_ASM584v2_genomic.gff and 2 sets of fastq files. GCF_000005845.2_ASM584v2_genomic is the reference, sample-1 is the parent and sample-2 is the daughter.

# Example commands used:
<From within ./scripts/ directory>
* `./setup.py`
* `./bowtie_index.py -f ../data/GCF_000005845.2_ASM584v2_genomic.fna -d ../data/`
* `./align.py -f ../data/sample-1_S1_L001_R1_001.fastq -r ../data/sample-1_S1_L001_R2_001.fastq -i ../data/genome -s ../data/parent_alignments.sam`

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
