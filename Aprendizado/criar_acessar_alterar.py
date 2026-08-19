print("exercicio - criar, acessar e alterar")
tabela_serviços = {
    "degrade": "45.00",
    "sombrancelha": "15.00",
    "barba": "25.00"
}
print(f"Valor do degrade é {tabela_serviços['degrade']}")
tabela_serviços["degrade"]="50.00"
print(f"Preços atualizados: {tabela_serviços}")
tabela_serviços["pintura"]= "100.00"
tabela_serviços["pezinho"] = "15.00"
print(f"Tabela atualizada: {tabela_serviços}")
tabela_serviços["barbeiros"]=input("Digite os nomes dos barbeiros: ").split(",")
print(f"Tabela atualizada")
for serviço, preço in tabela_serviços.items():
    print(f"Serviço: {serviço} / Preço: {preço}")
print(tabela_serviços.get("pé", "Serviço nao cadastrado ou sem valor"))