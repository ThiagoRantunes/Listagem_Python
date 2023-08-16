import biblioteca

while(True):
    print("Adicionar = add")
    print("Verificar = ver")
    print("Alterar = alt")
    print("Remover = rem")
    op = input("Escolha sua opção: ")
    if(op == "add"):
       biblioteca.Adicionar()
    elif(op == "ver"):
        biblioteca.Verificar()
    elif(op == "alt"):
        biblioteca.Alterar()
    elif(op == "rem"):
        biblioteca.Remover()