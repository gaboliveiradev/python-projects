nota_prova = float(input("Informe a nota da prova: "))
nota_trabalho = float(input("Informe a nota do trabalho: "))

media = (nota_prova + nota_trabalho) / 2

print("Sua média é de: ", media)

if media >= 6:
    print("PARABÉNS você está aprovado para entrar no club das Elietes <3")

else:
    print("Você não foi aprovado para entrar no clube das Elietes :(")