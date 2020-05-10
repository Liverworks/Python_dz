import argparse
from Bio import SeqIO
from Bio.Seq import Seq
import sys

parser = argparse.ArgumentParser()

parser.add_argument('-s', "--cut_size_start", required=False, type=int, nargs=1,
                    help='length of sequence to cut from the beggining')
parser.add_argument('-e', "--cut_size_end", required=False, type=int, nargs=1,
                    help='length of sequence to cut from the end')
parser.add_argument('-b', "--cut_size_both", required=False, default=5, type=int, nargs=1,
                    help='use with -q argument, number of bases from the edge to count quality, default=5')
parser.add_argument('-q', "--cut_qual", required=False, type=int, nargs=1,
                    help='bases from the edges of the sequence with lower quality to cut, use with -b argument')
parser.add_argument('-f', "--fastq", required=True, type=str, nargs=1, help='path to input fastq file')

args = parser.parse_args()
if args.cut_size_both == 5:
    b = args.cut_size_both
else:
    b = args.cut_size_both[0]

reads = SeqIO.parse(args.fastq[0], "fastq")
print(args.cut_size_end, args.cut_size_start)
if args.cut_qual != None:
    for i in reads:
        a = i
        quals = i.letter_annotations["phred_quality"]
        if sum(quals[:b]) / b < args.cut_qual[0]:
            a = i[b:]
        if sum(quals[-b:]) / b < args.cut_qual[0]:
            a = a[:-b]
        SeqIO.write(a, sys.stdout, "fastq")
else:
    if args.cut_size_end == None:
        args.cut_size_end = 0
    else:
        args.cut_size_end =  args.cut_size_end[0]
    if args.cut_size_start == None:
        args.cut_size_start = 0
    else:
        args.cut_size_start =  args.cut_size_start[0]
    print(args.cut_size_end, args.cut_size_start)
    for i in reads:
        if args.cut_size_end != 0:
            a = i[args.cut_size_start:-args.cut_size_end]
        else:
            a = i[args.cut_size_start:]
        SeqIO.write(a, sys.stdout, "fastq")

