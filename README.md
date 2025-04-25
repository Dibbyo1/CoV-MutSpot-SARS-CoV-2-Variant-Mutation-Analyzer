# CoV-MutSpot-SARS-CoV-2-Variant-Mutation-Analyzer
CoV-MutSpot is a bioinformatics tool written in Python that identifies mutation hotspots in SARS-CoV-2 virus variants by comparing them to the reference genome (RefSeq: NC_045512.2). It processes gene-level comparisons and summarizes nucleotide mismatches, helping researchers better understand how COVID-19 variants differ at a genomic level. This project compares 12 genes (e.g., envelope, membrane, ORF1a, surface) from the SARS-CoV-2 reference genome against multiple virus variants to detect mutation hotspots. A mismatch is recorded when the nucleotide at a specific position differs from the reference gene. The results are organized in a structured .csv file listing the specific mutations for each variant.

# Features
Detects mutations across 12 different SARS-CoV-2 genes.</br>
Outputs mutation summary in a structured CSV.</br>
Configurable mismatch tolerance (min 5 to max 20 or 1% of gene length).</br>
Reads input from properly organized FASTA files in Genes/ and Viruses/ folders.</br>
Includes a detailed report in PDF format.</br>
