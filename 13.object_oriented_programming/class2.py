from Bio import SeqIO
import seaborn as sns
import matplotlib.pyplot as plt

class PositiveSet(set):
    """
    Like set, but it is forbidden to add negative numbers
    """
    def __init__(self, *args):
        """
        :param args: should be numbers
        """
        l = []
        for i in args:
            if i <= 0:
                continue
            else:
                l.append(i)
        super().__init__(l)

    def add(self, element):
        """
        Adds a number to the set
        :param element: a number, negative will be ignored
        :return: PositiveSet with number added
        """
        if element > 0:
            super().add(element)


se = {1, 3, 4}

a = PositiveSet()
a.add(4)
a.add(-9)
se.add(8)

b = PositiveSet(1, 3, 4)

print(a, b, se)


class Fasta():
    """
    Stores a .fasta file and its path
    """
    def __init__(self, path):
        self.path = path
        self.fa = open(path, "r")

    def __len__(self):
        """
        :return: The number of sequences
        """
        c = 0
        for i in self.fa:
            if i[0] == ">":
                c += 1
        return c

    def __str__(self):
        return self.path

    def hist(self):
        """
        Shows sequences lengths distribution as a bar plot.
        """
        l = []
        for i in SeqIO.parse((self.fa), 'fasta'):
            l.append(len(i))
        sns.distplot(l, bins=25, kde=False)
        plt.show()
        self.fa.seek(0)

    def gc(self):
        """
        :return: List of G and C percent in each sequence
        """
        l = []
        for i in SeqIO.parse((self.fa), 'fasta'):
            c = 0
            ll = len(i)
            for a in i:
                if a == "G" or a == "C":
                    c += 1
            l.append(c / ll)
        self.fa.seek(0)
        return l

    def kmers(self):
        """
        Search for kmers, length 4
        :return: A list of dictionaries with number of each kmer in each sequense
        """
        full_l = []
        for line in SeqIO.parse((self.fa), 'fasta'):
            l = {}
            for i in range(len(line)-3):
                kmer = line[i:i+4]
                # Find every occurrence of each kmer
                count = 0
                a = -1
                while True:
                    a = line.seq.find(str(kmer.seq), a + 1)
                    if a == -1:
                        l[str(kmer.seq)] = count
                        break
                    count += 1

            full_l.append(l)
        self.fa.seek(0)
        return full_l



fasta1 = Fasta("/home/anna/ib/smfas.fasta")

print(fasta1)

fasta1.hist()

print(fasta1.gc())

print(fasta1.kmers())

