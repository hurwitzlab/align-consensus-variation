## Alignment, concensus and variation simple pipeline
Steps:
* Setup anaconda (python3), plumbum (python module), other software > 00-setup.py
* Align the parent to reference > 01-align.py
* Create a consensus of the parent > 02-consensus.py
* Align the daughter to the parent consensus > 03-align-to-con.py
* Create an ann.vcf file of the daughter alignment using the reference gff
    > 04-generate-vcf.py

Source data is here:
https://jmilabs.exavault.com/share/view/1ymd-5kbeaurx

#Example commands used:
<From within ./scripts/ directory>
* ./setup.py
* ./bowtie_index.py -f ../data/GCF_000005845.2_ASM584v2_genomic.fna -d ../data/
* ./align.py -f ../data/sample-1_S1_L001_R1_001.fastq -r ../data/sample-1_S1_L001_R2_001.fastq -i ../data/genome -s ../data/parent_alignments.sam

