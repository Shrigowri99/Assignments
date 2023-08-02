len_array=int(input())

min=999
max=0
smax=0
smin=0
for i in range(len_array):
    value=int(input())
    if max<value:
        smax=max
        max=value
    if min>value:
        smin=min
        min=value
        
        
print(smin)
print(smax)
