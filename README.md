# QiimeMetadataTranslate
# Language: Python
# Input: TXT
# Output: DIR
# Tested with: PluMA 1.1, Python 3.6

PluMA plugin to take the user-specified Qiime2 metadata and 
translate to three other files in the user-specified output directory:

metadata.tsv: Simple TSV file, without the additional Qiime2 header
sample_data.csv: Comma-separated value (CSV) file (useful for PhyloSeq)
sample_data.beta.csv: CSV file with additional column for sample name, useful for beta-diversity plots
