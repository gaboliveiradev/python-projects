import colorama
from colorama import Back, Fore, Style

def mensagem_boas_vindas():
    print("+---------------------------------+")
    print("| Seja Bem Vindo(a) Ao DesIlusão. |")
    print("+---------------------------------+")

mensagem_boas_vindas()
salario_bruto = float(input(Style.BRIGHT + "Digite seu salário bruto: "))
qnt_dependentes = float(input(Fore.MAGENTA + "Digite a quantia de dependentes: "))

primeira_faixa_inss = 0
segunda_faixa_inss = 0
terceira_faixa_inss = 0
quarta_faixa_inss = 0

if (salario_bruto <= 1100):
    primeira_faixa_inss = (salario_bruto * 0.075)

elif (salario_bruto > 1100):
    primeira_faixa_inss = (1100 * 0.075)

elif (salario_bruto <= 2203.48):
    segunda_faixa_inss = (salario_bruto - 1100) * 0.09

elif (salario_bruto > 2203.48):
    segunda_faixa_inss = (2203.48 - 1100) * 0.09

elif (salario_bruto <= 3305.22):
    terceira_faixa_inss = (salario_bruto - 2203.48) * 0.12

elif (salario_bruto > 3305.22):
    terceira_faixa_inss = (3305.22 - 2203.48) * 0.12

elif (salario_bruto <= 6433.57):
    quarta_faixa_inss = (salario_bruto - 3305.22) * 0.14

elif (salario_bruto > 6433.57):
    quarta_faixa_inss = (6433.57 - 3305.22) * 0.14

total_desconto_inss = primeira_faixa_inss + segunda_faixa_inss + terceira_faixa_inss + quarta_faixa_inss
salario_descontado_inss = salario_bruto - total_desconto_inss - (qnt_dependentes * 189.59)

if (salario_descontado_inss >= 1903.99) and (salario_descontado_inss <= 2826.65):
    ir = (salario_descontado_inss * 0.075) - 142.8
elif (salario_descontado_inss >= 2826.66) and (salario_descontado_inss <= 3751.05):
    ir = (salario_descontado_inss * 0.15) - 354.8
elif (salario_descontado_inss >= 3751.06) and (salario_descontado_inss <= 4664.68):
    ir = (salario_descontado_inss * 0.225) - 636.13
else:
    ir = (salario_descontado_inss * 0.275) - 869.36

total_descontos = (ir + total_desconto_inss)
salario_liquido = (salario_bruto - total_descontos)

print("")
print(Fore.RED + "===============X===============")
print(Fore.GREEN + "Descontos INSS: R${:.2f}".format(total_desconto_inss))
print(Fore.GREEN + "Descontos IRRF: R${:.2f}".format(ir))
print(Fore.GREEN + "Total dos Descontos: R${:.2f}".format(total_descontos))
print(Fore.GREEN + "Salário Liquido: R${:.2f}".format(salario_liquido))
print(Fore.RED + "===============X===============")