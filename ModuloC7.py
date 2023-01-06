# ModuloC7: Modulo do caso de uso 7

from ModuloValida import * # importando recursos 
from ModuloC1 import *

agenda = [ ] # base de dados da agenda na memória
modificada = False # flag de agenda modificada
arquivo = "agenda.txt" # nome padrão do arquivo da agenda

def agenda():
        print("----------------------------------------------------------------")
        le( ) # cria ou abre arquivo inicial
        while True :
                opcao = menu( )
                if opcao == 0 : # trata a opção escolhida pelo usuário
                    if not modificada or \
                        input( "Sai sem gravar agenda existente (S/N)? ").lower( ) == "s" :
                        break
                elif opcao == 1 :
                    novo( )
                elif opcao == 2 :
                    altera( )
                elif opcao == 3 :
                    apaga( )
                elif opcao == 4 :
                    lista( )
                elif opcao == 5 :
                    grava( )
                elif opcao == 6 :
                    le( )


def pede_nome( padrao = "" ) : # pede nome do investidor 
    return texto( "Nome do Investidor: ", padrao )

def pede_api( ) : # pede api do investidor 
    return valida_int( """Digite 0 caso deseje realizar o teste de Análise de Perfil do Investidor

1 - Conservador
2 - Moderado
3 - Arrojado

Classificação do API do Investidor: """, 0, 3 )

def realiza_api( ): # realiza o api em caso de nunca ter realizado
        i = pede_api( )
        
        if i == 0:
                while True:
                        api = pergunta( )
                        if api == 0:
                                print("----------------------------------------------------------------")
                                break
                        else:
                                print_perfil( calc_perfil( api ) )
                                perfil = perfil_id( calc_perfil( api ) )
                                break
        else:
                perfil = i
        if perfil == 1:
                return "Conservador"
        elif perfil == 2:
                return "Moderado"
        elif perfil == 3:
                return "Arrojado"

def pede_trib( ): # pede esquema de tributação do investidor 
    i = valida_int( """1 - Simplificada
2 - Completa

Esquema de Tributação do Investidor: """, 1, 2)
    if i == 1:
                return "Simplificada"
    elif i == 2:
                return "Completa"


def pede_renda( ): # pede faixa de renda do investidor 
    i = valida_int( """1 - Até 1.903,98	
2 - De 1.903,99 até 2.826,65	
3 - De 2.826,66 até 3.751,05	
4 - De 3.751,06 até 4.664,68	
5 - Acima de 4.664,68

Faixa de renda do Investidor: """, 1, 5 )
    if i == 1:
                return "Até 1903.98"
    elif i == 2:
                return "De 1903.99 até 2826.65"
    elif i == 3:
                return "De 2826.66 até 3751.05"
    elif i == 4:
                return "De 3751.06 até 4664.68"
    elif i == 5:
                return "Acima de 4664.68"

def pede_porcrenda( ): # pede % da renda dedicada à previdência
    return valida_int( "Porcentagem da renda mensal direcionada à previdência do Investidor (digite a porcentagem em inteiro, exemplo: 10% = 10): ", 0, 100 )

def pede_tempo( ): # pede tempo de contribuição dedicada à previdência
    i = valida_int( """1 - Até 2 anos
2 - De 2 a 4 anos
3 - De 4 a 6 anos
4 - De 6 a 8 anos
5 - De 8 a 10 anos
6 - Acima de 10 anos

Tempo de contribuição de previdência desejado do Investidor: """, 1, 6)

    if i == 1:
                return "Até 2 anos"
    elif i == 2:
                return "De 2 a 4 anos"
    elif i == 3:
                return "De 4 a 6 anos"
    elif i == 4:
                return "De 6 a 8 anos"
    elif i == 5:
                return "De 8 a 10 anos"
    elif i == 6:
                return "Acima de 10 anos"


def pede_arquivo( ): # entra nome de arquivo, com o nome atual como padrão
    global arquivo
    arquivo = texto( "Nome do arquivo da agenda", arquivo )


def mostra_dados( nome, api, trib, renda, porcrenda, tempo ): # mostra contato
    print( "Nome: %s | API: %s | Esquema de Tributação: %s | Faixa de Renda: %s | Renda em Previdência: %s | Tempo de contribuição: %s" % ( nome, api, trib, renda, porcrenda, tempo ) )

def pesquisa( nome ) : # pesquisa contato na agenda
    nome = nome.lower( ) 
    for posicao, contato in enumerate( agenda ) :
        if contato[ 0 ].lower( ) == nome :
            return posicao
    return None

def novo( ) : # cria novo contato na agenda
    global agenda, modificada
    print("----------------------------------------------------------------")
    nome = pede_nome( )
    print("----------------------------------------------------------------")
    api = realiza_api( )
    print("----------------------------------------------------------------")
    trib = pede_trib( )
    print("----------------------------------------------------------------")
    renda = pede_renda( )
    print("----------------------------------------------------------------")
    porcrenda = pede_porcrenda( )
    print("----------------------------------------------------------------")
    tempo = pede_tempo( )
    agenda.append( [ nome, api, trib, renda, porcrenda, tempo ] )
    modificada = True

def altera( ): # modifica contato na agenda
    global agenda, modificada
    posicao = pesquisa( pede_nome( ) )
    if posicao != None :
        nome = agenda[ posicao ][ 0 ]
        api = agenda[ posicao ][ 1 ]
        trib = agenda[ posicao ][ 2 ]
        renda = agenda[ posicao ][ 3 ]
        porcrenda = agenda[ posicao ][ 4 ]
        tempo = agenda[ posicao ][ 5 ]
        print( "Encontrado:" )
        mostra_dados( nome, api, trib, renda, porcrenda, tempo )
        print("----------------------------------------------------------------")
        nome = pede_nome(nome )
        print("----------------------------------------------------------------")
        api = realiza_api()
        print("----------------------------------------------------------------")
        trib = pede_trib()
        print("----------------------------------------------------------------")
        renda = pede_renda()
        print("----------------------------------------------------------------")
        porcrenda = pede_porcrenda()
        print("----------------------------------------------------------------")
        tempo = pede_tempo()
        print("----------------------------------------------------------------")
        agenda[ posicao ] = [ nome, api, trib, renda, porcrenda, tempo ]
        modificada = True
    else :
        print( "Nome não encontrado" )

def apaga( ): # apaga contato da agenda
    global agenda, modificada
    nome = pede_nome( )
    posicao = pesquisa( nome )
    if posicao != None :
        del agenda[ posicao ]
        modificada = True
    else :
        print( "Nome não encontrado" )

def lista( ) : # mostra toda a agenda
    global agenda
    print("----------------------------------------------------------------")
    print( "Agenda" )
    print("")
    for contato in agenda :
        mostra_dados( contato[ 0 ], contato[ 1 ],contato[ 2 ],contato[ 3 ],contato[ 4 ],contato[ 5 ] )

def grava( ): # salva agenda no disco, com opção de mudar o nome do arquivo
    global agenda, modificada, arquivo
    pede_arquivo( )
    arquivo_texto = open( arquivo, "w" ) # (re)escreve o arquivo
    for contato in agenda :
        arquivo_texto.write( "%s,%s,%s,%s,%s,%s\n" % ( contato[ 0 ], contato[ 1 ],contato[ 2 ],contato[ 3 ],contato[ 4 ],contato[ 5 ] ) )
    arquivo_texto.close( )
    modificada = False

def le( ): # le agenda do arquivo
    global agenda, modificada, arquivo
    if modificada and \
        input( "Lê sem gravar agenda existente (S/N)? " ).lower( ) == "n" :
        return
    agenda = [ ] # limpa a agenda existente
    pede_arquivo( )
    try : # lê o arquivo apenas se ele existir
        arquivo_texto = open( arquivo, "r" )
        for linha in arquivo_texto.readlines( ) :
            nome, api, trib, renda, porcrenda, tempo = linha.strip( ).split( "," )
            agenda.append( [ nome, api, trib, renda, porcrenda, tempo ] )
        arquivo_texto.close( )
        modificada = False
    except FileNotFoundError :
        print( "Arquivo '%s' não existe, agenda vazia" % arquivo )

def menu( ): # menu da agenda
    print("----------------------------------------------------------------")
    print( """1 - Adicionar novo Investidor
2 - Alterar cadastro do Investidor
3 - Apagar cadastro do Investidor
4 - Listar cadastros existentes

5 - Gravar informações atualizadas
6 - Ler agendas pré-existentes
    
0 - Sair da agenda
    """ )
    return valida_int( "Escolha uma opção: ", 0, 6 )
