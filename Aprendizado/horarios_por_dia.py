# ==========================================
# EXERCÍCIO: HORÁRIOS POR DIA
# ==========================================
print("Horarios por dia para marcação")
agenda_dias = {
    "TERÇA-FEIRA": ["08:00", "09:00", "10:00", "11:00"],
    "QUARTA-FEIRA": ["08:00", "09:00", "10:00", "11:00"]
}

while True:
    dia_interesse = input("Qual dia deseja marcar: (Ex: TERÇA-FEIRA) / SAIR para finalizar ").strip().upper()
    if dia_interesse == "SAIR":
        break
    if dia_interesse in agenda_dias:
        print(f"Agenda de {dia_interesse}: {agenda_dias[dia_interesse]}")
        horario_interesse = input(f"Qual horário deseja na(o) {dia_interesse}? ").strip()
        if horario_interesse in agenda_dias[dia_interesse]:
            agenda_dias[dia_interesse].remove(horario_interesse)
            print(f"Agendamento concluído! {horario_interesse} agendado na {dia_interesse} para você!")
            print(f"Horários restantes na {dia_interesse}: {agenda_dias[dia_interesse]}")
            print(f"{agenda_dias}")
            agendamento = (f"{dia_interesse} agendado as {horario_interesse}")
        else: 
            print("Horário indisponível!")
    if dia_interesse == "CANCELAR":
        print(agendamento)
        dia_cancelado = input("Qual dia tem agendamento que deseja cancelar? ").strip().upper()
        if dia_cancelado in agenda_dias:
            horario_cancelado = input(f"Qual horario deseja cancelar no {dia_cancelado}? ").strip().upper()
            if horario_cancelado not in agenda_dias[dia_cancelado]:
                agenda_dias[dia_cancelado].append(horario_cancelado)
                print(f"Cancelamento concluido / {horario_cancelado} agora disponivel em {dia_cancelado}!")
                print(f"Agenda atualizada {agenda_dias.sort()}")
        else:
            print("Não encontrado")
    if dia_interesse not in agenda_dias:
                print("Dia indisponível ou barbearia fechada!")