l=[1,4,3,5,8,2]
s=set(l)
print(s)
n=int(input())
for i in l:
    key=n-i
    if key!=i:
        if key in l:
            print(key,i)
            l.remove(key)
            l.remove(i)