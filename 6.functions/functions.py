def fibo(n):
    """
    :param n: int
    :return: fibonachi number of a given number
    """
    if n == 0:
        return 0
    if n == 2 or n == 1:
        return 1
    return fibo(n-2) + fibo(n-1)


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



def flatten(l, flat_list=None):
    """
    :param l: list
    :param flat_list: needed for proper work, do not use
    :return: list without inserted lists
    """
    if flat_list is None:
        flat_list = []
    for i in l:
        if type(i) == list:
            flatten(i, flat_list)
        else:
            flat_list.append(i)
    return flat_list







def reverse(l):
    """
    :param l: list
    :return: reversed list
    """
    length = 0
    rev_l = []
    for i in l:
        length += 1
    for i in range(length):
        rev_l.append(l[length - i-1])
    return rev_l



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



def get(input, index):
    """
    :param input: list or tuple or dict
    :param index: index of needed element
    :return: element from input of given index
    """
    return input[index]


print(maximum([100, 2, 3, 405, -2, 4]))

print(fibo(8))

print(flatten([1, [1, 2], 3, [[4, 5, [6], 7, 8, [9, 10, 11]]]]))
print(flatten([1, 2, 3]))

print(reverse([100, 2, 3, 45, -2, 4]))

print(mean([100, 2, 3, 45, -2, 4]))

print(*moda([100, 3, 100, 2, 45, 45, 45, 3, 45, 3, 3, -2, 4]))

print(get([1, 2, 15, 36], 2))

print(get((1, 2, 15, 36), -1))

print(get({1: 2, 'kva': 36}, 'kva'))