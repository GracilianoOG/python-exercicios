notas = [0, 0]
media = 0.0
situacao = ""
controle = 0

while controle != 2:
    notas[controle] = float(input(f"Informe a nota {controle + 1}° do aluno: "))
    if notas[controle] >= 0.0 and notas[controle] <= 10.0:
        print("Nota adicionada com sucesso!")
        controle += 1
    else:
        print("Nota inválida, informe apenas valores entre 0 e 10!")

media = (notas[0] + notas[1]) / 2

if media == 10.0:
    situacao = "Aprovado com distinção"
elif media >= 7.0:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print("\nPrimeira nota.: %2.2f" % notas[0])
print("Segunda nota..: %2.2f" % notas[1])
print("Média do aluno: %2.2f" % media)
print("Situação......:", situacao, "\n")
