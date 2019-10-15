from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""

    listA = list()
    listB = list()

    if not a or type(a) != str:
        return list()
    if not b or type(b) != str:
        return list()

    listA = a.split("\n")
    listB = b.split("\n")

    remaining = set(listA) & set(listB)

    return remaining


def sentences(a, b):
    """Return sentences in both a and b"""

    listA = list()
    listB = list()

    if not a or type(a) != str:
        return list()
    if not b or type(b) != str:
        return list()

    listA = sent_tokenize(a)
    listB = sent_tokenize(b)

    remaining = set(listA) & set(listB)

    return remaining


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    listA = list()
    listB = list()

    substringA = list()
    substringB = list()

    if not a or type(a) != str:
        return list()

    if not b or type(b) != str:
        return list()

    substringA = a.split()
    substringB = b.split()

    for word in substringA:
        sup_limit = len(word) - n
        for i in range(0, sup_limit + 1, 1):
            listA.append(word[i:i+n])
    for word in substringB:
        sup_limit = len(word) - n
        for i in range(0, sup_limit + 1, 1):
            listB.append(word[i:i+n])

    remaining = set(listA) & set(listB)
    return remaining
