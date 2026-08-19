print("Exercício dict - Histórico de Serviços do Cliente (Acúmulo de Dados)")
cadastro={
    "nome":"Pablo",
    "telefone":"31 973000059",
    "historico_serviços":[]
}
print(cadastro)
while True:
    servico=input("Digite os serviços realizados: (fim para encerrar) ")
    if servico=="fim":
        break
    cadastro["historico_serviços"].append(servico)
print(f"Cliente: {cadastro}")
