n,q=map(int,input().split())
d={}
for i in range(q):
    t,a,b=map(int,input().split())
    if(t==1):
        d[(a,b)]=1
    elif(t==2):
        d[(a,b)]=0
    elif((a,b) in d and (b,a) in d and d[(a,b)]==1 and d[(b,a)]==1):
        print('Yes')
    else:
        print('No')
