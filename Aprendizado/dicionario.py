print("""
LISTA DE BARBEIROS
EXERCICIO 1
""")

barbeiro=[
    {"nome": "Pablo", "especialidade": "Degradê", "esperiencia": 5},
    {"nome": "Juan", "especialidade": "Barba", "esperiencia": 3},
    {"nome": "Raul", "especialidade": "Sombracelha", "esperiencia": 1}
    ]
print(f"O barbeiro {barbeiro[2]['nome']} é especialista em {barbeiro[2]['especialidade']} há {barbeiro[2]['esperiencia']} anos.")
print(barbeiro)

print("""
Adionando mais informações
exercicio 2
""")
barbeiro[0]["especialidade"]="Corte e Barba"
barbeiro[0]["unidade"]="Centro"
barbeiro[2]["unidade"]="Serra"
for barbeiro in barbeiro:
    print(barbeiro)

print(""" 
ESTOQUE DE PRODUTOS
EXERCICIO 3 
""")
estoque=[]
produto={}

while True:
    print("Caso finalize a lista de produtos digite sair logo abaixo")
    prod=input("Nome produto: ").lower()
    if prod =="sair":
        break
    preço=float(input("Preço produto: "))
    produto={
        "item": prod,
        "preço": preço
    }
    estoque.append(produto)
print(estoque)
total_estoque = (sum(produto["preço"] for produto in estoque))
print(f"O valor total dos produtos no estoque é {total_estoque} reais")