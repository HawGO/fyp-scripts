import os
from collections import defaultdict

input_file = "ProP_output.txt"
output_folder = "C:\\Users\\User\\Desktop\\prop_output"

os.makedirs(output_folder, exist_ok=True)

groups = defaultdict(list)

with open(input_file, "r") as file:
    for line in file:
        stripped_line = line.strip()
        
        if not stripped_line:
            continue
        first_word = stripped_line.split()[0]
        groups[first_word].append(stripped_line)


for first_word, lines in groups.items():
    output_path = os.path.join(output_folder, f"{first_word}.txt")
    
    with open(output_path, "w") as outfile:
        outfile.write("\n".join(lines))
