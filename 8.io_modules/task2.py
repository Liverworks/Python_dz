
def subfile(inpath, outpath, beg=0, end=-1):
    '''
    Makes a copy of file or a copy of selected line interval
    :param inpath: full name of input file
    :param outpath: full name of output file (it will be rewrited!)
    :param beg: first line of new file
    :param end: last line of new file
    :return: none
    '''
    inp = open(inpath, 'r')
    outp = open(outpath, 'w')
    if end == -1:
        end = len(inp.readlines()) + 1  # number of lines
        inp.seek(0)
    s = 0
    for i in inp:
        if beg <= s < end:
            outp.write(i)
        s = s + 1

    inp.close()
    outp.close()

#subfile('', '', 1, 5)
