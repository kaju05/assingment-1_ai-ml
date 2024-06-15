str1=input("first string:")
str2=input("second string:")
sorted_str1 = sorted(str1)
sorted_str2 = sorted(str2)
for x,y in zip(sorted_str1, sorted_str2):
    if x!=y:
        print("not anagrams")
        break
print("anagrams")
