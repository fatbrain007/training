import re

def countVowels(str):
   
    vowels_pattern = r'[aeiouAEIOU]'
    vowels = re.findall(vowels_pattern, str)
    vowel_count = len(vowels)    
    
    return vowel_count

str1 = "HelloWorld!"
vowels = countVowels(str1)
print(f"Vowels: {vowels}")