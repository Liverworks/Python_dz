from Bio import SeqIO

input = SeqIO.parse(path_to_input, "fasta")

for i in input:
    a = i
    SeqIO.write(a, path_to_output, "fasta")