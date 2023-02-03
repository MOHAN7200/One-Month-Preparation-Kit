#Plus Minus


def plusMinus(arr):
    count1=0
    count2=0
    count3=0
    n=len(arr)
    for i in arr:
        if(i>0):
            count1+=1
        elif(i<0):
            count2+=1
        else:
            count3+=1
    print(count1/n)
    print(count2/n)
    print(count3/n)
