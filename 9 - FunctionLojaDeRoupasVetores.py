w = open("logs.txt", "a")

def imprimir_mensagem_pegar_dados():
    print("######## ######## ########  ######   ######  ########  #######  ########  ######## ")
    print("##          ##    ##       ##    ## ##    ##    ##    ##     ## ##     ## ##      ")
    print("##          ##    ##       ##       ##          ##    ##     ## ##     ## ##       ")
    print("######      ##    ######   ##        ######     ##    ##     ## ########  ######   ")
    print("##          ##    ##       ##             ##    ##    ##     ## ##   ##   ##       ")
    print("##          ##    ##       ##    ## ##    ##    ##    ##     ## ##    ##  ##       ")
    print("########    ##    ########  ######   ######     ##     #######  ##     ## ######## ")
    print("")
    nome_cliente = str(input("Digite o nome do cliente da vez: "))
    w.write("======== Log de Sistema - {} ========".format(nome_cliente))