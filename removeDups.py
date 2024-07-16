#6. How to remove duplicates from agiven array in Java?(solution)
def removeDups(lists):
    return list(set(lists))


lists = [1, 2, 3, "a", 1, "b", 2, "a", 4, 5, 6, 7, 3, "c"]
print(removeDups(lists)) 