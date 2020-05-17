from Bio import SeqIO
from Bio.Seq import Seq
import itertools
import time

def local_align(A, B, match=1, mism=-1, gap=-1):
    """
    Local alignment, I`m not sure, that it works good
    :param path: path to fasta file with 2 seqs
    :param match: match score
    :param mism: mismatch score
    :param gap: gap score
    :return: score and 2 aligned sequences as str
    """
    matrix = [[0] for i in range(len(B)+1)]   # making matrix with scores
    matrix[0] = [0 for i in range(len(A)+1)]
    for a in range(1, len(B)+1):    # filling the matrix
        for i in range(1, len(A)+1):
            if A[i-1] == B[a-1]:
                matrix[a].append(max(matrix[a - 1][i] + gap, matrix[a][i - 1] + gap, matrix[a - 1][i - 1] + match))
            else:
                matrix[a].append(max(matrix[a - 1][i] + gap, matrix[a][i - 1] + gap, matrix[a - 1][i - 1] + mism))
            if matrix[a][i] < 0:
                matrix[a][i] = 0
    #print(matrix)
    n = 0   # score
    a = 0
    i = 0
    maxn = min(matrix[-1])
    alignA = []
    alignB = []
    maxalignA = []
    maxalignB = []

    while a < len(B) and i < len(A):  # Going through the matrix with highest score on the way
        if matrix[a][i + 1] >= matrix[a + 1][i + 1] and matrix[a][i + 1] >= matrix[a + 1][i]:
            alignB.append("-")
            alignA.append(A[i])
            n = n + matrix[a][i + 1]
            i += 1
        elif matrix[a + 1][i] >= matrix[a + 1][i + 1] and matrix[a + 1][i] >= matrix[a][i + 1]:
            alignB.append(B[a])
            alignA.append("-")
            n = n + matrix[a + 1][i]
            a += 1
        elif matrix[a + 1][i + 1] >= matrix[a + 1][i] and matrix[a + 1][i + 1] >= matrix[a][i + 1]:
            alignB.append(B[a])
            alignA.append(A[i])
            n = n + matrix[a + 1][i + 1]
            a += 1
            i += 1
    if a == len(B):  # way from the edge to the corner
        while i < len(A):
            alignB.append("-")
            alignA.append(A[i])
            n = n + matrix[a][i + 1]
            i += 1
    elif i == len(A):
        while a < len(B):
            alignB.append(B[a])
            alignA.append("-")
            n = n + matrix[a + 1][i]
            a += 1
    # alignA.append("\n") # joining to sequences into one
    align = "".join(alignA + alignB)
    return n, "".join(alignA), "".join(alignB)

def naive_assembler(path, threshold=30):
    """
    Naive assembly of sequences
    :param path: path to fasta file
    :param threshold: score for counting an alignment as good enough
    :return: contigs as a list
    """
    reads = SeqIO.parse(path, "fasta")
    best=[]
    used=[]
    patch=[]
    last_best = tuple(best)
    for l1, l2 in itertools.combinations(reads, 2):
        test_alignment = local_align(l1.seq, l2.seq)
        #print(l1.seq)
        if (test_alignment[1].strip("-").find("-") != -1) or (test_alignment[2].strip("-").find("-") != -1):
            continue
        if test_alignment[0] > threshold:      # similar reads are now one read
            s = str()
            n = 0
            for i in test_alignment[1]:
                if i != '-':
                    s = s + i
                    n +=1
                else:
                    alnB = test_alignment[2]
                    s = s + alnB[n]
                    n += 1
            best.append(s)
            used.append(l1.name)        # remember their names
            used.append(l2.name)
        else:
            if l1.name not in used:
                patch.append(l1)
            if l2.name not in used:
                patch.append(l2)

    for i in patch:         # use reads again only if they are along
        if i.name not in used:
            best.append(i.seq)

    while last_best != tuple(best):     # stop then no changes
        last_best = tuple(best)
        # print(last_best == tuple(best))
        for l1, l2 in itertools.combinations(best, 2):      # now the same but immediately remove aligned reads
            test_alignment = local_align(l1, l2)
            if (test_alignment[1].strip("-").find("-") != -1) or (test_alignment[2].strip("-").find("-") != -1):
                continue
            if test_alignment[0] > threshold:
                s = str()
                n = 0
                for i in test_alignment[1]:
                    if i != '-':
                        s = s + i
                        n += 1
                    else:
                        alnB = test_alignment[2]
                        s = s + alnB[n]
                        n += 1
                best.append(s)
                #print(best)
                best.remove(l1)
                best.remove(l2)
                break
    return best

print(naive_assembler("test1.fa", threshold=10))


start = time.time()
naive_assembler("test2.fa", threshold=10)
stop = time.time()

print(stop - start)