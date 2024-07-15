#3. How do you check if two strings are anagrams of each other?
def areAnagrams(str1, str2):
    return sorted(str1) == sorted(str2)


str1 = "helloworld"
str2 = "wholleldor"
print(areAnagrams(str1, str2))