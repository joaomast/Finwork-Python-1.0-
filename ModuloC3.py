# ModuloC3: Modulo do Caso de uso 3

import csv # importa recursos
from ModuloValida import *

def det( ): # exibe detalhes sobre algum produto desejado
    while True:
        print("----------------------------------------------------------------")
        print("Digite 0 caso deseje retornar ao Menu")
        print("")
        opcoes()
        print("")
        x = valida_int( mensagem = "Acerca de qual desses produtos deseja ver mais detalhes? ", minimo = 0, maximo = 23 )
        print("")
        if x == 0:
            print("----------------------------------------------------------------")
            break
        else:
            exib_det( x )
            break
            
def exib_det(i): # procura na base e exibe detalhes
    arq_txt = open( "base_c3.txt", "r", newline = "", encoding = "utf-8" ) # abre o arquivo
    tab_txt = csv.DictReader( arq_txt ) # tabela como tupla de dicionários
    tabela = list( tab_txt ) # tabela como lista de dicionários
    print( tabela[i - 1]["Informacao"] ) # exibir mensagem com a informacao do produto
    arq_txt.close( )

def opcoes(): # chama as opções de produtos existentes
    arq_txt = open( "base_c3.txt", "r", newline = "", encoding = "utf-8" ) # abre o arquivo
    tab_txt = csv.DictReader( arq_txt ) # tabela como tupla de dicionários
    tabela = list( tab_txt ) # tabela como lista de dicionários

    for opcao in tabela:
        print( opcao["Opcoes"] )

    arq_txt.close( )
