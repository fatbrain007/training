def reverseString(s):    
    if len(s) <= 1:
        return s
    else:        
        return reverseString(s[1:]) + s[0]


str1 = "HelloWorld"
reversed_string = reverseString(str1)
print(reversed_string) 

