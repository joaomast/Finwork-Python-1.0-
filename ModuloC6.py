# ModuloC6: Modulo do caso de uso 6

import csv # importa recursos
import cv2 # importa recursos
from ModuloValida import *

def tabela( ): # exibe tabela que o assessor deseja consultar
    while True:
        print("----------------------------------------------------------------")
        print("Digite 0 para retornar ao Menu")
        x = valida_int("""
1 - Tabela Progressiva
2 - Tabela Regressiva
            
Qual tabela deseja consultar? """, 0, 2)
        if x == 0:
            print("----------------------------------------------------------------")
            break
        else:
            proc_tabela( x )
            break

def proc_tabela( tabela ): # procura tabela na base e exibe em nova janela
    if tabela == 1:
        exibir = cv2.imread( "Progressiva.jpg" )
        cv2.imshow( "Tabela Progressiva", exibir )
        cv2.waitKey( 0 )
    elif tabela == 2:
        exibir = cv2.imread( "Regressiva.jpg" )
        cv2.imshow( "Tabela Regressiva", exibir )
        cv2.waitKey( 0 )
