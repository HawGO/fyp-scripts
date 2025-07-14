from Bio import SeqIO
import csv

folder_path = 'C:\\Users\\User\\Desktop\\fyp_data\\orthocov_spike_prot.fasta'
csv_file_path = 'C:\\Users\\User\\Desktop\\fyp_data\\accession_name_genus.csv'
output_path = 'C:\\Users\\User\\Desktop\\fyp_data\\renamed.fasta'

def fasta_rename(fasta_file, csv_file, output_file):
    header_dict = {}

    with open(csv_file, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            accession = row['Accession']
            organism = row['Organism_Name'].replace('/', '-')
            genus = row['Genus']
            header_dict[accession] = f"{genus}_{organism}_{accession}"

    sequences = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        accession = record.id

        if accession in header_dict:
            record.id = header_dict[accession]
            record.description = ""

        sequences.append(record)

    SeqIO.write(sequences, output_file, "fasta")

fasta_rename(folder_path, csv_file_path, "output.fasta")
