#8. How do you count a number of vowels and consonants in a given string
import re

def countVowels(str):
   
    vowels_pattern = r'[aeiouAEIOU]'
    consonants_pattern = r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]'

    vowels = re.findall(vowels_pattern, str)
    consonants = re.findall(consonants_pattern, str)

    vowel_count = len(vowels) 
    consonant_count = len(consonants)   
    
    return vowel_count, consonant_count

str1 = "HelloWorld!"
vowels, consonants = countVowels(str1)
print(f"Vowels: {vowels}, Consonants: {consonants}")