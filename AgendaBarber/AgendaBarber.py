print("""====================   BARBER PLANNER V.0.0.1 / Seja bem vindo!!!   ====================""")
dia=""
horario=""
servico= {
      "BARBA":25,
      "CABELO": 45,
      "COMBO": 60
}
nota=""
cliente=[]
lista_clientes=[]
lista_barbeiro=[]
lista_cupom=[]
lista_dias=[]
historico_servicos=[]
lista_notas=[]
lista_cancelados=[]
caixa_diario=[]
lista_agendamentos=[]
horarios_disponiveis={
    "TERÇA-FEIRA": ["08:00", "09:00", "10:00", "11:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"],
    "QUARTA-FEIRA": ["08:00", "09:00", "10:00", "11:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"],
    "QUINTA-FEIRA": ["08:00", "09:00", "10:00", "11:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"],
    "SEXTA-FEIRA": ["08:00", "09:00", "10:00", "11:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"],
    "SÁBADO": ["08:00", "09:00", "10:00", "11:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"],
}

while True:
      opcao=int(input("""
[1] AGENDAR 
[2] CONSULTAR
[3] PAGAMENTO
[4] SAIR
[5] CANCELAMENTO
                      
Escolha entre as opções do menu: """))
      # AGENDAMENTO
      if opcao==1:
            print("Perfeito, vou te ajudar! Mas antes preciso de algumas informações: ")
            cliente=input("Insira seu nome: ").strip().upper()
            dia=input("Dia de interesse: ").strip().upper()

            if dia not in horarios_disponiveis:
                  print("Dia indisponivel ou barbearia estara fechada neste dia! Tente novamente jogador!" )
                  continue

            horario=(input(f""" Horarios disponiveis:
            {horarios_disponiveis[dia]} 
            escolha entre os horarios acima (Exemplo: 08:00): """))
            if horario not in horarios_disponiveis:
                  print(f"Horario {horario} esta indisponivel para {dia}, tente outro! ")
                  continue
            
            horarios_disponiveis[dia].remove[horario]
            barbeiro=input("Gostaria de marcar com qual barbeiro? ").strip().upper()
            servico=input(f"""
BARBA: 25 R$
CABELO: 45 R$
COMBO: 60 R$
                                                
Qual sera o serviço: """).strip().upper()
            historico_servicos.append(servico)        
            if servico=="BARBA":
                  print(f"Marcado com Barbeiro {barbeiro}, as {horario}h de {dia}! {servico} !")
            elif servico=="CABELO":
                  print(f"Marcado com Barbeiro {barbeiro}, as {horario}h de {dia}! {servico} !")
            elif servico=="COMBO":
                  print(f"Marcado com Barbeiro {barbeiro}, as {horario}h de {dia}! {servico}!")
            else:
                  print("Erro! Escolha novamente!")
            lista_clientes.append(cliente)
            
            agendamento={
                        "CLIENTE": cliente,
                        "DIA": dia,
                        "HORARIO": horario,
                        "BARBEIRO": barbeiro,
                        "SERVIÇO": servico
                        }
            lista_agendamentos.append(agendamento)
            
            lista_barbeiro.append(barbeiro)
            lista_dias.append(dia)
            
            # CONSULTAS
      elif opcao==2:
            print(f""" CONSULTA COMPLETA
Agendamentos: {lista_agendamentos}
{lista_barbeiro} estão escalados
{lista_dias} dias com clientes agendados
Serviços escolhidos: {historico_servicos}
Clientes que cancelaram agendamento: {lista_cancelados}
Faturamento do dia: R$ {sum(caixa_diario)} reais""")
            if horario==12:
                  print(f"{cliente} Seu agendamento atual: {dia} / Horario: {horario}h. Lembre-se de consultar disponibilidade!")
            else:
                  print(f"{cliente} Seu agendamento atual: {dia} / Horario: {horario}h.")
      elif opcao==3:
            valor_servicos=int(input("Valor total do seus serviços: "))
            cupom=str(input("Digite seu CUPOM de desconto: ")).strip().upper()
            if cupom=="CUPOM10":
                  desconto=valor_servicos * 0.10
                  valor_final=valor_servicos-desconto
                  caixa_diario.append(valor_final)
                  print(f"Seu CUPOM foi aplicado com sucesso! 10% off / Valor atualizado: {valor_final} reais")
            else:
                  print(f"Nenhum cupom valido, prossiga com pagamento de {valor_servicos} reais")
                  lista_cupom.append(cupom)
                  caixa_diario.append(valor_servicos)
            print(f"Cupons não cadastrados: {lista_cupom} ")
      elif opcao==4:
            nota=int(input("Qual nota de 0 a 10 voce avalia o sistema? "))
            lista_notas.append(nota)
            print(f"Fechando sistema, volte sempre!")
            break
      elif opcao==5:
            print(f"Clientes ativos: {lista_clientes}")
            print(lista_agendamentos)
            nome_cancelado=input("Nome do cliente que deseja cancelar agendamento: ").strip().upper()
            if nome_cancelado in lista_clientes:
                  lista_clientes.remove(nome_cancelado)
                  lista_cancelados.append(nome_cancelado)
                  horario_cancelado=input("Horario a ser liberado. Exemplo 08:00: ")
                  horarios_disponiveis.append(horario_cancelado)
                  if agendamento in lista_agendamentos:
                        if nome_cancelado in agendamento:
                              lista_agendamentos.remove(agendamento)
                              print(f"Agendamento de {nome_cancelado} foi cancelado")
            else:
                  print("Este cliente nao tem agendamento ativo")
            
      else:
            print(f"Não entendi, tente novamente.")