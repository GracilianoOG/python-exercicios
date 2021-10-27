nota1 = 0.0
nota2 = 0.0
media = 0.0
situacao = ""

nota1 = float(input("Informe a primeira nota do aluno: "))
nota2 = float(input("Informe a segunda nota do aluno: "))

media = (nota1 + nota2) / 2

if media == 10.:
    situacao = "Aprovado com distinção"
elif media >= 7.:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print("\nPrimeira nota:", nota1)
print("Segunda nota:", nota2)
print("Média do aluno:", media)
print("Situação:", situacao, "\n")
