# Common Variants Finder

## Introduction
This Python script, `common_variants_finder.py`, is designed to identify common variants present in multiple VCF (Variant Call Format) files. It uses the `pysam` library to handle VCF files and the `tabix` command to index them efficiently.

## Requirements
- Python 3.x
- `pysam` library
- `tabix` command-line tool

## Installation
To install the required Python libraries, use the following command:
```bash
pip install pysam

## Usage
python common_variants_finder.py -O OUTPUT_FILE -I INPUT_VCF_FILES


## Output

The script generates a new VCF file containing variants that are common across all input VCF files. The output VCF file is specified by the user using the -O or --output_file option.

## Notes
The script indexes all input VCF files using tabix to optimize variant retrieval.
It utilizes pysam to read and process VCF files efficiently.
Error handling is implemented for cases where invalid contigs are encountered during the retrieval process.
