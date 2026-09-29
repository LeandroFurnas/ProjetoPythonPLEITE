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
menu = '\n------------Menu DE INVENTÁRIO -----------|\n'
menu += '| 1 - Mostrar equipamentos                 |'
menu += '| 2 - Adicionar mais equipamento           |' 
menu += '| 3 - Pesquisar nos equipamento existentes |'
menu += '| 4 - Alterar o estado de um equipamento   |'
menu += '| 5 - Remover um equipamento               |'
menu += '| 6 - Lista de reparação                   |'
menu += '| 7 - Estatísticas                         |'                
menu += '| 8 - Histórico de operações               |'
menu += '| 0 - Sair                                 |'
menu += '--------------------------------------------'
#a flag que aprendi a poucas aulas mas da jeito
flag_ativo = True

while flag_ativo:
    print(menu)
    escolha_menu = int(input("Escolhe uma opção: \n"))
    if escolha_menu < 0 or escolha_menu > 8:
        
    if escolha_menu == 0:
        print()
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
        codigo = input('Qual o codigo do produto que queres? ').strip().upper()
        if codigo == '':
            continue
        elif codigo not in inventario
            print("Nao existe nada no inventario com esse codigo! ")
            continue
        elif codigo in iventario




    

    
