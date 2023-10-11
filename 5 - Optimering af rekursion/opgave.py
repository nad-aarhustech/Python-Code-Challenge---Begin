# Skriv en rekursiv funktion til at beregne det 
# n'te Fibonacci-tal. Optimer koden ved at bruge 
# memoization for at undgå gentagne beregninger.

# Fibonacci-tal er en sekvens af tal, hvor hvert tal er summen
# af de to foregående tal i sekvensen. Den mest almindelige 
# definition af Fibonacci-sekvensen begynder med 0 og 1 som de første to tal. 
# Her er de første få Fibonacci-tal i sekvensen:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# Så hvert tal i sekvensen er summen af de to foregående tal. 
# For eksempel er 2 = 1 + 1, 3 = 2 + 1, 5 = 3 + 2 osv.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(10))