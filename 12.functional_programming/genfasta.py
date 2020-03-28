from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.Data import CodonTable

def fastagen(path, tab=0):
    if tab == 0:
        tab = CodonTable.unambiguous_rna_by_name["Standard"]
    with open (path, "r") as fasta:
        for i in fasta:
            if i.startswith(">"):
                rna = Seq(i, IUPAC.unambiguous_rna)
                yield rna.translate(table=tab)


print(list(fastagen("...")))
