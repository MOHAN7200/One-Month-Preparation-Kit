#Pangrams


def pangrams(s):
    l=[]
    s=s.upper()
    for i in s:
        if(i!=' '):
            l.append(i)
    s=set(l)
    if(len(s)==26):
        return 'pangram'
    return 'not pangram'