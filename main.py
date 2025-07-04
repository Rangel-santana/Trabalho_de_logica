lista_livro = []  # Início das varíaveis globais
id_global = 0  # Valor inícial da variável


# Fim das varíaveis globais

# Início de cadastrar_livro
def cadastrar_livro(id):
    print('-' * 50)
    print('-' * 10,'MENU CADASTRAR LIVRO', '-' * 18)
    print('1 - Cadastrar Livro')
    print('id: {}'.format(id_global))
    nome = input('Por favor entre com o nome do livro: ')
    autor = input('Por favor entre com o autor do livro: ')
    editora = input('Por favor entre com a editora do livro: ')
    dicionario_livro = {'id': id,
                        'nome': nome,
                        'autor': autor,
                        'editora': editora}


    lista_livro.append(dicionario_livro.copy())
    print('-' * 50)


# Início consultar_livro
def consultar_livro():
    print('-' * 50)
    while True:
        print('-' * 10, 'MENU CONSULTAR LIVRO', '-' * 18)
        opcao_consultar = input('Escolha a opção desejada:\n' +
                                '1 - Consultar todos os livros\n' +
                                '2 - Consultar livro por id\n' +
                                '3 - Consultar livro(s) por autor\n' +
                                '4 - Retornar ao menu\n' +
                                '>>').upper()
        if opcao_consultar == '1':
            print('-' * 16)
            for livro in lista_livro:  # livro vai varrer toda a lista de livros
                for key, value in livro.items():
                    print('{}: {}'.format(key, value))
                print('\n')
            print('-' * 50)

        elif opcao_consultar == '2':
            id_livro = int(input('Digite o id do livro: '))
            for livro in lista_livro:
                if livro['id'] == id_livro: # se o valor do campo id do dicionário é igual ao valor de id_livro
                    print('-' * 16)
                    for key, value in livro.items():
                        print('{}: {}'.format(key, value))
                print('-' * 50)
        elif opcao_consultar == '3':
            autor_livro = input('Digite o autor do livro: ')
            for livro in lista_livro:
                if livro['autor'] == autor_livro:
                    print('-' * 50)
                    for key, value in livro.items():
                        print('{}: {}'.format(key, value))
                print('-' * 50)
        elif opcao_consultar == '4':
            return  # sai da função consultar_livro
        else:
            print('Opção inválida. Tente novamente. ')
            continue


# Início remover_livro
def remover_livro():
    print('-' * 50)
    print('-' * 15, 'MENU REMOVER LIVRO', '-' * 15)
    opcao_remover = int(input('Digite o id do livro a ser removido: '))
    for livro in lista_livro:
        if livro[ 'id'] == opcao_remover:
            lista_livro.remove(livro)
            print('Livro removido com sucesso! ')
            print('-' * 50)

# Inicio da main
print('Bem vindo a Livraria do Luis Rangel Santana Ramos')
print('-' * 50)
while True:
    print('-' * 15, 'MENU PRINCIPAL', '-' * 19)
    opcao_principal = input('Escolha a opção desejada:\n' +
                            '1 - Cadastrar livro\n' +
                            '2 - Consultar livro(s)\n' +
                            '3 - Remover livro\n' +
                            '4 - Sair\n' +
                            '>>').upper()
    if opcao_principal == '1':
        id_global = id_global + 1
        cadastrar_livro(id_global)

    elif opcao_principal == '2':
        consultar_livro()
    elif opcao_principal == '3':
        remover_livro()
    elif opcao_principal == '4':
        break
    else:
        print('Opção inválida. Tente novamente. ')
        continue  # Retorna para o início do laço
