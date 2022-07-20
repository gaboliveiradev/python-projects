def start():
    print("+----------------------------------+")
    print("| Seja Bem Vindo(a) a Outlet014 <3 |")
    print("+----------------------------------+")
    print("")
    nome_cliente = str(input("Digite o nome do cliente: "))
    print("")
    return nome_cliente

start()
valor_total = 0

# --------------------------------- Módulo de Venda ---------------------------------
while True:
    print("=============== Menu De Vendas - Outlet14 ===============")
    nome_roupa = str(input("Digite o nome da roupa: "))
    qnt = int(input("Digite a quantidade de peças: "))
    valor_roupa_un = float(input("Digite o valor unitário da roupa R$: "))
    valor_roupa_vendida = (qnt * valor_roupa_un)
    print("Você vendeu", qnt, nome_roupa, "no valor de R$",valor_roupa_un,"cada.")
    print("Totalizando um valor total de: R$", valor_roupa_vendida, " Reais.")
    print("=========================================================")
    cmd = str(input("Deseja vender outra roupa (S/N): "))
    valor_total += valor_roupa_vendida
    
    if(cmd == "n" or cmd == "N"):
        break

# --------------------------------- Módulo de Pagamento ---------------------------------
print("Valor total: R$ {:.2f}".format(valor_total))
pgto = float(input("Digite o valor recebido do cliente: R$"))
troco = (pgto - valor_total)

if(troco == 0):
    print("+----------------------------------------------------+")
    print("| A Outlet014 Agradeçe a Sua Compra! Volte Sempre :) |")
    print("+----------------------------------------------------+")
elif(troco < 0):
    print("Você está devendo um total de R$ {:.2f}".format(troco))
else:
    print("Seu troco é de R$ {:.2f}".format(troco))