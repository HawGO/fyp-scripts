import os
from Bio import SeqIO

def aa2nt_pos(aa_position):
    return aa_position * 3

def cleave(sequence, cleavage_position):
    s1 = sequence[:cleavage_position] #Split seq at cleavage pos
    s2 = sequence[cleavage_position:]
    
    return s1, s2

def process_multi(fasta_file_path, cleave_file, output_folder):
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(cleave_file, 'r') as file:
        cleave_positions = {}
        
        for line in file:
            if line.strip():
                seq_id, cleave_position_str = line.split('\t')
                cleave_positions[seq_id.strip()] = int(cleave_position_str.strip())
    
    with open(fasta_file_path, 'r') as file:
        sequences = list(SeqIO.parse(file, 'fasta'))
    
    for record in sequences:
        seq_id = record.id

        if seq_id in cleave_positions:
            aa_position = cleave_positions[seq_id]
            
            nucleotide_position = aa2nt_pos(aa_position)

            s1, s2 = cleave(record.seq, nucleotide_position)

            record_s1 = record[:]
            record_s1.seq = s1
            record_s1.id += '_s1'

            record_s2 = record[:]
            record_s2.seq = s2
            record_s2.id += '_s2'

            output_s1_path = os.path.join(output_folder, f"{record.id}_s1.fasta")
            output_s2_path = os.path.join(output_folder, f"{record.id}_s2.fasta")
            
            SeqIO.write(record_s1, output_s1_path, 'fasta')
            SeqIO.write(record_s2, output_s2_path, 'fasta')

            print(f"Processed {record.id} and saved cleaved sequences.")
        else:
            print(f"Warning: No cleavage position found for {seq_id}. Skipping.")

if __name__ == "__main__":
    fasta_file_path = input("Enter the path to the FASTA file: ")
    cleave_file = input("Enter the path to the tab-delimited TXT file: ")
    output_folder = input("Enter the folder to save the output files: ")
    
    process_multi(fasta_file_path, cleave_file, output_folder)
    print("Processing complete.")
