#7. How do you find duplicate characters in a given string?
def printDups(str):
    char_count = {}    
    
    for char in str:
        char_count[char] = char_count.get(char, 0) + 1
    
  
    for char, count in char_count.items():
        if count > 1:
            print(f"{char}: {count}")


str1 = "HelloWorld"
printDups(str1)