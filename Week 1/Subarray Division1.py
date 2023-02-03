#Subarray Division 1


def twoArrays(k, A, B):
    A.sort()
    B.sort()
    B.reverse()
    for i in range(len(A)):
        if(A[i]+B[i]<k):
            print(A[i]+B[i])
            return 'NO' 
    return 'YES'