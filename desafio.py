inventario  = []
while True:
    print(33*'-')
    print('|1. Cadastrar item              |')
    print('|2. Alterar quantidade          |')
    print('|3. Listar produtos disponiveis |')
    print('|4. Valor do estoque            |')
    print('|5. Sair                        |')
    print(33*'-')
    opcao = input('Escolha uma opção: ')


    if opcao == '1':
        nome = input('Diogite o nome do produto: ')
        preco = float(input('Digite o preço do produto: '))
        quantidade = int(input('Digite a quantidade: '))
        
        produto = {'nome': nome, 'quantidade': quantidade, 'preco': preco}
        inventario.append(produto)
        print('|  Produto cadastrado com sucesso!  |')
    
    
    elif opcao == '2':
        nome = input('Qual o nome do produto: ')
        
        encontrado = False
        for produto in inventario:
            if produto ['nome'] == nome:
                nova_quantidade = int(input('Digite a nova quantidade: '))
                produto ['quantidade'] =  nova_quantidade
                print('|  Quantidade alterada com sucesso!  |')
                encontrado = True
                break
        if not encontrado:
            print(f'|  {nome} nao encontrado  |')
    
    
    elif opcao == '3':
        # Listar Produtos
        if len(inventario) == 0:
            print("Nenhum produto no inventário.")
        else:
            for produto in inventario:
                print(f"Nome: {produto['nome']} | Quantidade: {produto['quantidade']} | Preço: R${produto['preco']:.2f}")

    
    elif opcao == '4':
        valor_total = 0
        for produto in inventario:
            valor_total += produto['quantidade'] * produto['preco']
            print(f'O inventario esta avaliado em: R${valor_total:.2f}')
    elif opcao == '5':
        print('Saindo...')
        exit()
    else:
        print('|  Opção inválida, digite outra.  |')