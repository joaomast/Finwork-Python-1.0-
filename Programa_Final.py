# Módulo de Acesso ao Programa 

from ModuloC1 import *
from ModuloC2 import *
from ModuloC3 import *
from ModuloC4 import *
from ModuloC5 import *
from ModuloC6 import *
from ModuloC7 import * 
from ModuloMenu import *
from ModuloValida import *

while True:
    opcao = menuprincipal( )
    if opcao == 0:
        break
    elif opcao == 1:

        while True:
            opcaoi = menu_investidor( )
            
            if opcaoi == 0:
                break
            elif opcaoi == 1 :
                quest( 1 )
            elif opcaoi == 2 :
                prod( )
            elif opcaoi == 3 :
                det( )
                
    elif opcao == 2:
        while True:
            opcaoa = menu_assessor( )
            
            if opcaoa == 0:
                break
            elif opcaoa == 1 :
                quest( 1 )
            elif opcaoa == 2 :
                prod( )
            elif opcaoa == 3 :
                det( )
            elif opcaoa == 4 :
                prev( )
            elif opcaoa == 5 :
                tribut( )
            elif opcaoa == 6 :
                tabela( )
            elif opcaoa == 7:
                agenda( )
