import re
import seaborn as sns
import matplotlib.pyplot as plt


with open('/home/anna/ib/python/text2430', 'r') as txt:
    # numbers from the story
    pat = re.compile(r'(\b[\d/]+\.[\d/]+\b).\s|[\s\n]([\d/]+)([\n\s]|\.\s)')  # Its a problem to get numbers at the end of a sentence.
    nums = pat.finditer(txt.read())
    l = [i.group(2) for i in nums]
    l2 = [i.group(1) for i in nums]
    print(l, l2)
    txt.seek(0)

    # words with a
    pat = re.compile(r'\w*[Aa]\w*')
    awords = pat.findall(txt.read())
    print(awords)
    txt.seek(0)

    # exclamations
    pat = re.compile(r'(?=([\.\"\!\?]([\w\s,:;]*\!)))')
    exclams = pat.finditer(txt.read())
    l = [i.group(2) for i in exclams]
    print(l)
    txt.seek(0)

    # Word lengths
    pat = re.compile(r'[a-z]+')
    words = pat.findall(txt.read().lower(), re.I)
    words = set(words)
    lenw = list(map(len, words))
    sns.distplot(lenw, bins=15, kde=False)
    plt.show()

# ftps
with open('/home/anna/ib/python/references.txt', 'r') as txt:
    with open('/home/anna/ib/python/ftps.txt', 'w') as outp:
        ftps = re.findall(r'ftp\.[\w\./#]*', txt.read())
        outp.write("\n".join(ftps))

# pattern for email searching
emailpattern = re.compile(r'\w*@[\w\.]*')