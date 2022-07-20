# ================= Mude Aqui Os Valores ===================
#############################################################
valor_mussarela = 22.60
valor_mortadela = 8.98
valor_presunto = 31.03
valor_peito_peru = 58.90

porcentagem_mussarela = 0.05
porcentagem_mortadela = 0.065
porcentagem_presunto = 0.045
porcentagem_peito_peru = 0.025
#############################################################

# =========================== Inicio Do Código ====================================
qnt_mussarela = float(input("Digite a quantidade de mussarela vendida(KG): "))
qnt_mortadela = float(input("Digite a quantidade de mortadela vendida(KG): "))
qnt_presunto = float(input("Digite a quantidade de presunto vendido(KG): "))
qnt_peito_peru = float(input("Digite a quantidade de peito de peru vendida(KG): "))

def calcular_total(qnt, valor):
    total = qnt * valor
    return total

def calcular_comissao(total, porcentagem):
    comissao = total * porcentagem
    return comissao

print("========== Mussarela =========")
print("Quantidade Vendida(KG): ", qnt_mussarela, "KG")
print("Valor Total: R$", round(calcular_total(qnt_mussarela, valor_mussarela)), "Reais")
print("Comissão Do Vendedor: R$", round(calcular_comissao(calcular_total(qnt_mussarela, valor_mussarela), porcentagem_mussarela)), "Reais")
print("========== Mortadela =========")
print("Quantidade Vendida(KG): ", qnt_mortadela, "KG")
print("Valor Total: R$", round(calcular_total(qnt_mortadela, valor_mortadela)), "Reais")
print("Comissão Do Vendedor: R$", round(calcular_comissao(calcular_total(qnt_mortadela, valor_mortadela), porcentagem_mortadela)), "Reais")
print("========== Presunto =========")
print("Quantidade Vendida(KG): ", qnt_presunto, "KG")
print("Valor Total: R$", round(calcular_total(qnt_presunto, valor_presunto)), "Reais")
print("Comissão Do Vendedor: R$", round(calcular_comissao(calcular_total(qnt_presunto, valor_presunto), porcentagem_presunto)), "Reais")
print("========== Peito De Peru =========")
print("Quantidade Vendida(KG): ", qnt_peito_peru, "KG")
print("Valor Total: R$", round(calcular_total(qnt_peito_peru, valor_peito_peru)), "Reais")
print("Comissão Do Vendedor: R$", round(calcular_comissao(calcular_total(qnt_peito_peru, valor_peito_peru), porcentagem_peito_peru)), "Reais")