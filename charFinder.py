#9. how do you count the occurrence of a given character in a string?
def charFinder(str1, char1):
    return str1.count(char1)


str1 = "HelloWorld"
char1 = "o"
print(f"found {charFinder(str1, char1)} {char1}s in {str1}")