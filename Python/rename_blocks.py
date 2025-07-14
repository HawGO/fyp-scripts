import os

def remove_fasta_phrase(directory):
    for filename in os.listdir(directory):
        if '.fasta' in filename:
            new_filename = filename.replace('.fasta', '')
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

directory_path = 'C:\\Users\\User\\Desktop\\fyp_data\\PDB'

remove_fasta_phrase(directory_path)
