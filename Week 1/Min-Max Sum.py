#Min-Max Sum

def miniMaxSum(arr):
    arr.sort()
    sum=0
    sum1=0
    for i in range(len(arr)-1):
        sum+=arr[i]
    for i in range(1,len(arr)):
        sum1+=arr[i]
    print(sum,sum1)