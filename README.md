# Dicer

## Introduction
Dicer outputs common variants present in multiple VCF (Variant Call Format) files. bcftools isec does something similar but Dicer is more user friendly in that it will only output a single VCF of intersecting variants, and Dicer will index any VCF files that need indexing automatically. bcftools isec is more capable, but if you are looking for a simple tool to intersect variants from a set of VCF files, Dicer does the job. 

## Requirements
- `Python 3.x`
- `pysam` 
- `tabix` 

## Arguments
-O, --output_file: Path to the output VCF file.

-I, --input_vcf_files: List of input VCF files to compare.

## Installation
Dicer does not need installation beyond the required libraries. All you need to do is clone the repo and cd into dicer like so:

```bash
git clone https://github.com/rugare-m/dicer.git
```
and:

```bash
cd dicer
```

To install the required Python libraries, use the following command:
```bash
pip install pysam
```
and (provided you have conda installed):
```bash
conda install samtools
```

## Example Usage 
```bash
python dicer.py -I toy1.vcf.gz toy2.vcf.gz toy3.vcf.gz toy4.vcf.gz -O intersect.vcf.gz
```

## Output
The script generates a new VCF file containing variants that are common across all input VCF files. The output VCF file is specified using the -O or --output_file option.

## Notes
The header of the output VCF file is simply copied over from first input VCF file. This shouldn't be an issue but worth remembering if you run into problems downstream. Equally, the variant lines written to the output come from the first VCF file. The variants must be a match for chrom, pos, ref and alt in all VCFs to be written to the output. If more than one alt is described in the VCF, dicer will only consider the first alt allele. If this is a potential issue, it might be worth decomposing your VCFs before using this tool. 
