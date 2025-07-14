from Bio import SeqIO
import csv

def calculate_gc_content(seq):
    gc_count = seq.count('G') + seq.count('C')
    return (gc_count / len(seq)) * 100

def main(fasta_file, output_csv):
    with open(output_csv, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Header', 'GC Content (%)'])

        for record in SeqIO.parse(fasta_file, 'fasta'):
            header = record.id
            sequence = str(record.seq)
            gc_content = calculate_gc_content(sequence)
            csvwriter.writerow([header, gc_content])

if __name__ == '__main__':
    fasta_file = 'C:\\Users\\User\\Desktop\\fyp_data\\Sequences\\spike_cds.fasta'
    output_csv = 'C:\\Users\\User\\Desktop\\fyp_data\\spike_gc.csv'
    main(fasta_file, output_csv)
