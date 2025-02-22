import os
import csv

def count_greater_than_signs(file_path):
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            count += line.count('>')
    return count

def search_a3m_files(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.a3m'):
                file_path = os.path.join(root, file)
                count = count_greater_than_signs(file_path)
                folder_name = os.path.basename(root)
                results.append([folder_name, count])
    return results

def write_to_csv(results, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Folder Name', 'Count of >'])
        writer.writerows(results)

if __name__ == "__main__":
    directory = input("Enter the directory to search for A3M files: ")
    output_file = input("Enter the output CSV file name: ")
    results = search_a3m_files(directory)
    write_to_csv(results, output_file)
