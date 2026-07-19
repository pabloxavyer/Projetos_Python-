print("""====================   BARBER PLANNER V.0.0.1 / Seja bem vindo!!!   ====================""")
dia=""
horario=""
servico=""
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

while True:
      opcao=int(input("""
[1] AGENDAR 
[2] CONSULTAR
[3] PAGAMENTO
[4] SAIR
[5] CANCELAMENTO
                      
Escolha entre as opções do menu: """))
      
      if opcao==1:
            print("Perfeito, vou te ajudar! Mas antes preciso de algumas informações: ")
            cliente=input("Insira seu nome: ").strip().upper()
            dia=input("Dia de interesse: ").strip().upper()
            horario=int(input("Horario de interesse: "))
            barbeiro=input("Gostaria de marcar com qual barbeiro? ").strip().upper()
            servico=int(input(f"""
[1] Barba
[2] Cabelo
[3] Combo
                                                
Qual sera o serviço: """)) 
            historico_servicos.append(servico)        
            if servico==1:
                  print(f"Marcado com Barbeiro {barbeiro}, as {horario}h de {dia}! serviço BARBA!")
            elif servico==2:
                  print(f"Marcado com Barbeiro {barbeiro}, as {horario}h de {dia}! serviço CABELO!")
            elif servico==3:
                  print(f"Marcado com Barbeiro {barbeiro}, as {horario}h de {dia}! o COMBO!")
            else:
                  print("Erro! Escolha novamente!")
            lista_clientes.append(cliente)
            
            agendamento=f"Cliente: {cliente}  Dia: {dia}  Horário: {horario} Barbeiro: {barbeiro}"
            lista_agendamentos.append(agendamento)
            
            lista_barbeiro.append(barbeiro)
            lista_dias.append(dia)
      elif opcao==2:
            print(f""" CONSULTA COMPLETA
Agendamentos: {lista_agendamentos}
{lista_barbeiro} estão escalados
{lista_dias} dias com clientes agendados
Numero dos serviços escolhidos: {historico_servicos}
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
            nome_cancelado=input("Nome do cliente que deseja cancelar agendamento: ").strip().upper()
            if nome_cancelado in lista_clientes:
                  lista_clientes.remove(nome_cancelado)
                  lista_cancelados.append(nome_cancelado)
                  print(f"Agendamento de {nome_cancelado} foi cancelado")
            else:
                  print("Este cliente nao tem agendamento ativo")
      else:
            print(f"Não entendi, tente novamente.")