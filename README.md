# Viral Variants Occurrences (ViVO) finder tool
ViVOfinder is a bioinformatic tool designed to extract the occurences of all intrahost single nucleotide variant (iSNV) of a viral sample, from pileup file.
Output format is a "table.csv" file with the occurrences of all nucleotide variants for each position.


**Reference:** M Rueca, B Bartolini, CEM Gruber et al. Compartmentalized Replication of SARS-Cov-2 in upper vs lower Respiratory Tract Assessed by Whole Genome Quasispecies Analysis. Microorganism 2020 (Submitted).


## Instructions
The software is ready-to-use.

The data input expected is a "pileup" file, produced by using "samtools mpileup" tool (http://www.htslib.org/doc/samtools-mpileup.html).
When pileup is obtained, you can extract all iSNV by thiping the command:

python ./ViVOfinder.py -i path-to-file/InputFile.mpileup -o path-to-file/OutputFile.csv

## ViVOfinder help
>python ViVOfinder.py -h

Usage: python ViVOfinder.py -i path-to-file/InputFile.mpileup -o path-to-file/OutputFile.csv

ViVOfinder is a bioinformatic tool designed to extract the occurences of all
intrahost single nucleotide variant (iSNV) of a viral sample, from pileup
file.

Options:
-  -h, --help    show this help message and exit
-  -i IN_PILEUP  input file in mpileup format [REQUIRED]
-  -o OUT_CSV    output file in csv format [REQUIRED]


