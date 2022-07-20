def imprimir_mensagem():
    print("+-------------------------------+")
    print("| Seja Bem Vindo ao CalcEtec <3 |")
    print("+-------------------------------+")
    print("")

imprimir_mensagem()

num_tabuada = int(input("Informe o número multiplicador: "))

for i in range(0, 11):
    resultado = (num_tabuada * i)
    print(num_tabuada, "x", i, "=", resultado)