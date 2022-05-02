def acronimo(frase):
    acronimo = ""

    for letra in frase:
        if letra.isupper(): acronimo += letra

    return acronimo

resultado = acronimo(input("Informe uma frase para ser convertida: "))
print("Acrônimo:", resultado)