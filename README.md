# Dicer

## Introduction
Dicer is written to output common variants present in multiple VCF (Variant Call Format) files. The program will index VCF files if no index file (*tbi) is found in the working directory. 

## Requirements
- Python 3.x and above 
- `pysam` library
- `tabix` command-line tool

## Arguments
-O, --output_file: Path to the output VCF file.
-I, --input_vcf_files: List of input VCF files to compare.

## Installation
To install the required Python libraries, use the following command:
```bash
pip install pysam
```

## Example Usage 
python dicer.py -I toy1.vcf.gz toy2.vcf.gz toy3.vcf.gz toy4.vcf.gz -O intersect.vcf.gz


## Output
The script generates a new VCF file containing variants that are common across all input VCF files. The output VCF file is specified using the -O or --output_file option.

## Notes
The header of the output VCF file is simply copied over from first input VCF file. This shouldn't be an issue but worth remembering if you run into problems downstream. 
