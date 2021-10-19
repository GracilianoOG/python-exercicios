# Do módulo x, importe a classe y
from Pergunta import Pergunta

# Perguntas
perguntas_prompts = [
    "Que cor é a maçã?\n(a) Vermelha/Verde\n(b) Roxa\n(c) Laranja\n\n",
    "Que cor é a banana?\n(a) Rosa\n(b) Magenta\n(c) Amarela\n\n",
    "Que cor é o morango?\n(a) Amarela\n(b) Vermelha\n(c) Azul\n\n"
]

# Perguntas e suas respostas
perguntas_respostas = [
    Pergunta(perguntas_prompts[0], "a"),
    Pergunta(perguntas_prompts[1], "c"),
    Pergunta(perguntas_prompts[2], "b")
]


def perguntas_programa(perguntas):
    pontos = 0
    for pergunta in perguntas:
        resposta = input(pergunta.prompt)
        if resposta == pergunta.resposta:
            pontos += 1
    print("Você acertou " + str(pontos) + "/" + str(len(perguntas)) + "!")


perguntas_programa(perguntas_respostas)
