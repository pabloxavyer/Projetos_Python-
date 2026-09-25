import random

print("ESCALA DE LANCHE")

pessoas = {
    "meninos": ["Pablo", "Iran"],
    "meninas": ["Ruth", "Giulia"],
}

# 4 itens para bater com a quantidade das 4 pessoas do grupo
lanche = ["doce", "salgado", "salgado", "bebida"]

todas_pessoas = pessoas["meninas"] + pessoas["meninos"]
todas_pessoas.sort()

escala = {}
disponiveis = todas_pessoas.copy()