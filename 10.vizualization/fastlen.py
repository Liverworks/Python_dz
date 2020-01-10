import seaborn as sns
import matplotlib.pyplot as plt

def fastlen(path):
    """
    Histogram of sequence lengths
    :param path: path to fasta file
    """
    l = []
    with open(path, "r") as fast:
        for i in fast:
            if i[0] != ">":
                l.append(len(i))

    sns.distplot(l, bins=25, kde=False)
    plt.show()



fastlen("/home/anna/laba/prot.fasta")
