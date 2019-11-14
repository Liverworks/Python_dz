l = [1,4,5,3,6,7,0,2]

def lin_search(l, el):
    """
    :param l: list
    :param el: element to find
    :return: index of element found
    """
    for ind, i in enumerate(l):
        if i == el:
            return ind



def bin_search(l, el, ind=0):
    """
    :param l: sorted list
    :param el: element to find
    :param ind: do not use
    :return: index of element found
    """
    a = len(l)//2
    if l[a] == el:
        return a + ind
    elif l[a] > el:
        l = l[0:a]
        return bin_search(l, el)
    else:
        l = l[a:len(l)]
        return bin_search(l, el, ind = a + ind)

print(lin_search(l, 1))
l = sorted(l)
print(l)
print(bin_search(l, 1))