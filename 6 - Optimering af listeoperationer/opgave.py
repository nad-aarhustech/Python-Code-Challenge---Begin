# Skriv en funktion, der tager to lister som input og 
# returnerer en ny liste med de fælles elementer. Optimer 
# koden for hastighed og effektivitet.

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

def find_common_elements(list1, list2):
    common_elements = []
    for item in list1:
        if item in list2 and item not in common_elements:
            common_elements.append(item)
    return common_elements

# Test af funktionen

resultat = find_common_elements(list1, list2)
print(resultat)