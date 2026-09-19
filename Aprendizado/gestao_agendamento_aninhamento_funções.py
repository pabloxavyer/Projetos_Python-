print("Exercicio Gestão de Agendamentos (Aninhamento + Funções)")
horario=0
agenda = {
    "09:00": {"cliente": "Pablo", "servico": "degrade", "valor": 50.0},
    "10:00": {"cliente": "Juan", "servico": "barba", "valor": 25.0},
}
print(agenda)
buscar_agendamento=(horario)
horario=input("Digite o horário do agendamento que deseja buscar: ")
if horario in agenda:
    print(f"{horario} esta reservado")
    print(f"{agenda[horario]}")
else:
    print("horario livre ou sem cadastro")
adicionar_agendamento=input("Deseja adicionar um agendamento? (s/n) ")
if "s" in adicionar_agendamento:
    cliente=input("Seu nome: ")
    horario=input("Seu horario: ")
    serviço=input("Seu corte: ")
    agenda[horario]={"cliente": cliente, "servico": serviço, "valor": 00.00}
    print(f"Agendamento sucessivel para {agenda[horario]["cliente"]}")
    print(f"Agenda atualizada: {agenda}")
    for chave, valor in agenda.items():
        print(f"{chave} - {valor}")