from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.Data import CodonTable


class Rnas:
    def __init__(self, name, seq, straight=True):
        self.straight = straight
        self.name = name
        self.seq = seq
        self.length = len(seq)
        if not self.straight:
            self.seq = self.seq[::-1]
            self.straight = True

    def translate(self):
        """
        Makes a protein seq out of RNA seq
        :return: protein seq as Bio.Seq object
        """
        tab = CodonTable.unambiguous_rna_by_name["Standard"]
        rna = Seq(self.seq, IUPAC.unambiguous_rna)
        return rna.translate(table=tab)

    def smart_translate(self):
        """
        Makes a protein seq out of the first ORF
        :return: a protein seq
        """
        tab = CodonTable.unambiguous_rna_by_name["Standard"]
        for i in range(self.length):
            if self.seq[i:i + 3] == "AUG":
                rna = Seq(self.seq[i:self.length], IUPAC.unambiguous_rna)
                strrna = str(rna.translate(table=tab))
                return strrna[:strrna.find("*") + 1]
        return "No ORFs"

    def rev_tr(self):
        """
        Makes complementary DNA seq
        :return: DNA seq
        """
        dna = self.seq[::-1]
        dna = dna.translate(dna.maketrans("AUGC", "TACG"))
        return dna


tst = Rnas("Test RNA", "AAAAUGAUGGGCCGCAGCAGUAGUUAGUUUAGU")

print(tst)
print(tst.name)
print(tst.length)
print(tst.seq)
print(tst.straight)
print(tst.translate())
print(tst.rev_tr())
print(tst.smart_translate())


class RealRna:
    soluble_in_water = True
    soluble_in_organic = False

    def __init__(self, name, rna_type="Unknown", solved=False, isolated=False):
        self.name = name
        self.rna_type = rna_type
        self.solved = solved
        self.isolated = isolated

    def degradate(self):
        """
        Degradate the RNA
        """
        self.name = "Forget it"
        self.rna_type = None
        self.solved = None
        self.isolated = None

    def isolate(self):
        """
        Now you can solve your RNA
        """
        self.isolated = True

    def solute(self):
        """
        Adding some water
        """
        if not self.isolated:
            return "Isolate first"
        else:
            self.solved = True
