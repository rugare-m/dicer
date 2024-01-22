# Dicer

## Introduction
Dicer outputs common variants present in multiple VCF (Variant Call Format) files. bcftools isec does something similar but Dicer is more user friendly in that it will only output a single VCF of intersecting variants, and Dicer will index any VCF files that need indexing automatically. bcftools isec is more capable, but if you are looking for a simple tool to intersect variants from a set of VCF files, Dicer does the job. 

## Requirements
- Python 3.x and above 
- `pysam` library
- `tabix` command-line tool

## Arguments
-O, --output_file: Path to the output VCF file.

-I, --input_vcf_files: List of input VCF files to compare.

## Installation
Dicer does not need installation beyond the required libraries. You can install the required libraries with:
To install the required Python libraries, use the following command:
```bash
pip install pysam
```
and:
```bash
pip install tabix
```


## Example Usage 
```bash
python dicer.py -I toy1.vcf.gz toy2.vcf.gz toy3.vcf.gz toy4.vcf.gz -O intersect.vcf.gz
```

## Output
The script generates a new VCF file containing variants that are common across all input VCF files. The output VCF file is specified using the -O or --output_file option.

## Notes
The header of the output VCF file is simply copied over from first input VCF file. This shouldn't be an issue but worth remembering if you run into problems downstream. 
