sr=int(input())
er=int(input())
n=int(input())
c=0
for i in range(sr,er+1):
    for j in range(2,int(i/2)+1):
        if i%j==0:
            break
    else:
         c=c+1
         if c==n:
            print(i)
            break
