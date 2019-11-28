def bubble_sort(l):
    """
    bubble sort
    :param l: a list of numbers
    :return: sorted list
    """
    for i in range(len(l) - 1):
        a = 0
        for el in range(len(l) - 1):
            if l[el] > l[el + 1]:
                l[el], l[el + 1] = l[el + 1], l[el]
                a = 1
        if a == 0:
            break  # if the list is already sorted - break
    return l



def gene_search(s):
    """
    Search ORFs 12 nucleotides and longer
    :param s: a DNA string
    :return: a list of ORFs
    """
    from re import finditer

    l = []
    s = s.upper()
    for i in finditer("ATG", s):
        count = 0
        for a in range(i.start(), len(s), 3):
            count +=1
            if s[a:a + 3] == "TAG" or s[a:a + 3] == "TGA" or s[a:a + 3] == "TAA":
                if count > 3:
                    l.append(s[i.start(): a + 3])
                break

    # Searching in compliment string
    s = s[::-1]
    s = s.translate(s.maketrans("ATGC", "TACG"))
    for i in finditer("ATG", s):
        count = 0
        for a in range(i.start(), len(s), 3):
            count +=1
            if s[a:a + 3] == "TAG" or s[a:a + 3] == "TGA" or s[a:a + 3] == "TAA":
                if count > 3:
                    l.append(s[i.start(): a + 3])
                break
    return l



print(gene_search("ATGATGATGAAAAAtTAaGATGTAATAATAATAACTATTTTaTCATCATCAT"))
print(gene_search("ATGATGATGAAAAAtTAaGATGTAATAATAATAACTATTTTaTCATCATCAT"))

l = [10, 9, 8, 7, 6, 5]
print(bubble_sort(l))
