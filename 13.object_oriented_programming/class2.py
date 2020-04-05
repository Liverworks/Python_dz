from Bio import SeqIO
import seaborn as sns
import matplotlib.pyplot as plt
import itertools

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
        self.fa = SeqIO.parse(path, "fasta")

    def __len__(self):
        """
        :return: The number of sequences
        """
        c = 0
        for i in self.fa:
                c += 1
        self.fa = SeqIO.parse(self.path, "fasta")
        return c

    def __str__(self):
        return self.path

    def len_hist(self):
        """
        Shows sequences lengths distribution as a bar plot.
        """
        l = []
        for i in self.fa:
            l.append(len(i))
        sns.distplot(l, bins=25, kde=False)
        plt.title("Sequence lengths")
        plt.show()
        self.fa = SeqIO.parse(self.path, "fasta")

    def gc(self):
        """
        :return: List of G and C percent in each sequence
        """
        l = []
        for line in self.fa:
            gc = 0
            line_len = len(line)
            for letter in line:
                if letter == "G" or letter == "C":
                    gc += 1
            l.append(gc / line_len)
        self.fa = SeqIO.parse(self.path, "fasta")
        return l

    def kmers(self):
        """
        Search for kmers, length 4
        :return: A list of dictionaries with number of each kmer in each sequense
        """
        full_l = []
        kmers = ["".join(x) for x in itertools.combinations_with_replacement("ACGT", 4)]
        for line in self.fa:
            l = dict.fromkeys(kmers, 0)
            print(l)
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
            print(l)
            sns.barplot(x = list(l.keys()), y = list(l.values()))
            plt.title('Kmers')
            plt.xticks(rotation=90)
            plt.show()
        self.fa = SeqIO.parse(self.path, "fasta")

    def explore(self):
        """
        Call all functions for an object of Fasta class
        """
        print(self)
        print("Number of sequences")
        len(self)
        self.len_hist()
        print("GC content in all sequences")
        self.gc()
        self.kmers()

fasta1 = Fasta("/home/anna/ib/smfas.fasta")

print(fasta1)

fasta1.len_hist()

print(fasta1.gc())

print(fasta1.kmers())
