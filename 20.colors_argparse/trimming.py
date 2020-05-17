import argparse
from Bio import SeqIO
from Bio.Seq import Seq
import sys
import warnings


parser = argparse.ArgumentParser()

parser.add_argument('-s', "--cut_size_start", required=False, type=int,
                    help='length of sequence to cut from the beggining')
parser.add_argument('-e', "--cut_size_end", required=False, type=int,
                    help='length of sequence to cut from the end')
parser.add_argument('-b', "--cut_size_both", required=False, default=5, type=int,
                    help='use with -q argument, number of bases from the edge to count quality, default=5')
parser.add_argument('-q', "--cut_qual", required=False, type=int,
                    help='bases from the edges of the sequence with lower quality to cut, use with -b argument')
parser.add_argument('-f', "--fastq", required=True, type=str, help='path to input fastq file')

args = parser.parse_args()

reads = SeqIO.parse(args.fastq, "fastq")

if args.cut_size_end == args.cut_size_start == args.cut_qual == None:
    warnings.warn("No quality or edge lengths given, the same file will be returned!")

b = args.cut_size_both
if args.cut_qual != None:
    for i in reads:
        a = i
        quals = i.letter_annotations["phred_quality"]
        if sum(quals[:b]) / b < args.cut_qual:
            a = i[b:]
        if sum(quals[-b:]) / b < args.cut_qual:
            a = a[:-b]
        SeqIO.write(a, sys.stdout, "fastq")
else:
    if args.cut_size_end is None:
        args.cut_size_end = 0
    if args.cut_size_start is None:
        args.cut_size_start = 0
    print(args.cut_size_end, args.cut_size_start)
    for i in reads:
        if args.cut_size_end != 0:
            a = i[args.cut_size_start:-args.cut_size_end]
        else:
            a = i[args.cut_size_start:]
        SeqIO.write(a, sys.stdout, "fastq")


