import os

lista = []

while True:
    print("Selecione uma opcao")
    selecionar = input("i[nserir] [a]pagar [l]istar: ")
    
    if selecionar == 'i':
        os.system('cls')
        item = input('Informe o item que deseja adicionar:')
        if item.isalpha():
            lista.append(item)
        else:
            print('Escreva apenas itens do mercado ')
        
    elif selecionar == 'a':
        os.system('cls')
        if lista:
            lista_enumerada = list(enumerate(lista, start=1))
            for indice, nome in lista_enumerada:
                print(indice, nome)
        try:
            remover = input('Qual o índice do item que deseja remover:')
            lista.pop(int(remover) - 1)  # Remover o item correspondente ao índice
        except IndexError:
            print('Esse indice nao existe')

        else:
            print('item apagado')
    
    elif selecionar == 'l':
        os.system('cls')
        if lista:
            for item in lista:
                print(item)
        else:
            print('Nada para listar')
                

    # Poderia ter botado simplesmente else
    elif selecionar != 'i' and selecionar != 'a' and selecionar != 'l':
        print('Você deve digitar apenas: i[nserir] [a]pagar [l]istar')
        
    # Listar os itens e seus índices após cada operação
    lista_enumerada = list(enumerate(lista, start=1))
    for indice, nome in lista_enumerada:
        print(indice, nome)