import os
from Bio import SeqIO

def segment_protein(sequence, segment_length=400, step=100):
    segments = []
    
    for i in range(0, len(sequence), step):
        
        segment = sequence[i:i + segment_length]
        
        if len(segment) == segment_length:
            segments.append(segment)

    if len(sequence) > segment_length:
        final_segment = sequence[-segment_length:]
        
        if final_segment not in segments:
            segments.append(final_segment)
            
    return segments

def process_fasta(fasta_file):
    for record in SeqIO.parse(fasta_file, "fasta"):
        header = record.id
        sequence = str(record.seq)
        segments = segment_protein(sequence)
        
        if not os.path.exists(header):
            os.makedirs(header)
        
        for idx, segment in enumerate(segments):
            segment_file = os.path.join(header, f"{header}_segment_{idx + 1}.fasta")
            
            with open(segment_file, "w") as f:
                f.write(f">{header}_segment_{idx + 1}\n")
                f.write(f"{segment}\n")

if __name__ == "__main__":
    fasta_file = "C:\\Users\\User\\Desktop\\fyp_data\\Sequences\\add_out.fasta"
    process_fasta(fasta_file)


