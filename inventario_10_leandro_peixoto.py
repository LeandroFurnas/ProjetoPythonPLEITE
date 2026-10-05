#Aqui e pra criar os tuples da sala, estados e uma lista cos tipos
SALAS = ("LAB1","LAB2","LAB3")
ESTADOS = ("operacional", "avariado", "em reparação")
tipos = ['computador', 'monitor', 'impressora', 'router', 'switch',
         'projetor','quadro']
#aqui o iventario com os eletronicos todos que se tem no local
inventario = {
    'PC01': {
        'nome': 'desktop lenovo',
        'tipo': 'computador',
        'sala': 'LAB1',
        'quantidade': 12,
        'estado': 'operacional',
    },
    'MN01': {
        'nome': 'monitor HP 24',
        'tipo': 'monitor',
        'sala': 'LAB1',
        'quantidade': 12,
        'estado': 'operacional',
    },
    'SW01': {
        'nome': 'switch cisco 12 portas',
        'tipo': 'switch',
        'sala': 'LAB2',
        'quantidade': 2,
        'estado': 'avariado',
    },
    'IMP01': {
        'nome': 'impressora 3D',
        'tipo': 'impressora',
        'sala': 'LAB3',
        'quantidade': 1,
        'estado': 'avariado',
    },
    'RT01': {
        'nome': 'router NOS',
        'tipo': 'router',
        'sala': 'LAB2',
        'quantidade': 3,
        'estado': 'operacional',
    },
    'PJ01': {
        'nome': 'projetor LED',
        'tipo': 'projetor',
        'sala': 'LAB3',
        'quantidade': 2,
        'estado': 'operacional',
    },
    'QD01': {
        'nome': 'Quadro Digital',
        'tipo': 'quadro',
        'sala': 'LAB1',
        'quantidade': 3,
        'estado': 'operacional',
    },
    'QD02': {
        'nome': 'Quadro Digital',
        'tipo': 'quadro',
        'sala': 'LAB2',
        'quantidade': 3,
        'estado': 'avariado',
    },
    'QD03': {
        'nome': 'Quadro Digital',
        'tipo': 'quadro',
        'sala': 'LAB3',
        'quantidade': 3,
        'estado': 'operacional',
    },
}
#aqui e um ciclo no dicionario para saber quais os itens avariados usando primeiro o for para pegar todos os valores e um if para comparação
lista_reparação = []
for reparavel in inventario:
    if inventario[reparavel]['estado'] == "avariado":
        lista_reparação.append(reparavel)
#aqui e so as listas vazias para guardar o que tem por vir
reparados = []
historico = []
#menu coms os += para mostrar o menu
menu = '\n-------------- MENU DE INVENTÁRIO --------------\n'
menu += '| 1 - Mostrar equipamentos                      |\n'
menu += '| 2 - Adicionar mais equipamento                |\n'
menu += '| 3 - Pesquisar nos equipamentos existentes     |\n'
menu += '| 4 - Alterar o estado de um equipamento        |\n'
menu += '| 5 - Remover um equipamento                    |\n'
menu += '| 6 - Lista de reparação                        |\n'
menu += '| 7 - Estatísticas                              |\n'
menu += '| 8 - Histórico de operações                    |\n'
menu += '| 0 - Sair                                      |\n'
menu += '----------------------------------------------'
#a flag que aprendi a poucas aulas mas da jeito
flag_ativo = True

while flag_ativo:
    print(menu)
    escolha_menu = int(input("Escolhe uma opção de 0 a 8: \n"))
    if escolha_menu < 0 or escolha_menu > 8:
        print("Isso não existe tenta denovo!")    
        continue
    if escolha_menu == 0:
        op = input("Queres sair do programa (y/n)?")
        if op == 'y':
            break
        else:
            continue
    if escolha_menu == 1:
        if not inventario:
            print('O inventário está vazio.')
        else:
            print('CÓDIGO | NOME | SALA | QUANTIDADE | ESTADO')
            for codigo in sorted(inventario):
                item = inventario[codigo]
                print(codigo, "|", item['nome'], "|", item['sala'], "|", item['quantidade'], "unidades |", item['estado'])
            print("Total de registos:", len(inventario))
    elif escolha_menu == 2:
        codigo = input("Código do equipamento: ").strip().upper()
        if codigo == '':
            print("O código não pode estar vazio.")
            continue
        if codigo in inventario:
            print("Esse código já existe.")
            continue
    
        nome = input("Qual o nomo do produto? ").strip()
        while nome == '':
            print("Tens de dizer algum nome de algum produto!")
            nome = input("Qual o nome do seu produto novamente?").strip()
        
        tipo = input(f"Tipos existentes neste momento: {tipos}").strip().lower()
        while tipo not in tipos:
            print("Dame algum tipo valido! ")
            tipo = input(f"Tipos existentes neste momento: {tipos}").strip().lower()

        sala = input(f"Qual e sala que tu queres: {SALAS}").strip().upper()
        while sala not in SALAS:
            print("Essa sala nao existe escolhe uma valida! ")
            sala = input(f"Salas existentes: {SALAS}").strip().upper()

        quantidade = int(input("Quantos tu queres adicionar?"))
        while quantidade <= 0:
            print("Escolhe um numero valido")
            quantidade = int(input("Quantos tu queres adicionar?"))

        inventario[codigo] = {
            'nome': nome,
            'tipo': tipo,
            'sala': sala,
            'quantidade': quantidade,
            'estado': 'operacional'
        }
        historico.append(f"Adicionaste corretamente o Codigo : {codigo}: ({tipo.strip().upper().title()})")
        print("Parabéns adicionaste o material com sucesso! ")

    elif escolha_menu == 3:
        for codigo in sorted(inventario):
            item = inventario[codigo]
            print(codigo, "|", item['nome'])
            
        pesquisa = input("Insere um codigo de algum produto valido:").strip().upper()
        equipamento = inventario.get(pesquisa)
        
        if equipamento:
            print(f"Informação do {pesquisa}")
            for chave, valor in equipamento.items():
                print(f"\n{chave.title().strip()}")
                print(str(valor).title())        
        else:
            print("Esse codigo nao e valido tenta denovo! ")

    elif escolha_menu == 4:
        for codigo in sorted(inventario):
            item = inventario[codigo]
            print(codigo, "|", item['nome'], item['estado'])
        
        codigo_input = str(input("Qual o codigo que queres alterar?")).strip().upper()
        
        if codigo_input in inventario:
            estado_nestemomento = inventario[codigo_input]['estado']
            print(f"Estado atual: {estado_nestemomento}")
            print(f"Todos os estados possiveis: {ESTADOS}")
            
            new_inp = str(input("Qual o novo estado que tu queres? ")).strip().lower()
            while new_inp not in ESTADOS:
                print("Não corresponde a nenhum valor existente nos estados")
                new_inp = str(input("Qual o novo estado que tu queres? ")).strip().lower()

            if new_inp == estado_nestemomento:
                print("O teu material ja tem o mesmo estado que colocaste")
            else:
                inventario[codigo_input]['estado'] = new_inp

                if new_inp == 'avariado':
                    if codigo_input not in lista_reparação:
                        lista_reparação.append(codigo_input)
                elif codigo_input in lista_reparação:
                    lista_reparação.remove(codigo_input)

                historico.append(f"Estado de {codigo_input}: {estado_nestemomento} -> {new_inp}")
                print("Alterou o estado corretamente! ")
        else:
                print("Esse codigo não existe no inventario")
    elif escolha_menu == 5:
        for codigo in sorted(inventario):
                    item = inventario[codigo]
                    print(codigo, "|", item['nome'], item['estado'])
        
        new_inp2 = input("Qual o codigo do equipamento que queres remover?").strip().upper()
        while new_inp2 in inventario:
            codigo_escolhido = inventario[new_inp2]['nome']
            print(f"O produto que escolheste e o: {codigo_escolhido}")
            deci2 = input("Tens a certeza que queres prosseguir?").strip().lower()
            if deci2 == 's':
                del inventario[new_inp2]
                while new_inp2 in lista_reparação:
                    lista_reparação.remove(new_inp2)
                    print(f"{new_inp2.upper()} foi eliminado da lista de reparaçao com sucesso!")
                historico.append(f"removeste :{new_inp2} / {codigo_escolhido}")
                print(f"{new_inp2.upper()} foi eliminado do iventario com sucesso!")
                
            elif deci2 == 'n':
                break
            else:
                print("Isso nao e uma opçao valida pedida")
    elif escolha_menu == 6:
        if not lista_reparação:
            print("A lista esta toda vazia")
        else:
            contadorNum = 1
            for reparaçao in (lista_reparação):
                codigo_escolhido2 = inventario[reparaçao]['nome']
                print(f"{contadorNum}. Nome: {reparaçao} - {codigo_escolhido2}")
                contadorNum +=1
            deci3 = input("Queres processar todas as reparações? ").strip().lower()
            if deci3 == 's':
                while lista_reparação:
                    historico.append(lista_reparação[0])
                    inventario[lista_reparação[0]]['estado'] = 'operacional'
                    reparados.append(lista_reparação[0])
                    itemRemovido = lista_reparação.pop(0)
                    print(f"O {itemRemovido} vai ser reparado e ele vai ser removido da lista de raparação!")
                print(f"Equipamentos reparados nesta sessão: {reparados}")
    elif escolha_menu == 7:
        
