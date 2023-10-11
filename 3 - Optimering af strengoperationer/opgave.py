# Skriv en funktion, der tager en streng som input og 
# returnerer en ny streng med alle 
# mellemrum fjernet. Optimer koden for hastighed.

def remove_spaces(input_string):
    return input_string.replace(" ", "")

# Test af funktionen
input_string = "Dette er en teststreng uden mellemrum"
resultat = remove_spaces(input_string)
print(resultat)