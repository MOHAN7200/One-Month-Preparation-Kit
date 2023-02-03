#Sparse Arrays


def matchingStrings(strings, queries):
    l=[]
    for i in queries:
        l.append(strings.count(i))
    return l