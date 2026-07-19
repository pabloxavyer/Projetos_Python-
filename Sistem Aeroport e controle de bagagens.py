print("Sistema de aeroporto e controle de bagagens")
print("""menu
[1] RAIO X
[2] PAINEL DE VOOS
[3] SAIR""")
# adicionar while true depois

    nome_completo=(input("Digite seu nome completo: ")).strip().title()
    if nome_completo=="":
        print("Erro! Nome não pode ficar sem preencher.")
    else:
        print(f"Olá {nome_completo.upper()}")
    print("===raio x===".upper())
    itens=str(input("Me fale o que voce esta levando na bagagem: ")).lower()
    lista_itens=[]
    lista_itens.append(itens)
    lista_itens_proibidos=["tesoura", "arma", "bomba"]
    if "tesoura" in itens or "arma" in itens or "bomba" in itens:
        print("ALERTA")
    else:
        print("liberado")  
    print("===PAINEL DE VOOS===")
    lista_voos=["VIX123", "BHZ123", "SPX123"]
    voo=str(input("Qual codigo do seu voo?" )).upper()
    if voo in lista_voos:
        print("Voo proximo")
        lista_voos.remove(voo)
    else:
        print("verifique seu voo no atendimento")
    print(f"Voos que ainda nao voaram: {lista_voos}")
    sair=str(input("Deseja sair do sistema? [S/N]")).strip().upper()
    if sair==sim:
        break