n=int(input())
arr=list(map(int,input().strip().split()))
k=[]
sum=0
for i in range(n):
    if arr[i]%2==0:
        if arr[i] not in k:
            k.append(arr[i])
for i in range(len(k)):
    sum=sum+k[i]
print(sum)    