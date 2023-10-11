# Skriv en funktion, der tager en liste af tal som input 
# og returnerer en ny liste uden dubletter. Optimer koden 
# for hastighed og effektivitet.

input_list = [1, 2, 2, 3, 4, 4, 5]

def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Test af funktionen

resultat = remove_duplicates(input_list)
print(resultat)