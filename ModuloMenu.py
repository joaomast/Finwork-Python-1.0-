#ModuloMenu

from ModuloValida import *
def menuprincipal( ) : # menu principal do software
    print("----------------------------------------------------------------")
    print( """0 - Sair do programa
            
1 - Acessar o modo para Investidor
2 - Acessar o modo para Consultor/Assessor de Investimentos         
""" )
    return valida_int( "Escolha uma opção para acesso: ", 0, 2 )

def menu_assessor( ): # menu do modo para assessor
    print("----------------------------------------------------------------")
    print( """0 - Sair do modo para Consultor/Assessor de Investimentos
            
1 - Realizar Análise do Perfil do Investidor
2 - Consultar produtos indicados para o Perfil
3 - Acessar detalhes sobre algum produto de investimento
4 - Acessar recomendação de tipo de previdência
5 - Acessar recomendação de tipo de tributação para previdência
6 - Consultar tabelas de tributação de previdência

7 - Acessar agenda de Investidores
""" )
    return valida_int( "Escolha uma opção para acesso: ", 0, 7 )
    
def menu_investidor( ): # menu do modo para investidor
    print("----------------------------------------------------------------")
    print( """0 - Sair do modo para Investidor
            
1 - Realizar Análise do Perfil do Investidor
2 - Consultar produtos indicados para o Perfil
3 - Acessar detalhes sobre algum produto de investimento
""" )
    return valida_int( "Escolha uma opção para acesso: ", 0, 3 )
    print("----------------------------------------------------------------")
    
