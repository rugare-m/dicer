import argparse
import pysam
import subprocess

def find_common_variants(input_vcf_files, output_file):
    # index all input VCFs
    for vcf_file in input_vcf_files:
        subprocess.run(['tabix', '-p', 'vcf', '-f', vcf_file])

    # open VCF files
    vcf_readers = []

    try:
        vcf_readers = [pysam.VariantFile(vcf_file) for vcf_file in input_vcf_files]

        # create new VCF file for output, with header from first input VCF
        output_vcf = pysam.VariantFile(output_file, 'w', header=vcf_readers[0].header)

        #for vcf_reader in vcf_readers:
        #    if not vcf_reader.index:
        #        vcf_reader.index

        # iterate through variants in first VCF file
        for record in vcf_readers[0]:
            chrom = record.chrom
            pos = record.pos
            ref = record.ref
            alt = record.alts[0]

            # Check if  variant is (not) present in all other VCF files
            if all(
                any(rec.chrom == chrom and rec.pos == pos and rec.ref == ref and rec.alts[0] == alt for rec in
                    vcf_reader.fetch(chrom, pos - 1, pos)) for vcf_reader in vcf_readers[1:]
            ):
                output_vcf.write(record)

    except Exception as e:
        # error handling for invalid contigs - pysam fetch() doesnt like wierd contig names
        error_message = str(e)
        if "invalid contig" in error_message:
            print(f"Error: {error_message} - skipping contig")
        else:
            # re-raise  exception if unrelated to invalid contigs
            raise
    finally:
        # close VCF files
        for vcf_reader in vcf_readers:
            vcf_reader.close()

        if 'output_vcf' in locals():
            output_vcf.close()

def main():
    parser = argparse.ArgumentParser(description="Find common variants in multiple VCF files.")
    parser.add_argument("-O", "--output_file", required=True, help="Output VCF file path")
    parser.add_argument("-I", "--input_vcf_files", nargs='+', required=True, help="Input VCF files")

    args = parser.parse_args()
    find_common_variants(args.input_vcf_files, args.output_file)

if __name__ == "__main__":
    main()