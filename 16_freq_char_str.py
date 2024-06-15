str = 'kanika'
dic = {}
for x in range(ord('a'), ord('z') + 1):
    dic[chr(x)] = 0
    
for x in str:
    dic[x]+=1
for key in dic:
    print(f'{key}: {dic[key]}')