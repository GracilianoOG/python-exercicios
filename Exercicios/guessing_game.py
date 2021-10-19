# Jogo que tentei fazer sozinho após aprender bastante teoria do Python! Ainda poderá ser melhorado em futuras versões.

# Configuração do jogo
palavra = "Banana"
palavra = palavra.lower()

dica = "Dica: " + "É uma fruta que os macacos adoram!"
linha = "-" * 60

# Configuração do jogador
nome_jogador = ""
resposta = ""
max_tentativas = 6
num_tentativas = max_tentativas

# Jogo começa
print(
    """
    -----------------------
    - Jogo da advinhação  -
    -----------------------
    -   Tente a sorte!!!  -
    -----------------------
    """
    )

nome_jogador = input("Informe o seu nome, por favor: ")

print(dica)
print(nome_jogador + ", você possui (", num_tentativas, "/", max_tentativas, ") tentativas, cuidado ao errar!")
print(linha)

while (resposta != palavra) and (num_tentativas != 0):
    resposta = input("E a palavra é...: ").lower()

    if (resposta != palavra):
        num_tentativas -= 1
        if (num_tentativas > 0):
            print("Errou! Você ainda possui (", num_tentativas, "/", max_tentativas, ") tentativa(s)")
        else:
            print("Errou de novo, suas tentativas acabaram!")
            print(nome_jogador, "perdeu o jogo!")
    else:
        print(linha)
        print(nome_jogador, "venceu!")
        erros = max_tentativas - num_tentativas
        print("Erros cometidos:", erros)

        if erros > max_tentativas // 2:
            print("Pode fazer melhor na próxima vez!")

    print(linha)
