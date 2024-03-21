from collections import defaultdict
Ha,Wa=map(int,input().split())
A=[input() for i in range(Ha)]
Hb,Wb=map(int,input().split())
B=[input() for i in range(Hb)]
Hx,W=map(int,input().split())
X=[input() for i in range(Hx)]
 
H1=max(Hx,Ha,Hb)
W1=max(W,Wa,Wb)
ans=defaultdict(lambda:defaultdict(lambda:'.'))
for i in range(Hx):
  for j,x in enumerate(X[i]):
    ans[i+H1][j+W1]=X[i][j]
ans2='No'
 
for i in range(Hx+H1):
  for j in range(W+W1):
    for i2 in range(Hx+H1):
      for j2 in range(W+W1):
        check=True
        for x in range(max(i+Ha,i2+Hb,Hx+H1)):
          for y in range(max(j+Wa,j2+Wb,W+W1)):
            if ((0<=(x-i)<Ha) and (0<=(y-j)<Wa)) and ((0<=(x-i2)<Hb) and (0<=(y-j2)<Wb)):
              if (ans[x][y]=='#') and((B[x-i2][y-j2]=='#') or (A[x-i][y-j]=='#')):
                continue
              if (ans[x][y]=='.') and((B[x-i2][y-j2]=='.') and (A[x-i][y-j]=='.')):
                continue
            else:
              if ((0<=(x-i2)<Hb) and (0<=(y-j2)<Wb)):
                if (ans[x][y]==B[x-i2][y-j2]):
                  continue
              elif ((0<=(x-i)<Ha) and (0<=(y-j)<Wa)):
                if (ans[x][y]==A[x-i][y-j]):
                  continue
              else:
                continue
 
                
            check=False
            break
          if (check==False):
            break
        
        
        if check:
          ans2='Yes'
          print('Yes')
          exit()
 
print(ans2)