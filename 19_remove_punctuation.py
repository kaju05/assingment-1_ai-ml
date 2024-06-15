punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
str=input("enter string:")
res=''.join(char for char in str if char not in punctuations)
print(res)