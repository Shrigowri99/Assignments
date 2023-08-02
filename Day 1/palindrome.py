number=int(input())
num=number
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=int(num/10)
if rev==number:
    print("palindrome")
else:
    print("not palindrome")
    