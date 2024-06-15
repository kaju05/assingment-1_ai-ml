str=input('Enter string:')
file = open('example.txt', 'w')
file.write(str)
file.close()