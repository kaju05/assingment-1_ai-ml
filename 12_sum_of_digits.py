num=int(input('enter number:'))
cnt=0
while num>0:
    cnt+=int(num%10)
    num=int(num/10)
print(cnt)