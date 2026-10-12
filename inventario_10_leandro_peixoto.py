# Trabalho - Programa para gerir material escolar de informática
# Criador - Leandro Peixoto
# Número - 10
# Data - 12/10/2026

# Aqui é pra criar os tuples da sala, estados e uma lista com os tipos
SALAS = ("LAB1", "LAB2", "LAB3")
ESTADOS = ("operacional", "avariado", "em reparação")
tipos = ['computador', 'monitor', 'impressora', 'router', 'switch',
         'projetor', 'quadro']

# Aqui o inventário com os eletrónicos todos que se tem no local
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

# Aqui é um ciclo no dicionário para saber quais os itens avariados
# usando primeiro o for para pegar todos os valores e um if para
# comparação
lista_reparação = []
for reparavel in inventario:
    if inventario[reparavel]['estado'] == "avariado":
        lista_reparação.append(reparavel)

# Aqui é só as listas vazias para guardar o que tem por vir
reparados = []
historico = []

# Menu com os += para mostrar o menu
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

# A flag que aprendi há poucas aulas, mas dá jeito
flag_ativo = True

while flag_ativo:
    print(menu)
    escolha_menu = int(input("Escolhe uma opção de 0 a 8: \n"))
    if escolha_menu < 0 or escolha_menu > 8:
        print("Isso não existe, tenta de novo!")
        continue
    if escolha_menu == 0:
        op = input("Queres sair do programa (y/n)?")
        if op == 'y':
            break
        else:
            continue
#aqui ele verifica se o inventario esta fazio, se tiver alguma coisa no inventario ele mostra O codigo,nome,etc...    
    if escolha_menu == 1:
        if not inventario:
            print('O inventário está vazio.')
        else:
            print('CÓDIGO | NOME | SALA | QUANTIDADE | ESTADO')
            for codigo in sorted(inventario):
                item = inventario[codigo]
                print(codigo, "|", item['nome'], "|", item['sala'], "|",
                      item['quantidade'], "unidades |", item['estado'])
            print("Total de registos:", len(inventario))
 #no 2 ele pede um input de um codigo e com esse codigo,nome,etc.. ele vai o enfiar no dicionario iventario os valores que forem inseridos nas variaveis
    elif escolha_menu == 2:
        codigo = input("Código do equipamento: ").strip().upper()
        if codigo == '':
            print("O código não pode estar vazio.")
            continue
        if codigo in inventario:
            print("Esse código já existe.")
            continue

        nome = input("Qual o nome do produto? ").strip()
        while nome == '':
            print("Tens de dizer algum nome de algum produto!")
            nome = input("Qual o nome do seu produto novamente?").strip()

        tipo = input(
            f"Tipos existentes neste momento: {tipos}").strip().lower()
        while tipo not in tipos:
            print("Dá-me algum tipo válido! ")
            tipo = input(
                f"Tipos existentes neste momento: {tipos}").strip().lower()

        sala = input(f"Qual é a sala que tu queres: {SALAS}").strip().upper()
        while sala not in SALAS:
            print("Essa sala não existe, escolhe uma válida! ")
            sala = input(f"Salas existentes: {SALAS}").strip().upper()

        quantidade = int(input("Quantos tu queres adicionar?"))
        while quantidade <= 0:
            print("Escolhe um número válido")
            quantidade = int(input("Quantos tu queres adicionar?"))
#aqui e feito o registro de tudo 
        inventario[codigo] = {
            'nome': nome,
            'tipo': tipo,
            'sala': sala,
            'quantidade': quantidade,
            'estado': 'operacional'
        }
        historico.append(f"Adicionaste corretamente o Código: {codigo}: "
                         f"({tipo.strip().upper().title()})")
        print("Parabéns, adicionaste o material com sucesso! ")
#no 3 e a procura que pede um codigo e verifica se e valido no inventario
    elif escolha_menu == 3:
        for codigo in sorted(inventario):
            item = inventario[codigo]
            print(codigo, "|", item['nome'])

        pesquisa = input(
            "Insere um código de algum produto válido:").strip().upper()
        equipamento = inventario.get(pesquisa)

        if equipamento:
            print(f"Informação do {pesquisa}")
            for chave, valor in equipamento.items():
                print(f"\n{chave.title().strip()}")
                print(str(valor).title())
        else:
            print("Esse código não é válido, tenta de novo! ")
#pede um codigo depois procura o codigo no inventario mostra o estado do codigo depois pede para qual alterar de acordo com a lista ESTADOS
    elif escolha_menu == 4:
        for codigo in sorted(inventario):
            item = inventario[codigo]
            print(codigo, "|", item['nome'], item['estado'])

        codigo_input = str(input(
            "Qual o código que queres alterar?")).strip().upper()

        if codigo_input in inventario:
            estado_nestemomento = inventario[codigo_input]['estado']
            print(f"Estado atual: {estado_nestemomento}")
            print(f"Todos os estados possíveis: {ESTADOS}")

            new_inp = str(input(
                "Qual o novo estado que tu queres? ")).strip().lower()
            while new_inp not in ESTADOS:
                print("Não corresponde a nenhum valor existente nos estados")
                new_inp = str(input(
                    "Qual o novo estado que tu queres? ")).strip().lower()

            if new_inp == estado_nestemomento:
                print("O teu material já tem o mesmo estado que colocaste")
            else:
                inventario[codigo_input]['estado'] = new_inp

                if new_inp == 'avariado':
                    if codigo_input not in lista_reparação:
                        lista_reparação.append(codigo_input)
                elif codigo_input in lista_reparação:
                    lista_reparação.remove(codigo_input)

                historico.append(f"Estado de {codigo_input}: "
                                 f"{estado_nestemomento} -> {new_inp}")
                print("Alterou o estado corretamente! ")
        else:
            print("Esse código não existe no inventário")
    #no 5 ele novamente pede o codigo do equipamento e de acordo com o que foi dado mostra o equipamente e pede confirmação para deletar e depois da del
    elif escolha_menu == 5:
        for codigo in sorted(inventario):
            item = inventario[codigo]
            print(codigo, "|", item['nome'], item['estado'])

        new_inp2 = input(
            "Qual o código do equipamento que queres remover?"
        ).strip().upper()
        while new_inp2 in inventario:
            codigo_escolhido = inventario[new_inp2]['nome']
            print(f"O produto que escolheste é o: {codigo_escolhido}")
            deci2 = input("Tens a certeza que queres prosseguir? (s/n)")
            deci2 = deci2.strip().lower()
            if deci2 == 's':
                del inventario[new_inp2]
                while new_inp2 in lista_reparação:
                    lista_reparação.remove(new_inp2)
                    print(f"{new_inp2.upper()} foi eliminado da lista de "
                          f"reparação com sucesso!")
                historico.append(f"removeste: {new_inp2} / {codigo_escolhido}")
                print(f"{new_inp2.upper()} foi eliminado do inventário "
                      f"com sucesso!")

            elif deci2 == 'n':
                break
            else:
                print("Isso não é uma opção válida pedida")
  #no 6 faz uma verificação na lista de reparação se estiver vazia faz print que esta fazia else mostra a lista de reparação e se quer processar
    elif escolha_menu == 6:
        if not lista_reparação:
            print("A lista está toda vazia")
        else:
            contadorNum = 1
            for reparaçao in (lista_reparação):
                codigo_escolhido2 = inventario[reparaçao]['nome']
                print(f"{contadorNum}. Nome: {reparaçao} - "
                      f"{codigo_escolhido2}")
                contadorNum += 1
            deci3 = input("Queres processar todas as reparações? ")
            deci3 = deci3.strip().lower()
            if deci3 == 's':
                while lista_reparação:
                    historico.append(f"Estes foram processados e reparados: {lista_reparação[0]}")
                    inventario[lista_reparação[0]]['estado'] = 'operacional'
                    reparados.append(lista_reparação[0])
                    itemRemovido = lista_reparação.pop(0)
                    print(f"O {itemRemovido} vai ser reparado e ele vai ser "
                          f"removido da lista de reparação!")
                print(f"Equipamentos reparados nesta sessão: {reparados}")
    # no 7 ele faz quase a mesma coisa do 6 mas no 7 ele so mostra informaçoes/estatisticas como um for que se constroi 
    elif escolha_menu == 7:
        if not inventario:
            print("Inventário vazio!")
        else:
            # Lista com a quantidade de cada equipamento
            quantidades = [inventario[codigo]['quantidade']
                           for codigo in inventario]

            # Lista com o tipo de cada equipamento, e depois sem repetidos
            lista_tipos = []
            for codigo in inventario:
                lista_tipos.append(inventario[codigo]['tipo'])
            tipos_distintos = sorted(set(lista_tipos))

            # Dicionário com o número de registos por estado
            contagem_estados = {}
            for codigo in inventario:
                estado = inventario[codigo]['estado']
                if estado in contagem_estados:
                    contagem_estados[estado] += 1
                else:
                    contagem_estados[estado] = 1

            print(f"Número de registos: {len(inventario)}")
            print(f"Total de unidades: {sum(quantidades)}")
            print(f"Maior quantidade: {max(quantidades)}")
            print(f"Menor quantidade: {min(quantidades)}")
            print(f"Tipos existentes: {tipos_distintos}")

            print("Registos por estado -")
            for estado in contagem_estados:
                print(f"{estado}: {contagem_estados[estado]}")

            print("Unidades por sala:")
            for sala in SALAS:
                total_sala = 0
                for codigo in inventario:
                    if inventario[codigo]['sala'] == sala:
                        total_sala += inventario[codigo]['quantidade']
                print(f"{sala}: {total_sala}")
    # no 8 ele simplesmente mostra os ultimos 5 .appends que o historico teve com uma slice de -5
    elif escolha_menu == 8:
        if not historico:
            print("Ainda não fizeste nada")
        else:
            print("As tuas 5 últimas operações:")
            for operacao in historico[-5:]:
                print(operacao)
            print(f"Total de operações: {len(historico)}")
