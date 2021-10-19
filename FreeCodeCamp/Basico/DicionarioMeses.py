dicionario_meses = {
    "Jan": "Janeiro",
    "Fev": "Fevereiro",
    "Mar": "Março",
    "Abr": "Abril",
    "Mai": "Maio",
    "Jun": "Junho",
    "Ago": "Agosto",
    "Set": "Setembro",
    "Out": "Outubro",
    "Nov": "Novembro",
    "Dez": "Dezembro"
}

print(dicionario_meses)
print(dicionario_meses["Jan"])
print(dicionario_meses.get("Jan"))
print(dicionario_meses.get("Jan", "Valor inválido!"))

print(dicionario_meses.get("Xis", "Valor inválido!"))
