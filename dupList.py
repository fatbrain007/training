#2. How do you print duplicate characters from a string? (solution)
def getDups(str):
    char_count = {} 
    dups =[]   
    
    for char in str:
        char_count[char] = char_count.get(char, 0) + 1
    
  
    for char, count in char_count.items():
        if count > 1:
            dups.append(char)
    
    return dups


str1 = "HelloWorld"
print(getDups(str1))