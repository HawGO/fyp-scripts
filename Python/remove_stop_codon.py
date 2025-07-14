def remove_stop_codon(sequence):
    return sequence[:-3]

def parse_multi(input_fasta, output_fasta):
    with open(input_fasta, 'r') as infile, open(output_fasta, 'w') as outfile:
        sequence = ""
        header = ""
        
        for line in infile:
            line = line.strip()
            
            if line.startswith(">"):
                if sequence:
                    cleaned_sequence = remove_stop_codon(sequence)
                    outfile.write(f"{header}\n{cleaned_sequence}\n")

                header = line
                sequence = ""
            else:
                sequence += line
        
        if sequence:
            cleaned_sequence = remove_stop_codon(sequence)
            outfile.write(f"{header}\n{cleaned_sequence}\n")

input_fasta = "C:\\Users\\User\\Desktop\\spike_cds.fasta"
output_fasta = "spike_nostop.fasta"

parse_multi(input_fasta, output_fasta)
