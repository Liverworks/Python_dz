def fastq2fasta(pathq, patha, n=50):
    """
    Converts fastq into fasta
    :param pathq: path to fastq file
    :param patha: path to new fasta file (will ne rewrited)
    :param n: use only sequences longer than n
    """
    i = 0
    with open(pathq, "r") as fastq:
        with open(patha, "w") as fasta:
            for line in fastq:
                i += 1
                if i % 4 == 1:
                    title = ">" + line[1:len(line)]
                if i % 4 == 2 and len(line) >= n:
                    fasta.write(title)
                    fasta.write(line)


def global_align(path, match=1, mism=-1, gap=-1):
    """
    Global alignment
    :param path: path to fasta file with 2 seqs
    :param match: match score
    :param mism: mismatch score
    :param gap: gap score
    :return: score and 2 aligned sequences
    """
    with open(path, "r") as fasta:  # read sequences from file
        lines = fasta.readlines()
        A = lines[1].strip()
        B = lines[3].strip()
    matrix = [[i * gap] for i in range(len(B)+1)]   # making matrix with scores
    matrix[0] = [i * gap for i in range(len(A)+1)]
    for a in range(1, len(B)+1):    # filling the matrix
        for i in range(1, len(A)+1):
            if A[i-1] == B[a-1]:
                matrix[a].append(max(matrix[a - 1][i] + gap, matrix[a][i - 1] + gap, matrix[a - 1][i - 1] + match))
            else:
                matrix[a].append(max(matrix[a - 1][i] + gap, matrix[a][i - 1] + gap, matrix[a - 1][i - 1] + mism))
    i = 0
    a = 0
    n = 0   # score
    alignA = []
    alignB = []
    while a < len(B) and i < len(A):    # Going through the matrix with highest score on the way
        if matrix[a][i + 1] >= matrix[a + 1][i + 1] and matrix[a][i + 1] >= matrix[a + 1][i]:
            alignB.append("-")
            alignA.append(A[i])
            n = n + matrix[a][i + 1]
            i += 1
        elif matrix[a + 1][i + 1] >= matrix[a + 1][i] and matrix[a + 1][i + 1] >= matrix[a][i + 1]:
            alignB.append(B[a])
            alignA.append(A[i])
            n = n + matrix[a + 1][i + 1]
            a += 1
            i += 1
        elif matrix[a + 1][i] >= matrix[a + 1][i + 1] and matrix[a + 1][i] >= matrix[a][i + 1]:
            alignB.append(B[a])
            alignA.append("-")
            n = n + matrix[a + 1][i]
            a += 1
    print(matrix)
    if a == len(B):     # way from the edge to the corner
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
    alignA.append("\n") # joining to sequences into one
    align = "".join(alignA + alignB)
    return n, align



# fastq2fasta("/home/anna/ib/Sample_EveT12_1_csn.fastq", "/home/anna/ib/Sample_EveT12_1_csn.fasta")

print(global_align("/home/anna/ib/Sample_EveT12_1_csn.fasta"))



def local_align(path, match=1, mism=-1, gap=-1):
    """
    Local alignment, I`m not sure, that it works good
    :param path: path to fasta file with 2 seqs
    :param match: match score
    :param mism: mismatch score
    :param gap: gap score
    :return: score and 2 aligned sequences as str
    """
    with open(path, "r") as fasta:  # read sequences from file
        lines = fasta.readlines()
        A = lines[1].strip()
        B = lines[3].strip()
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
    n = 0   # score
    a = 0
    i = 0
    maxn = min(matrix[-1])
    alignA = []
    alignB = []
    maxalignA = []
    maxalignB = []
    """    for e in range(len(B)): # Doing global alignment from and to every possible coordinate
        for b in range(len(A)):
            for c in range(1, len(A)):
                for d in range(1, len(B)):
                    a = e
                    i = b
                    if c <= i or d <= a:
                        continue
                    n = 0
                    while a < d and i < c:    # Going through the matrix with highest score on the way
                        if matrix[a + 1][i + 1] >= matrix[a][i + 1] and matrix[a + 1][i + 1] >= matrix[a + 1][i]:
                            alignB.append(B[a])
                            alignA.append(A[i])
                            n = n + matrix[a + 1][i + 1]
                            a += 1
                            i += 1
                        elif matrix[a + 1][i] >= matrix[a + 1][i + 1] and matrix[a + 1][i] >= matrix[a][i + 1]:
                            alignB.append(B[a])
                            alignA.append("-")
                            n = n + matrix[a + 1][i]
                            a += 1
                        elif matrix[a][i + 1] >= matrix[a + 1][i + 1] and matrix[a][i + 1] >= matrix[a + 1][i]:
                            alignB.append("-")
                            alignA.append(A[i])
                            n = n + matrix[a][i + 1]
                            i += 1
                    if a == d:  # way from the edge to the corner
                        while i < c:
                            alignB.append("-")
                            alignA.append(A[i])
                            n = n + matrix[a][i + 1]
                            i += 1
                    elif i == c:
                        while a < d:
                            alignB.append(B[a])
                            alignA.append("-")
                            n = n + matrix[a + 1][i]
                            a += 1
                    if n > maxn:    # choose max score
                        maxn = n
                        maxalignA = "".join(alignA)
                        maxalignB = "".join(alignB)
                    alignA.clear()
                    alignB.clear()"""
    while a < len(B) and i < len(A):  # Going through the matrix with highest score on the way
        if matrix[a][i + 1] >= matrix[a + 1][i + 1] and matrix[a][i + 1] >= matrix[a + 1][i]:
            alignB.append("-")
            alignA.append(A[i])
            n = n + matrix[a][i + 1]
            i += 1
        elif matrix[a + 1][i + 1] >= matrix[a + 1][i] and matrix[a + 1][i + 1] >= matrix[a][i + 1]:
            alignB.append(B[a])
            alignA.append(A[i])
            n = n + matrix[a + 1][i + 1]
            a += 1
            i += 1
        elif matrix[a + 1][i] >= matrix[a + 1][i + 1] and matrix[a + 1][i] >= matrix[a][i + 1]:
            alignB.append(B[a])
            alignA.append("-")
            n = n + matrix[a + 1][i]
            a += 1
    print(matrix)
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
    alignA.append("\n") # joining to sequences into one
    align = "".join(alignA + alignB)
    return n, align

print(local_align("/home/anna/ib/Sample_EveT12_1_csn.fasta"))