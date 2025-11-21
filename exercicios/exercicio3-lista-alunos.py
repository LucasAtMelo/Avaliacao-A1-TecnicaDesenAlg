alunos = [] #lista que os alunos serão guardados 

while True: # loop infinito 
    print('-' * 90)
    print("""
        1. Visualizar alunos
        2. Adicionar aluno
        3. Remover aluno
        4. Sair do Sistema  
    """) # inteface com as opções de operação 
    print('-' * 90) 

    escolha = int(input('Digite a operação desejada:  ')) # escolha de operção do usuário 

    if escolha == 1: #escolha de visualizar a lista 
        print('Visualizar a lista escolhido') #mensagem de escolha 
        if len(alunos) <= 0: # se a lista não tiver nenhum aluno 
            print('Alunos ainda não foram adicionados a lista') # aviso de nenhum aluno cadastrado
        else: # caso tenha alunos 
            for i, aluno in enumerate(alunos): # itera a lista com indice e item separados 
                print(f'{i+1} - {aluno}') # mostra indice(adicionado 1 para não começar do 0) e item separados 

    elif escolha == 2: # escolha de adiconar aluno 
        print('Adicionar um aluno escolhido') 
        aluno = input('Nome do aluno: ') # nome do aluno a ser adicionado 
        alunos.append(aluno) #adiciona o aluno como último a lista 
        print('Inserção concluída') # mensagem de sucesso 

    elif escolha == 3: # escolha de remover aluno 
        print('Remover um aluno escolhido')
        if alunos:
            for i, aluno in enumerate(alunos): # também itera também a lista mostrando índice + 1 e item 
                print(f'{i + 1} - {aluno}') 
            excluido = int(input('Número do aluno à ser excluido: ')) - 1 # escolha de exclusão do usuário -1 para adequar com os índices(antes somados com 1)
            print(f'Aluno(a) {alunos[excluido]} removido da lista') # confirmação do aluno excluido 
            alunos.pop(excluido) # aluno exlcuido
        else:
            print('Nenhum aluno cadastrado') 

    elif escolha == 4: #escolha de sair do sistema 
        print('Saindo do sistema! ')
        break # quebra do loop 

print('Até a próxima :)') # mensagem de despedida 
