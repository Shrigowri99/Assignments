len_array=int(input())

count=0
ref=0
for i in range(len_array):
    value=int(input())
    if ref<value:
        ref=value
        count+=1
    
print(count)
            