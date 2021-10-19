vogais = "aeiou"
letra = input("Insira uma letra: ")
letra_formatada = letra.lower()

if letra_formatada in vogais:
    print("A letra", letra, "é uma vogal!")
else:
    print("A letra", letra, "é uma consoante!")
