import os
import csv

genes_path = './Genes'
viruses_path = './Viruses'
spreadsheet_path = './saha_dibbyo_assignment2_spreadsheet.csv'

def allowed_range(gene_length):
    return max(5, min(20, int(0.01 * gene_length)))

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        sequence = ''.join(line.strip() for line in lines[1:])
    return sequence

def compare(gene_seq, virus_seq):
    allowed = allowed_range(len(gene_seq))
    mismatches = []
    for i in range(len(virus_seq) - len(gene_seq) + 1):
        mismatch_count = 0
        current = []
        for j in range(len(gene_seq)):
            if gene_seq[j] != virus_seq[i + j]:
                mismatch_count += 1
                current.append(f"{gene_seq[j]}{j+1}{virus_seq[i + j]}")
            if mismatch_count > allowed:
                break;
        if mismatch_count <= allowed:
            mismatches.extend(current)
    return mismatches

def load_sequences(folder):
    sequences = []
    filenames = []
    for filename in os.listdir(folder):
        if filename.endswith('.fasta'):
            file_path = os.path.join(folder, filename)
            names = filename.replace('.fasta', '')
            sequences.append(read_file(file_path))
            filenames.append(names)
    return filenames, sequences

gene_names, gene_sequences = load_sequences(genes_path)
virus_names, virus_sequences = load_sequences(viruses_path)

with open(spreadsheet_path, mode = 'w', newline = '') as file:
    writer = csv.writer(file)
    header = ['Virus'] + gene_names
    writer.writerow(header)
    for virus_index, virus_seq in enumerate(virus_sequences):
        row = [virus_names[virus_index]]
        for gene_index, gene_seq in enumerate(gene_sequences):
            mismatches = compare(gene_seq, virus_seq)
            row.append(mismatches)
        writer.writerow(row)