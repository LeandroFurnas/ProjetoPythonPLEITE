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
        print("Isso não existe! Tenta Novamente")    
        continue
    if escolha_menu == 0:
        op = input("Queres sair do programa (y/n)?")
        if op == 'y':
            continue
        else:
            break
    if escolha_menu == 1:
        if not inventario:
            print('O inventário está vazio.')
        else:
            print('CÓDIGO | NOME | SALA | QUANTIDADE | ESTADO')
            for codigo in sorted(inventario):
                item = inventario[codigo]
                print(codigo, "|", item['nome'], "|", item['sala'], "|", item['quantidade'], "un. |", item['estado'])
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

    

        
        





    

    
