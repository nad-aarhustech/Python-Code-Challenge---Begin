def common_elements(list1, list2):
    return list(set(list1) & set(list2))

# Test af funktionen
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
resultat = common_elements(list1, list2)
print(resultat)