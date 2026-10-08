import random

print("ESCALA DE LANCHE")

pessoas = {
    "meninos": ["Pablo", "Iran", "Patrick", "Victor", "Wendel"],
    "meninas": ["Ruth", "Giulia"]
}
pessoas["meninos"].append("Daniel")
pessoas["meninas"].extend(["Kathleen", "Edilaine", "Irys"])
print (pessoas["meninos"])
print (pessoas["meninas"])


lanche = ["doce", "salgado", "salgado", "bebida"]
for todas_pessoas in lanche:
    print (todas_pessoas)

todas_pessoas = pessoas["meninas"] + pessoas["meninos"]
todas_pessoas.sort()

escala = {}
disponiveis = todas_pessoas.copy()
for pessoa in disponiveis:
    sorteado = random.choice(lanche)
    if sorteado in escala:
        escala[sorteado].append(pessoa)
    else:
        escala[sorteado] = [pessoa]
print (escala) 