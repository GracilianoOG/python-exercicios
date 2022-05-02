def palindromo(string):
    string_reversed = string[::-1]
    return string == string_reversed

eh_palindromo = palindromo("aka")

print("É palíndromo") if eh_palindromo else print("Não é palíndromo")