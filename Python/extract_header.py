def extract_headers(fasta_file, output_file):
    with open(fasta_file, 'r') as file, open(output_file, 'w') as out:
        for line in file:
            if line.startswith('>'):
                out.write(line)
    print(f"Headers extracted and saved to {output_file}")

fasta_file = 'C:\\Users\\User\\Desktop\\spike_cds_wout.fasta'
output_file = 'headers.txt'
extract_headers(fasta_file, output_file)
