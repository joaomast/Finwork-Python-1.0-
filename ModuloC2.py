# ModuloC2: Modulo do Caso de uso 2

import csv # importa recursos
from ModuloValida import *

def prod( ): # exibe recomendacoes de produtos de acordo com o perfil
    while True:
        print("----------------------------------------------------------------")
        x = valida_int("""Digite 0 caso deseje retornar ao Menu

1 - Conservador
2 - Moderado
3 - Arrojado

Qual é o seu Perfil de Investidor? """, 0, 3)

        if x == 0:
            print("----------------------------------------------------------------")
            break
        else:
            exib_prod( x )
            break
                
def exib_prod( i ): # procura produtos na base e os exibe
    arq_txt = open( "base_c2.txt", "r", newline = "", encoding = "utf-8" ) # abre o arquivo
    tab_txt = csv.DictReader( arq_txt ) # tabela como tupla de dicionários
    tabela = list( tab_txt ) # tabela como lista de dicionários

    print("")
    print( tabela[i - 1]["Indicacao"] ) # exibir mensagem com a informacao dos produtos recomendados para o perfil
    
    arq_txt.close( )

