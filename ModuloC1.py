# ModuloC1: Modulo do caso de uso 1

import csv # importa recursos
from ModuloValida import *
from ModuloMenu import *
from ModuloC2 import *

def quest( acessarc2 = 0 ): # executa o questionario de API, com opção de sugerir acessar o caso de uso 2 (se acessarc2 = 1)
    while True:
        api = pergunta( )
    
        if api == 0:
            break
        else:
            print_perfil( calc_perfil( api ) )

            if acessarc2 == 1:
                acessar_c2( perfil_id( calc_perfil( api ) ) )
                break
            else:
                break

def print_perfil( i ): # printa informações sobre o perfil com base no questionario de API
    arq_txt = open( "baseperfil_c1.txt", "r", newline = "", encoding = "utf-8" ) # abre o arquivo
    tab_txt = csv.DictReader( arq_txt ) # tabela como tupla de dicionários
    tabela = list( tab_txt ) # tabela como lista de dicionários
    print( "" ) # espaço na exibição
    print( "O seu perfil é " + tabela[i]["Perfil"] ) # exibir mensagem com o perfil resultado
    print( tabela[i]["Detalhe"] ) # exibe detalhes sobre o perfil
    print( "----------------------------------------------------------------" ) # barra na exibição
    arq_txt.close( )

def pergunta( ): # define funcao que le perguntas do questionário
    arq_txt = open( "basequest_c1.txt", "r", newline = "", encoding = "utf-8" ) # abre o arquivo com as questões
    tab_txt = csv.DictReader( arq_txt ) # tabela como tupla de dicionários
    tabela = list( tab_txt ) # tabela como lista de dicionários
    api = [ 0, 0, 0, 0, 0, 0, 0, 0 ] # define lista vazia para inserir respostas
    x = 0
    
    while x < ( len(tabela) - 1 ): # passa por todas as questões
        print( "----------------------------------------------------------------" )
        print( "Digite 0 caso deseje retornar ao Menu" )
        print( "" )
        opcoesc1( x + 1 ) # exibe as opções de resposta para a questão i
        print("")
        if x == 2 or x == 4 or x == 5: # define validação de entrada para questões com 3 alternativas
            y = valida_int( tabela[x]["Questao"] + " ", minimo = 0, maximo = 3 ) 
        else: # define validação de entrada para questões com 4 alternativas
            y = valida_int( tabela[x]["Questao"] + " ", minimo = 0, maximo = 4 )   
        if y != 0:
            api[x] = y
            x += 1   
        else:
            api = 0 # opção de retorno ao menu
            break
    return api

    arq_txt.close( )

def opcoesc1( opcao ): # chama as opcoes disponiveis para cada uma das questoes
    arq_txt = open( "baseopcoes_c1.txt", "r", newline = "", encoding = "utf-8" ) # abre o arquivo
    tab_txt = csv.DictReader( arq_txt ) # tabela como tupla de dicionários
    tabela = list( tab_txt ) # tabela como lista de dicionários
    opcao = str( opcao ) # transforma as opções em string
    for i in tabela:
            print( i[opcao] ) # exibe a opção
    arq_txt.close( )

def calc_perfil( lista ): # calcula o perfil com a lista criada com base na matriz de calcúlo no arquivo txt
    arq_txt = open( "matriz_c1.txt", "r", newline = "", encoding = "utf-8" ) # abre o arquivo
    tab_txt = csv.DictReader( arq_txt ) # tabela como tupla de dicionários
    tabela = list( tab_txt ) # tabela como lista de dicionários
    resultado = 0
    x = 0
    
    while x < len(lista):
       index = lista[x]
       if index == 1:
           index = "1"
       elif index == 2:
           index = "2"
       elif index == 3:
           index = "3"
       elif index == 4:
           index = "4"

       resultado = int( tabela[x][index] ) + resultado

       x += 1
    return resultado # somatório do valor das questões

    arq_txt.close( )

def acessar_c2( perfil ): # acesso ao caso de uso 2 direto do questionário
    x = valida_int("""Digite 0 caso deseje retornar ao Menu

1 - Sim
2 - Não

Deseja visualizar os produtos indicados para o seu perfil? """, 0, 2)

    if x == 1:
        exib_prod( perfil )


def perfil_id( i ): # encontra id do API para exibir produtos indicados na função acessar_c2
    arq_txt = open( "baseperfil_c1.txt", "r", newline = "", encoding = "utf-8" ) # abre o arquivo
    tab_txt = csv.DictReader( arq_txt ) # tabela como tupla de dicionários
    tabela = list( tab_txt ) # tabela como lista de dicionários
    perfil = tabela[i]["Perfil"]

    if perfil == "Conservador":
        perfil = 1
    elif perfil == "Moderado":
        perfil = 2
    elif perfil == "Arrojado":
        perfil = 3

    return perfil
    arq_txt.close( )
