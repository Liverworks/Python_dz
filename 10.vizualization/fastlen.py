
def fastlen(path):

    import seaborn as sns
    import matplotlib.pyplot as plt

    l = []
    with open(path, "r") as fast:
        for i in fast:
            if i[0] != ">":
                l.append(len(i))

    sns.boxplot(l)
    plt.show()



fastlen("/home/anna/laba/prot.fasta")
