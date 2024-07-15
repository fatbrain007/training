def first_non_repeated_char(str):
    
    char_count = {}
    for char in str:
        char_count[char] = char_count.get(char, 0) + 1    
   
    for char in str:
        if char_count[char] == 1:
            return char
    return None


str1 = "lloWorld"
print(first_non_repeated_char(str1)) 
