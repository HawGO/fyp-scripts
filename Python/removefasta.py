import os

def remove_fasta(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if ".fasta" in file:
                new_file_name = file.replace(".fasta", "")

                source_file = os.path.join(root, file)
                destination_file = os.path.join(root, new_file_name)

                os.rename(source_file, destination_file)
                print(f"Renamed: {source_file} -> {destination_file}")

folder_path = "C:\\Users\\User\\Desktop\\af2_plddt"
remove_fasta(folder_path)
