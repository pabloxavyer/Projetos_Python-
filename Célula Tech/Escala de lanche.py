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


lanche = ["doce", "salgado", "bebida", "doce", "salgado", "bebida", "doce", salgado", "bebida"]
print (len(lanche))
for item in lanche:
    print (item)

todas_pessoas = pessoas["meninas"] + pessoas["meninos"]
todas_pessoas.sort()
print (len(todas_pessoas))

escala = {}
disponiveis = todas_pessoas.copy()
