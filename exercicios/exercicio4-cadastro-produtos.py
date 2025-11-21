produtos = dict() # dicionário que vai guardar os itens 

while True: # loop infinito 
    print('-' * 90) 
    print("""
    1. Visualizar produtos
    2. Adicionar produtos
    3. Remover produtos
    4. Sair do sistema
    """) # interface de escolha usuário 
    print('-' * 90)
    
    escolha = int(input('Digite a operação desejada: ')) # escolha de operação do usuário 
    if escolha == 1: # escolha de visualizar os itens 
        print('Visualizar itens escolhido') 
        if len(produtos) <= 0: # se não houver itens no dicionário 
            print('Nenhum produto cadastrado!')
        else:
            for chave, valor in produtos.items(): # itera o dicionario com chaves e valores 
                print(f'Produto: {chave}: R${valor}')

    elif escolha == 2: # escolha de adicionar item 
        print('Adicionar item escolhido')
        nome_produto = input('Nome do produto: ') # nome do item do usuário 
        valor_produto = float(input('Digite o valor do produto: ')) # valor do item 
        produtos[nome_produto] = valor_produto #adiciona o item com o valor no dicionário 
    
    elif escolha == 3: # escolha de remoção 
        print('Remover item escolhido') 
        if len(produtos) > 0:
            nome_produto = input('Nome do produto: ') # nome do produto a ser removido 
            if nome_produto in produtos: # se o produto do usuário estiver cadastrado 
                print(f'Produto {nome_produto} de valor R${produtos[nome_produto]} removido!') # confirmação da remoção com valor 
                produtos.pop(nome_produto) # remoção do item 
            else: # se o produto não for cadastrado 
                print('Produto não encontrado')
        else:
            print('Nenhum produto cadastrado!')
    
    elif escolha == 4: # escolha de sair do sistema 
        print('Saindo do sistema!')
        break # quebra do loop 

print('Até a próxima :)') # mensagem de despedida 
