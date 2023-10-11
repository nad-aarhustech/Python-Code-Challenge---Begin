# Skriv en funktion, der tager en liste af tal som input 
# og returnerer en ny liste, der indeholder kun de positive 
# tal fra den oprindelige liste. Optimer koden for læsbarhed og effektivitet.

input_list = [1, -2, 3, -4, 5, -6]

def find_positive_numbers(input_list):
    positive_numbers = []
    for num in input_list:
        if num > 0:
            positive_numbers.append(num)
    return positive_numbers

# Test af funktionen
input_list = [1, -2, 3, -4, 5, -6]
resultat = find_positive_numbers(input_list)
print(resultat)