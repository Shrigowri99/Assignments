string=input()
count_star=0
count_hash=0
for i in string:
    if i=='*':
        count_star+=1
    elif i=='#':
        count_hash+=1
if count_hash==count_star:
    print("0")
elif count_hash>count_star:
    print("negative integer")
else:
    print("postive integer")
    