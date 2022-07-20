def start(teste):
    print("+----------------------------------+")
    print("| Seja Bem Vindo(a) a Outlet014 <3 |")
    print("+----------------------------------+")
    nome_cliente = str(input("Digite o nome do cliente: "))
    print("")
    return nome_cliente

start()
nomes_roupas_all = []
valores_unit_roupas = []
qnt_roupas_all = []
venda_total = 0

print("=============== Menu De Vendas - Outlet14 ===============")
print("")
while True:
    nome_roupa = str(input("Digite o nome da roupa: "))
    nomes_roupas_all.append(nome_roupa)
    valor_unit = float(input("Digite o valor unitário: R$ "))
    valores_unit_roupas.append(valor_unit)
    qnt_roupas = int(input("Digite a quantidade de roupa: "))
    qnt_roupas_all.append(qnt_roupas)
    cmd = str(input("Deseja continuar vendendo (S/N): "))
    print("")
    
    if(cmd == "n" or cmd == "N"):
        break

tamanho = len(nomes_roupas_all)

print("=============== Histórico de Compras ===============")
for i in range(0, tamanho):
    valor_roupa_vendida = (qnt_roupas_all[i] * valores_unit_roupas[i])
    print("")
    print("Nome da Peça: ", nomes_roupas_all[i])
    print("Preço por Peça: R${:.2f} Reais".format(valores_unit_roupas[i]))
    print("Quantidade:", qnt_roupas_all[i])
    print("Valor total: R${:.2f} Reais".format(valor_roupa_vendida))
    print("")
    venda_total += valor_roupa_vendida

print("=============== Faça Seu Pagamento ===============")
print("")
print("Valor Total da Compra: R${:.2f}".format(venda_total))
pgto = float(input("Digite a quantia recebida pelo cliente: R$"))

if(pgto < venda_total):
    falta_pagar = (venda_total - pgto)
    print("")
    print("Você está devendo uma quantia de R$-", falta_pagar)
else:
    troco = (pgto - venda_total)
    print("")
    print("Obrigado por comprar conosco. Seu troco é de R$", troco)

print("")
print("+------------------------+")
print("| Obrigado volte sempre! |")
print("+------------------------+")