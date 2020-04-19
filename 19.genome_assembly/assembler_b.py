from Bio import SeqIO

def assembler(path, k=5):
    """
    Primitive assembler
    :param path: path to fasta
    :param k: k-1-mer length
    :return: contigs and their score
    """
    reads = SeqIO.parse(path, "fasta")
    contigs = []
    graph_w = {}
    graph_v = {}

    for read in reads:  # making to dicts - with weights and with neighbours
        sread = str(read.seq)
        for n in range(len(sread) - k + 1):
            if read.seq[n:n+k] not in graph_w.keys():
                graph_w[sread[n : n + k]] = 1
            else:
                graph_w[sread[n : n + k]] += 1
            if n == 0:
                kmer = str(sread[n : n + k])
            else:
                if kmer not in graph_v.keys():
                    graph_v[kmer] = set()
                    graph_v[kmer].add(sread[n : n + k])
                    kmer = sread[n : n + k]
                else:
                    graph_v[kmer].add(sread[n : n + k])
                    kmer = sread[n : n + k]

    # print(graph_w)
    # print(graph_v)

    visited = {v: False for v in graph_v}
    # print(visited)
    f = None
    for i in graph_v.keys():        # take first vertex
        for a in graph_v.values():
            for b in a:
                if b == i:
                    f = "is"
        if f == "is":
            f = "not"
            continue
        else:
            v = i
            break

    #visited[v] = True
    seq = v
    count = graph_w[v]
    stop = "ok"
    #graph_w[seq1] = (graph_w[v])
    for vertex in graph_v:
        while not visited[v]:      # searching for all seqs connected with first vertex
            visited[v] = True
            # Go to other vertex, adjacent to current, if they weren't visited before
            for neighbour in graph_v[v]:
                if not visited[neighbour]:
                    # print(v, neighbour, visited)
                    seq += neighbour[-1]
                    graph_w[seq] = (count + graph_w[neighbour]) / 2
                    count = (count + graph_w[neighbour]) / 2
                    v = neighbour
                break
        if stop != "Stop":
            contigs.append((seq, graph_w[seq]))
        if not visited[vertex]:
            v = vertex
        else:
            stop = "Stop"

    return contigs

print(assembler("test2.fasts"))
