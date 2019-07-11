N=int(input())
K=list(map(int,input().split()))
for i in range(len(K)-1):
    if (K[i]>K[i+1]):
        print(i)
