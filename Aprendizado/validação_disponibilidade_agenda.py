print("Exercício 2: Validação de Disponibilidade de Horário (Checagem de Chave)")
agenda={
    "09:00":"",
    "10:00":"",
    "11:00":"Pablo",
}
print(agenda)


while True:
    nome=input("Qual seu nome? ")
    agendamento=input("Digite o horário que deseja agendar: (ex: 09:00) ")
    if agendamento not in agenda:
        print("Horario nao existe")
    elif agenda[agendamento] != "":
        print(f"A hora {agendamento} ja possui marcação")
    else:
        agenda[agendamento]=nome
        print(agenda)
        break
    
