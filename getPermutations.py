import itertools

def getPermutations(s):
  
    permutations = itertools.permutations(s)
    
   
    permutation_list = [''.join(p) for p in permutations]
    
    return permutation_list


str1 = "Hello"
permutation1 = getPermutations(str1)
print(permutation1)
