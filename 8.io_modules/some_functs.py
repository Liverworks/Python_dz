def maximum(l):
    """
    :param l: list of numbers
    :return: maximum value from the list
    """
    m = l[0]
    for i in l:
        if i > m:
            m = i
    return m

def mean(l):
    """
    :param l: list of numbers
    :return: mean of the list
    """
    length = 0
    m = int()
    for i in l:
        length += 1
        m += i
    return m/length



def moda(l):
    """
    :param l: list
    :return: mode values of the given list as list
    """
    dict_l = {}
    mod = []
    for i in l:
        dict_l[i] = dict_l.get(i, 0) + 1
    m = maximum(list(dict_l.values()))
    for i in dict_l:
        if dict_l[i] == m:
            mod.append(i)
    return mod