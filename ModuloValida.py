#ModuloValida: módulo de validação das entradas

def valida_int( mensagem, minimo, maximo ): # validacao de entrada de inteiro
    while True:
        try:
            v = int( input(mensagem) )
            if v >= minimo and v <= maximo:
                return v
            else:
                print("Opção inválida, digite algo entre as opções exibidas")
                print( "----------------------------------------------------------------" )
        except:
            print("Digite uma das opções do programa: ")
            print( "----------------------------------------------------------------" )


def texto( pergunta, padrao = "" ): # entra texto não vazio com valor padrão opcional
    while True :
        if padrao == "" :
            string = input( pergunta )
        else :
            string = input( pergunta + " (padrão = %s):" % padrao )
        if string != "" :
            return string
        elif padrao != "" :
            return padrao
        print( "Entrada inválida, favor digitar pelo menos um caractere" )
        print( "----------------------------------------------------------------" )
