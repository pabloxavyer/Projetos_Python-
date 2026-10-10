print("ENTRADAS E SAIDAS - CONTROLE FINANCEIRO PESSOA")
entradas={
        "Ruth": [],
        "Pablo": []
          }
saidas={}
entradas["Ruth"].extend([5000, 3000])
entradas["Ruth"]=sum(entradas["Ruth"])
entradas["Pablo"].append(10000)
print(entradas)
print(saidas)
while True:
    coisa=input("Item a ser adicionado: ")
    valor=int(input("Valor do item: "))
    operador=input("Entrada ou saida: ")
    if operador== "Saida":
        if coisa not in entradas:
            saidas[coisa] = []
            saidas[coisa].append(valor)
    if operador=="Entrada":
        if coisa not in entradas:
            entradas[coisa] = []
            entradas[coisa].append(valor)
        else:
            entradas[coisa].append(valor)
    print(entradas)
    print(saidas)