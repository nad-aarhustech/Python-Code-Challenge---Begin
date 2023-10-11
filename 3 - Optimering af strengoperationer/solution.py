def remove_spaces(input_string):
    return ''.join(input_string.split())

# Test af funktionen
input_string = "Dette er en teststreng uden mellemrum"
resultat = remove_spaces(input_string)
print(resultat)