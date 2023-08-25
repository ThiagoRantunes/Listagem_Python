

lista = {"Thiago":True, "Murilo":False, "Luiz":True, "Vitor":True}

def Adicionar():
    while(True):
        adicionar = input("Digite um nome: ")
        if(adicionar in lista):
            print("Esse nome ja esta na lista!!")
        else:
            break
    verificar = input("Ele respondeu? Sim ou Não: ")
    if(verificar == "Sim"):
        lista[adicionar] = True
        for nomeLista in lista.items():
                print(nomeLista)
    elif(verificar == "Não"):
        lista[adicionar] = False
        for nomeLista in lista.items():
                print(nomeLista)


def Verificar():
    while(True):
        nome = input("Sair ou Quem você procura?: ")
        if(nome == "Sair"):
            break
        if(nome in lista):
            if(lista[nome] == True):
                print("O nome que você digitou ja respondeu, MUITO OBRIGADO!!")
                break
            elif(lista[nome] == False):
                print("O nome que você digitou ainda não respondeu!!")
                break
        else:
            print("O nome que você digitou não esta na lista")

def Alterar():
    for nomeLista in lista.items():
            print(nomeLista)
    alterar = input("Digite o nome de quem você quer alterar: ")
    if(alterar in lista):
        alterarVerificacao = input("Digite a nova verificação: Sim ou Não: ")
        if(alterarVerificacao == "Sim"):
            lista[alterar] = True
            for nomeLista in lista.items():
                print(nomeLista)
        elif(alterarVerificacao == "Não"):
            lista[alterar] = False
            for nomeLista in lista.items():
                print(nomeLista)
    else:
        print("O nome que você digitou não esta na lista")

def Remover():
    for nomeLista in lista.items():
        print(nomeLista)
    deletar = input("Digite quem você quer remover: ")
    if(deletar in lista):
        del lista[deletar]
        for nomeLista in lista.items():
            print(nomeLista)
    else:
        print("O nome que você digitou não esta no sistema!")
