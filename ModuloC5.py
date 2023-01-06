# ModuloC5: Modulo do caso de uso 5

import csv # importa recursos
from ModuloValida import *

def tribut( ): # exibe escolha de tabela de tributação ideal
    while True:
        print("----------------------------------------------------------------")
        print("Digite 0 se deseja retornar ao Menu")
        print("")
        opcoes( "q1_c5.txt" ) # exibe opcoes para a questão
        print("")
        renda = valida_int( "Em qual intervalo de renda mensal o investidor se encaixa? ", 0, 5 )
        if renda == 0:
            break
        else:
            print("----------------------------------------------------------------")
            print("Digite 0 se deseja retornar ao Menu")
            print("")
            opcoes( "q2_c5.txt" ) # exibe opcoes para a questão
            print("")
            tempo = valida_int( "Por quanto tempo o investidor deseja continuar contribuindo? ", 0, 6 )

            if tempo == 0:
                break
            else:
                print("")
                calc_tabela( renda, tempo )
                break
    

def print_tab( i ): # printa tabela indicada
    arq_txt = open( "indicacoes.txt", "r", newline = "", encoding = "utf-8" ) # abre o arquivo
    tab_txt = csv.DictReader( arq_txt ) # tabela como tupla de dicionários
    tabela = list( tab_txt ) # tabela como lista de dicionários

    print( tabela[i - 1]["Tabela"] ) # exibir mensagem com a tabela indicada
    arq_txt.close( )

def opcoes( base ): # define funcao que chama as opcoes possiveis de acordo com base   
    base = str( base )
    arq_txt = open( base, "r", newline = "", encoding = "utf-8" ) # abre o arquivo
    tab_txt = csv.DictReader( arq_txt ) # tabela como tupla de dicionários
    tabela = list( tab_txt ) # tabela como lista de dicionários

    for opcao in tabela:
        print( opcao["Opcao"] )

    arq_txt.close( )

def calc_tabela( renda, tempo ): # calcula a tabela de acordo com condicionais teóricas e printa resposta
    if renda == 1 or renda == 2:
        print_tab( 1 )
    else:
        if renda == 3:
            if tempo <= 5:
                print_tab( 1 )
            else:
                print_tab( 2 )
        elif renda == 4:
            if tempo <= 3:
                prin_tab( 1 )
            else:
                print_tab( 2 )
        elif renda == 5:
            if tempo <= 2:
                print_tab( 1 )
            else:
                print_tab( 2 )
