def fastagen(path, tab=0):
    from Bio.Seq import Seq
    from Bio.Alphabet import IUPAC
    from Bio.Data import CodonTable
    if tab == 0:
        tab = CodonTable.unambiguous_rna_by_name["Standard"]
    with open (path, "r") as fasta:
        for i in fasta:
            if i[0] != ">":
                rna = Seq(i, IUPAC.unambiguous_rna)
                yield rna.translate(table=tab)


print(list(fastagen("...")))
