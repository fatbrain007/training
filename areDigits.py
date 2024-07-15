import re

str1 = "6666666668888"
if re.match(r'^\d+$', str1):
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")

