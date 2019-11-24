
def subfile(inpath, outpath, beg=0, end=-1):
    '''

    :param inpath: full name of input file
    :param outpath: full name of output file (it will be rewrited!)
    :param beg: first line of new file
    :param end: last line of new file
    :return: none
    '''
    inp = open(inpath, 'r')
    outp = open(outpath, 'w')
    if end == -1:
        end = len(inp.readlines())   # number of lines
        inp.seek(0)
    s = 0
    for i in inp.readlines():
        if s >= beg and s <= end:
            outp.write(i)
        s = s + 1

    inp.close()
    outp.close()

subfile('', '', 0)
