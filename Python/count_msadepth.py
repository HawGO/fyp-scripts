import os
import csv

def count_seq(file_path):
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            count += line.count('>')
    return count

def a3m_search(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.a3m'):
                file_path = os.path.join(root, file)
                count = count_seq(file_path)
                folder_name = os.path.basename(root)
                results.append([folder_name, count])
    return results

def write_to_csv(results, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Folder Name', 'Count of >'])
        writer.writerows(results)

if __name__ == "__main__":
    directory = 'C:\\Users\\User\\Desktop\\fyp_data\\raw_ColabFold_a3m
    output_file = 'colabfold_msa_depth.csv'
    results = a3m_search(directory)
    write_to_csv(results, output_file)
