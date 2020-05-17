from Bio import SeqIO
import sys
import argparse
import logging

logging.basicConfig(filename="assembler.log", filemode='w', format='%(asctime)s: %(message)s', datefmt="%Y.%m.%d: %H:%M:%S", level=logging.DEBUG)
logger = logging.getLogger(__name__)
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
            if read.seq[n:n + k] not in graph_w.keys():
                graph_w[sread[n:n + k]] = 1
            else:
                graph_w[sread[n:n + k]] += 1
            if n == 0:
                kmer = str(sread[n:n + k])
            else:
                if kmer not in graph_v.keys():
                    graph_v[kmer] = set()
                    graph_v[kmer].add(sread[n:n + k])
                    kmer = sread[n:n + k]
                else:
                    graph_v[kmer].add(sread[n:n + k])
                    kmer = sread[n:n + k]

    logger.debug("Counts of kmers are %s", graph_w)
    logger.debug("Relationships of kmers are %s", graph_v)
    v = None
    visited = {v: False for v in graph_v}
    logger.debug("All visited - false. %s", visited)
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
            logger.debug("Found the beginning")
            v = i
            break

    if v is None:
        logger.debug("Did not found the beginning")
        v = list(graph_v.keys())[0]

    seq = v
    count = graph_w[v]
    stop = "ok"

    for vertex in graph_v:
        while not visited[v]:      # searching for all seqs connected with first vertex
            visited[v] = True
            # Go to other vertex, adjacent to current, if they weren't visited before
            for neighbour in graph_v[v]:
                if neighbour in visited.keys():
                    if not visited[neighbour]:
                        logger.debug("We are here %s", (v, neighbour, visited))
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



parser = argparse.ArgumentParser()

parser.add_argument('-k', "--kmer_length", required=False, type=int, default=5,
                    help='length of kmer, default=5')
parser.add_argument('-f', "--fasta", required=True, type=str, help='path to input fasta file')
args = parser.parse_args()

logger.info("Given arguments are %s", args)

logger.info("Starting")
result = assembler(args.fasta, args.kmer_length)
logger.info("Writing fasta")

for i in result:
    print(">", i[1])
    print(i[0])

logging.info("Done")
