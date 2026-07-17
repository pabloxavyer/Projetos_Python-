print("""====================
   BARBER PLANNER V.0.0.1 / Seja bem vindo!!!
====================""")
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

while True:
      opcao=int(input("""
[1] AGENDAR 
[2] CONSULTAR
[3] PAGAMENTO
[4] SAIR
[5] CANCELAMENTO
                      
Escolha entre as opções do menu: """))
      
      if opcao==1:
            print("Perfeito, vou te ajudar!")
            cliente=input("Insira seu nome: ")
            dia=input("Dia de interesse: ")
            horario=int(input("Horario de interesse: "))         
            barbeiro=input("Gostaria de marcar com qual barbeiro? ")
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
            lista_clientes.append(f"Cliente: {cliente}  Dia: {dia}  Horário: {horario} Barbeiro: {barbeiro}")
            lista_barbeiro.append(barbeiro)
            lista_dias.append(dia)
      elif opcao==2:
            print(f""" CONSULTA COMPLETA
Agendamentos: {lista_clientes}
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
            caixa_diario.append(valor_servicos)
            cupom=str(input("Digite seu CUPOM de desconto: "))
            if cupom=="CUPOM10" or cupom=="cupom10" or cupom=="Cupom10":
                  print(f"Seu CUPOM foi aplicado com sucesso! 10% off / Valor atualizado: {valor_final} reais")
                  desconto=valor_servicos * 0.10
                  valor_final=valor_servicos-desconto
                  caixa_diario.append(valor_final)
            else:
                  print(f"Nenhum cupom valido, prossiga com pagamento de {valor_servicos} reais")
                  lista_cupom.append(cupom)
            print(f"Cupons não cadastrados: {lista_cupom} ")
      elif opcao==4:
            nota=int(input("Qual nota de 0 a 10 voce avalia o sistema? "))
            lista_notas.append(nota)
            print(f"Fechando sistema, volte sempre!")
            break
      elif opcao==5:
            nome_cancelado=input("Nome do cliente que deseja cancelar agendamento: ")
            lista_cancelados.append(nome_cancelado)
            print(f"Agendamento de {nome_cancelado} foi cancelado")
      else:
            print(f"Não entendi, tente novamente.")