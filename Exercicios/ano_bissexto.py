ano = int(input("Digita o ano: "))
mensagem = ""

if ano < 1582:
    mensagem = "Não está no calendário Gregoriano"
elif ano % 4 != 0:
    mensagem = "Ano comum"
elif ano % 100 != 0:
    mensagem = "Ano bissexto"
elif ano % 400 != 0:
    mensagem = "Ano comum"
else:
    mensagem = "Ano bissexto"

print(mensagem)
