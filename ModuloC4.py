# ModuloC4: Modulo do caso de uso 4

import csv # importa recursos

def prev(): # exibe tipo de previdência ideal para o perfil
    while True:
        try:
            print("----------------------------------------------------------------")
            print("Digite 0 caso deseje retornar ao Menu")
            print("")
            perg_prev( 1,2 )
            print("")
            perg_prev( 1,1 )
            v = input()
            v = int( v )
            if v == 0:
                break
            else:
                if v >= 1 and v <= 2:
                    if v == 1:
                        print_prev( 1 )
                        break
                    elif v == 2:
                        print("----------------------------------------------------------------")
                        print("Digite 0 caso deseje retornar ao Menu")
                        print("")
                        x = porc_renda( )
                        if x == 0:
                            break
                        else:
                            print("")
                            print_prev( x )
                            break
                else:
                    print("Opção inválida, digite algo entre as opções exibidas")
        except:
            print("Digite uma das opções: ")

def porc_renda(): # pede a porcentagem da renda que o investidor deseja investir em previdência
    while True:
            perg_prev( 2, 1 )
            v = int( input("Digite aqui: ") )
            if v >= 0 and v <= 100:
                 if v <= 12:
                    i = 2
                    return i
                 else:
                    i = 3
                    return i
            else:
                print("Opção inválida, digite algo entre as opções exibidas")

def perg_prev(ID, pergouop): # busca perguntas e opções de resposta na base
    arq_csv = open( "baseperg_c4.txt", "r", newline = "", encoding = "utf-8" ) # abre o arquivo
    tab_csv = csv.DictReader( arq_csv ) # tabela como tupla de dicionários
    tabela = list( tab_csv ) # tabela como lista de dicionários
    if pergouop == 1:
        print( tabela[ID - 1]["Pergunta"] )
    elif pergouop == 2:
        print( tabela[ID - 1]["Opcao"] )
    arq_csv.close( )

def print_prev(i): # define funcao
    arq_csv = open( "baseresp_c4.txt", "r", newline = "", encoding = "utf-8" ) # abre o arquivo
    tab_csv = csv.DictReader( arq_csv ) # tabela como tupla de dicionários
    tabela = list( tab_csv ) # tabela como lista de dicionários
    print( tabela[i - 1]["Resposta"] ) # exibir mensagem com o perfil resultado
    arq_csv.close( )



