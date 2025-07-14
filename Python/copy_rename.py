import os
import shutil
import re

def copy_rename(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if "rank_001" in file:
                dir_name = os.path.basename(root)

                match = re.search(r"(YP|NP)_\S+_segment_\S+", dir_name)
                if match:
                    new_name_prefix = match.group(0)
                    new_file_name = f"{new_name_prefix}_pLDDT.json"

                    source_file = os.path.join(root, file)
                    destination_file = os.path.join(output_folder, new_file_name)

                    shutil.copy2(source_file, destination_file)
                    print(f"Copied and renamed: {source_file} -> {destination_file}")
                else:
                    print(f"Skipping directory {dir_name}: Doesn't match the expected pattern.")
                    continue

input_folder = "C:\\Users\\User\\Desktop\\fyp_data\\raw_ColabFold_JSON"
output_folder = "C:\\Users\\User\\Desktop\\af2_plddt"

copy_rename(input_folder, output_folder)
