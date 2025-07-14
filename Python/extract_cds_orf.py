from Bio import SeqIO

def extract_cds(input_fasta):
    with open(input_fasta, "r") as fasta_file:
        for record in SeqIO.parse(fasta_file, "fasta"):
            header = record.id.replace(" ", "_")
            filename = f"{header}.fasta"
            with open(filename, "w") as output_file:
                SeqIO.write(record, output_file, "fasta")
            print(f"CDS written to: {filename}")

extract_cds("C:\\Users\\User\\Desktop\\fyp_final\\nsp12_trimmed.fasta")
