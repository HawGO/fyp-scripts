import csv
from Bio import SeqIO

def cut_sp(csv_file, fasta_file, output_file):
    cleavage_sites = {}
    
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        
        for row in reader:
            accession = row[0].strip()
            
            try:
                position = int(row[1])
                cleavage_sites[accession] = position
            except ValueError:
                print(f"Skipping invalid row: {row}")

    with open(fasta_file, 'r') as f_in, open(output_file, 'w') as f_out:
        
        for record in SeqIO.parse(f_in, "fasta"):
            accession = record.id.split()[0]
            
            if accession in cleavage_sites:
                cut_pos = cleavage_sites[accession]
                record.seq = record.seq[cut_pos:]
                
            SeqIO.write(record, f_out, "fasta")

cut_sp("cleavage_site.csv", "s1_protein.fasta", "s1_protein_no_sp.fasta")
